-- Ajuste os caminhos/tipos conforme o banco utilizado.
-- Tabelas esperadas: orders, customers, reviews.
-- Idealmente, carregar CSVs para tabelas com datas em DATE/TIMESTAMP.

-- 1) Base de análise no nível do pedido.
WITH review_por_pedido AS (
    SELECT order_id, AVG(review_score) AS review_score
    FROM reviews
    GROUP BY order_id
),
base AS (
    SELECT
        o.order_id,
        c.customer_state,
        o.order_purchase_timestamp,
        o.order_delivered_customer_date,
        o.order_estimated_delivery_date,
        r.review_score,
        DATE_DIFF('day', o.order_estimated_delivery_date,
                  o.order_delivered_customer_date) AS atraso_dias,
        DATE_DIFF('day', o.order_purchase_timestamp,
                  o.order_delivered_customer_date) AS tempo_entrega_dias
    FROM orders o
    LEFT JOIN customers c ON o.customer_id = c.customer_id
    LEFT JOIN review_por_pedido r ON o.order_id = r.order_id
    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL
      AND o.order_estimated_delivery_date IS NOT NULL
)
SELECT
    COUNT(*) AS pedidos,
    AVG(CASE WHEN atraso_dias <= 0 THEN 1.0 ELSE 0.0 END) * 100 AS percentual_no_prazo,
    AVG(CASE WHEN atraso_dias > 0 THEN atraso_dias END) AS atraso_medio_dias_atrasados,
    AVG(tempo_entrega_dias) AS tempo_medio_entrega,
    AVG(review_score) AS nota_media
FROM base;

-- 2) Nota média por pontualidade.
WITH review_por_pedido AS (
    SELECT order_id, AVG(review_score) AS review_score
    FROM reviews GROUP BY order_id
),
base AS (
    SELECT o.order_id, r.review_score,
           DATE_DIFF('day', o.order_estimated_delivery_date,
                     o.order_delivered_customer_date) AS atraso_dias
    FROM orders o LEFT JOIN review_por_pedido r ON o.order_id = r.order_id
    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL
      AND o.order_estimated_delivery_date IS NOT NULL
)
SELECT CASE WHEN atraso_dias <= 0 THEN 'No prazo' ELSE 'Atrasado' END AS faixa_entrega,
       COUNT(*) AS pedidos, AVG(review_score) AS nota_media
FROM base
GROUP BY 1;

-- Observação: DATE_DIFF varia entre bancos (BigQuery usa DATE_DIFF(data_fim,data_inicio,DAY)).
