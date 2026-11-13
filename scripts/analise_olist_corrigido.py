
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)


def read_csv(name):
    path = RAW / name
    if not path.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {path}. "
            "Baixe os CSVs do Kaggle e extraia em data/raw/."
        )
    return pd.read_csv(path, low_memory=False)


# 1. Carregamento dos dados
orders = read_csv("olist_orders_dataset.csv")
reviews = read_csv("olist_order_reviews_dataset.csv")
customers = read_csv("olist_customers_dataset.csv")

date_cols = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")


# 2. Tratamento das avaliações
reviews["review_score"] = pd.to_numeric(
    reviews["review_score"], errors="coerce"
)

reviews_order = reviews.groupby("order_id", as_index=False).agg(
    review_score=("review_score", "mean"),
    quantidade_avaliacoes=("review_score", "count")
)


# 3. Tratamento dos clientes
customers_order = customers[
    ["customer_id", "customer_state"]
].drop_duplicates("customer_id")


# 4. Junção das tabelas
df = orders.merge(reviews_order, on="order_id", how="left")
df = df.merge(customers_order, on="customer_id", how="left")


# 5. Seleção dos pedidos entregues com datas válidas
df = df[
    (df["order_status"] == "delivered") &
    df["order_delivered_customer_date"].notna() &
    df["order_estimated_delivery_date"].notna() &
    df["order_purchase_timestamp"].notna()
].copy()


# 6. Criação das variáveis de entrega
df["atraso_dias"] = (
    df["order_delivered_customer_date"] -
    df["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

df["tempo_entrega_dias"] = (
    df["order_delivered_customer_date"] -
    df["order_purchase_timestamp"]
).dt.total_seconds() / 86400

# Remover tempos de entrega negativos
df = df[df["tempo_entrega_dias"] >= 0].copy()

# Classificação do prazo
df["entregue_no_prazo"] = df["atraso_dias"] <= 0

df["faixa_entrega"] = np.where(
    df["entregue_no_prazo"],
    "No prazo",
    "Atrasado"
)

df["mes_compra"] = (
    df["order_purchase_timestamp"].dt.to_period("M").astype(str)
)


# Calcula a média somente dos atrasos reais (valores maiores que zero).
# Se não houver pedidos atrasados no grupo, retorna NaN.
def media_atraso_positivo(valores):
    atrasos = valores[valores > 0]
    if atrasos.empty:
        return np.nan
    return atrasos.mean()


# 7. KPI geral
kpis = pd.DataFrame([{
    "pedidos_analisados": int(df["order_id"].nunique()),
    "percentual_no_prazo": round(
        df["entregue_no_prazo"].mean() * 100, 2
    ),
    "percentual_atrasados": round(
        (~df["entregue_no_prazo"]).mean() * 100, 2
    ),
    "atraso_medio_dias_atrasados": round(
        df.loc[df["atraso_dias"] > 0, "atraso_dias"].mean(), 2
    ),
    "tempo_medio_entrega_dias": round(
        df["tempo_entrega_dias"].mean(), 2
    ),
    "nota_media": round(df["review_score"].mean(), 2),
}])

kpis.to_csv(OUT / "kpis_gerais.csv", index=False)


# 8. Satisfação por faixa de prazo
avaliacoes = df.groupby("faixa_entrega", as_index=False).agg(
    pedidos=("order_id", "nunique"),
    nota_media=("review_score", "mean"),
    percentual_com_avaliacao=(
        "review_score",
        lambda s: s.notna().mean() * 100
    ),
    atraso_medio_dias=(
        "atraso_dias",
        media_atraso_positivo
    ),
)

avaliacoes[
    ["nota_media", "percentual_com_avaliacao", "atraso_medio_dias"]
] = avaliacoes[
    ["nota_media", "percentual_com_avaliacao", "atraso_medio_dias"]
].round(2)

avaliacoes.to_csv(OUT / "avaliacoes_prazo.csv", index=False)


# 9. Análise por estado
estado = df.groupby("customer_state", dropna=False).agg(
    pedidos=("order_id", "nunique"),
    percentual_no_prazo=(
        "entregue_no_prazo",
        lambda s: s.mean() * 100
    ),
    atraso_medio_dias=(
        "atraso_dias",
        media_atraso_positivo
    ),
    nota_media=("review_score", "mean"),
).reset_index().rename(
    columns={"customer_state": "estado"}
)

estado[
    ["percentual_no_prazo", "atraso_medio_dias", "nota_media"]
] = estado[
    ["percentual_no_prazo", "atraso_medio_dias", "nota_media"]
].round(2)

estado.to_csv(OUT / "por_estado.csv", index=False)


# 10. Análise por mês de compra
mes = df.groupby("mes_compra", as_index=False).agg(
    pedidos=("order_id", "nunique"),
    percentual_no_prazo=(
        "entregue_no_prazo",
        lambda s: s.mean() * 100
    ),
    atraso_medio_dias=(
        "atraso_dias",
        media_atraso_positivo
    ),
    nota_media=("review_score", "mean"),
)

mes[
    ["percentual_no_prazo", "atraso_medio_dias", "nota_media"]
] = mes[
    ["percentual_no_prazo", "atraso_medio_dias", "nota_media"]
].round(2)

mes.to_csv(OUT / "por_mes.csv", index=False)


# 11. Base analítica detalhada
df["mes_ano"] = df["order_purchase_timestamp"].dt.strftime("%Y-%m")

cols = [
    "order_id",
    "customer_state",
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "atraso_dias",
    "tempo_entrega_dias",
    "entregue_no_prazo",
    "faixa_entrega",
    "review_score",
    "mes_compra",
    "mes_ano"
]

df[cols].to_csv(OUT / "base_analitica.csv", index=False)


# 12. Resultado final
print("EDA concluída. Arquivos gerados em:", OUT)
print("\nKPIs gerais:\n", kpis.to_string(index=False))
print("\nAvaliações por faixa de prazo:\n", avaliacoes.to_string(index=False))
print("\nAnálise por estado:\n", estado.to_string(index=False))
print("\nAnálise mensal:\n", mes.to_string(index=False))
