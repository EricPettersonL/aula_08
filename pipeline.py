# vai chamar as minhas funções e executar o pipeline
from etl import lendo_arquivos, criando_coluna_total, exportando_arquivo


pasta: str = "data"
tipo_arquivo: list = ["csv", "parquet"]
df_final = lendo_arquivos(pasta)
df_total = criando_coluna_total(df_final)
exportando_arquivo(df_total, tipo_arquivo )
