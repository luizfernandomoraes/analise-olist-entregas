# 3. Metodologia da análise exploratória (EDA)

## Ferramentas
- Python: pandas, numpy e matplotlib.
- SQL: consultas de validação e agregação.
- Looker Studio: visualização dos resultados.

## Preparação
1. Ler os CSVs com identificadores como texto.
2. Converter datas para datetime.
3. Filtrar pedidos entregues com datas real e prevista válidas.
4. Consolidar avaliações por pedido para evitar duplicidade na junção.
5. Consolidar localização do cliente por pedido.
6. Calcular atraso, tempo de entrega e indicador de pontualidade.
7. Verificar nulos, duplicidades e valores extremos.

## Variáveis derivadas
- `atraso_dias = entrega_real - entrega_prevista`
- `tempo_entrega_dias = entrega_real - compra`
- `entregue_no_prazo = atraso_dias <= 0`
- `mes_compra = mês da compra`
- `faixa_entrega = No prazo / Atrasado`

## Análises
- estatísticas descritivas de atraso e tempo de entrega;
- percentual de pontualidade;
- nota média por faixa de prazo;
- pontualidade por estado;
- evolução mensal.

## Cuidados de interpretação
Uma diferença entre notas não prova que o atraso foi a única causa da avaliação. Produto, preço, atendimento, expectativa e outros fatores também influenciam a satisfação. O projeto descreve associações, não causalidade.
