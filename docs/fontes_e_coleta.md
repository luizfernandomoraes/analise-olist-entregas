# 2. Fontes de dados e método de coleta

## Fonte principal
**Brazilian E-Commerce Public Dataset by Olist**, publicado no Kaggle:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

A descrição do publicador informa aproximadamente 100 mil pedidos realizados entre 2016 e 2018, com tabelas relacionadas a pedidos, clientes, itens, pagamentos, avaliações, produtos, vendedores e geolocalização. Os dados comerciais foram anonimizados.

## Arquivos utilizados
| Arquivo | Conteúdo | Tipo | Uso |
|---|---|---|---|
| `olist_orders_dataset.csv` | status e datas do pedido | Estruturado | datas de compra, entrega real e prevista |
| `olist_order_reviews_dataset.csv` | nota e comentários | Estruturado + texto | satisfação do consumidor |
| `olist_customers_dataset.csv` | identificador e localização | Estruturado | estado do cliente |
| `olist_order_items_dataset.csv` | itens, vendedores, preço e frete | Estruturado | contexto comercial opcional |

## Acesso e coleta
1. Acessar o endereço Kaggle acima.
2. Entrar na conta Kaggle, se solicitado.
3. Baixar o arquivo ZIP do dataset.
4. Extrair os CSVs para a pasta `data/raw/` deste projeto.
5. Não alterar os arquivos originais; a limpeza ocorre no script.

**Método:** download direto (CSV compactado em ZIP). Não é necessário scraping nem API para esta versão.

## Relacionamentos
- Pedidos ↔ clientes: `customer_id`.
- Pedidos ↔ avaliações: `order_id`.
- Pedidos ↔ itens: `order_id`.

## Licença e cuidados
A página do dataset informa licença CC BY-NC-SA 4.0. Verifique os termos vigentes na página antes de redistribuir os dados. O repositório deste projeto não deve incluir os CSVs brutos; inclua apenas instruções e resultados agregados. Não tente reidentificar pessoas.
