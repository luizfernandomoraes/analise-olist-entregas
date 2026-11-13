# Relatório de Insights — Análise de Entregas Olist

## 1. Objetivo da análise

O objetivo deste projeto é analisar os atrasos nas entregas do
e-commerce brasileiro Olist e investigar como o prazo de entrega
está relacionado à satisfação dos consumidores.

A análise utiliza dados históricos de pedidos realizados entre
2016 e 2018.

## 2. Resultados gerais

Foram analisados 96.470 pedidos entregues.

| Indicador | Resultado |
|---|---:|
| Pedidos entregues analisados | 96.470 |
| Entregas realizadas no prazo | 91,89% |
| Entregas atrasadas | 8,11% |
| Atraso médio entre pedidos atrasados | 9,55 dias |
| Nota média geral dos clientes | 4,16 |

## 3. Principais descobertas

### 3.1 Pontualidade das entregas

A maior parte dos pedidos analisados foi entregue dentro do prazo
estimado, representando 91,89% do total.

Entretanto, 8,11% dos pedidos foram entregues com atraso.
Esse percentual demonstra que ainda existem oportunidades de
melhoria na operação logística.

### 3.2 Impacto dos atrasos

Entre os pedidos atrasados, o atraso médio foi de 9,55 dias.

Esse resultado indica que os atrasos podem representar uma
experiência negativa para os consumidores, especialmente quando
o prazo prometido não é cumprido.

### 3.3 Satisfação dos consumidores

A nota média geral das avaliações foi de 4,16 pontos.

A relação entre o prazo de entrega e as avaliações dos clientes
foi investigada no dashboard, permitindo comparar pedidos
entregues no prazo e pedidos atrasados.

Não se deve interpretar essa relação como prova de causalidade,
pois outros fatores também podem influenciar a satisfação.

### 3.4 Análise geográfica e temporal

O dashboard permite observar a distribuição dos pedidos e dos
atrasos por estado, além da evolução mensal dos pedidos e dos
atrasos médios.

Essas visualizações ajudam a identificar diferenças regionais
e variações ao longo do período analisado.

## 4. Recomendações

Com base nos resultados, recomenda-se:

1. Monitorar os pedidos com maior risco de atraso.
2. Investigar as regiões com maior concentração de entregas atrasadas.
3. Acompanhar o desempenho das transportadoras e dos prazos estimados.
4. Melhorar a comunicação com os consumidores quando houver atrasos.
5. Monitorar as avaliações dos clientes para identificar oportunidades
   de melhoria na experiência de compra.

## 5. Limitações da análise

Os dados utilizados são históricos e abrangem o período de 2016 a 2018.
Portanto, os resultados não representam necessariamente a situação
atual do comércio eletrônico brasileiro.

A análise identifica associações e padrões, mas não comprova que
os atrasos sejam a única causa de avaliações negativas.

## 6. Conclusão

A análise demonstra que 91,89% dos pedidos entregues foram recebidos
dentro do prazo, enquanto 8,11% apresentaram atraso.

O atraso médio entre os pedidos atrasados foi de 9,55 dias,
e a nota média geral dos consumidores foi de 4,16.

Os resultados reforçam a importância do acompanhamento dos prazos
logísticos e da satisfação dos consumidores.

A utilização de Python, Pandas, SQL e Looker Studio permitiu
organizar, analisar e apresentar os dados de forma visual,
facilitando a identificação de padrões e oportunidades de melhoria.