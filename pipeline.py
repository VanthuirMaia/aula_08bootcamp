from etl import pipeline_caucular_kpi_de_vendas_consolidada

pasta_argumento: str = 'data'
formato_de_saida: list = ["parquet"] # Caso queira em Parquet, substituir apenas o argumento ["parquet"]

pipeline_caucular_kpi_de_vendas_consolidada(pasta_argumento, formato_de_saida)


