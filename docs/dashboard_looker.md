# 5. Dashboard no Looker Studio

## Arquivos para importar
Após executar o script, use os CSVs em `data/processed/`:
- `kpis_gerais.csv`
- `avaliacoes_prazo.csv`
- `por_estado.csv`
- `por_mes.csv`

## Layout sugerido — página 1: Visão geral
**Título:** Entregas e satisfação no e-commerce brasileiro  
Cartões:
- Pedidos analisados
- Entrega no prazo (%)
- Atraso médio (dias)
- Nota média

Gráficos:
- Barras: nota média por faixa de prazo (no prazo/atrasado).
- Série temporal: percentual de entrega no prazo por mês.
- Tabela: indicadores gerais.

## Página 2: Visão regional e temporal
- Barras horizontais: percentual de atraso por estado (filtrar estados com pelo menos 100 pedidos).
- Série temporal: pedidos analisados e pontualidade por mês.
- Tabela: estado, pedidos, percentual no prazo, atraso médio e nota média.

## Design e narrativa
1. Comece com a dimensão do problema (quantos pedidos foram analisados).
2. Mostre a pontualidade.
3. Conecte prazo e satisfação.
4. Termine com regiões/períodos que merecem investigação.

Use cores discretas: azul para visão geral, verde para no prazo e laranja para atraso. Evite gráficos 3D e excesso de cores.

## Publicação
Compartilhe o relatório com permissão de visualização e coloque o link em `dashboard/link_dashboard.txt`.
