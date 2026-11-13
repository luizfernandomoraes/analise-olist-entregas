# Projeto de Análise de Dados — Entregas e satisfação no e-commerce brasileiro

**Pergunta central:** como o cumprimento do prazo de entrega se relaciona com a satisfação dos clientes?

Projeto acadêmico com a base pública *Brazilian E-Commerce Public Dataset by Olist* (pedidos de 2016–2018). Os dados são históricos e anonimizados; não representam o desempenho atual do comércio eletrônico brasileiro.

## Objetivos
- Medir pontualidade e atraso das entregas.
- Comparar avaliações de pedidos entregues no prazo e atrasados.
- Identificar diferenças por estado e mês de compra.
- Transformar achados em recomendações operacionais.

## Fonte de dados
Baixe a base no [Kaggle — Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) e extraia os CSVs para `data/raw/`. O projeto usa:
- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_customers_dataset.csv`

A base completa também contém pagamentos, produtos, vendedores, geolocalização e tradução de categorias. Consulte `docs/fontes_e_coleta.md`.

## Como executar
1. Instale Python 3.10+.
2. `pip install -r requirements.txt`
3. Baixe e extraia os CSVs em `data/raw/`.
4. Execute `python scripts/analise_olist.py`.
5. Os arquivos prontos para o Looker Studio serão salvos em `data/processed/`.

## Estrutura
- `docs/`: problema, fontes, metodologia e relatório de insights.
- `scripts/analise_olist.py`: limpeza, junções, EDA e exportação.
- `notebooks/eda_olist.ipynb`: notebook para exploração passo a passo.
- `sql/consultas.sql`: consultas equivalentes para análise em SQL.
- `data/raw/`: CSVs originais (não versionar).
- `data/processed/`: tabelas agregadas para visualização (geradas pelo script).

## Métricas e definições
- **Atraso (dias):** data real de entrega menos data estimada. Valor positivo = atrasou; zero ou negativo = no prazo.
- **Entrega no prazo:** entrega real menor ou igual à data estimada.
- **Tempo de entrega (dias):** entrega real menos compra.
- **Avaliação:** nota de 1 a 5 registrada na tabela de avaliações.

A análise principal considera somente pedidos com status `delivered` e datas reais/estimadas disponíveis. As médias de avaliação são calculadas no nível do pedido após consolidar avaliações duplicadas.

## Limitações
- Período observado: 2016–2018.
- Dados observacionais não demonstram causalidade.
- Pedidos sem data real de entrega não entram no cálculo de pontualidade.
- Pode haver mais de uma avaliação por pedido; o script consolida pela média.
- O dataset é uma amostra de uma operação/plataforma, não de todo o mercado brasileiro.

## Próximas etapas
Depois de executar o script, importe `kpis_gerais.csv`, `por_estado.csv`, `por_mes.csv` e `avaliacoes_prazo.csv` no Looker Studio. Orientações em `docs/dashboard_looker.md`.
