# Aula 08 Funções

Nessa aula foi realizada uma ETL, com o uso de biblioteca Pandas para processar dados de arquivos JSON e exportá-los para diferentes formatos de arquivo. Vamos explicar as diferentes partes do código:

## Importações de Bibliotecas:
```python
import pandas as pd
import os
import glob


```


import pandas as pd: Importa a biblioteca Pandas com o alias pd, que é comumente usado para abreviar o nome da biblioteca.
import os: Importa o módulo os, que fornece funcionalidades para interagir com o sistema operacional.
import glob: Importa o módulo glob, que é usado para encontrar todos os caminhos de arquivo correspondentes a um padrão especificado.
## Função lendo_arquivos:
```python
# ler o arquivo e concatenar em um só dataframe

def lendo_arquivos(path: str)-> pd.DataFrame:
    '''
    Função para ler os arquivos json e concatenar em um dataframe
    
    Parameters Pasta data
    
    '''
    json_files = glob.glob(os.path.join(path, "*.json"))

    df = pd.concat((pd.read_json(f) for f in json_files), ignore_index=True)

    return df


```

Esta função recebe um argumento path, que é o caminho para a pasta contendo os arquivos JSON.
glob.glob(os.path.join(path, "*.json")): Utiliza a função glob.glob() para encontrar todos os arquivos com extensão .json na pasta especificada pelo path.
pd.concat((pd.read_json(f) for f in json_files), ignore_index=True): Lê cada arquivo JSON encontrado e concatena os DataFrames resultantes em um único DataFrame, ignorando os índices originais.
## Função criando_coluna_total:
```python
# Criar uma coluna total com a multiplicação das colunas quantidade e venda

def criando_coluna_total(df: pd.DataFrame)-> pd.DataFrame:
    '''
    Função para criar uma coluna total com a multiplicação das colunas quantidade e venda
    
    Parameters DataFrame
    
    '''
    df["Total"] = df["Quantidade"] * df["Venda"]

    return df


```

Esta função recebe um DataFrame como entrada.
df["Total"] = df["Quantidade"] * df["Venda"]: Cria uma nova coluna chamada "Total", que contém o resultado da multiplicação das colunas "Quantidade" e "Venda".
## Função exportando_arquivo:
```python
# Exportar o dataframe para um arquivo csv ou parquet, a pessoa que decide
def exportando_arquivo(df: pd.DataFrame, tipo_arquivo: list):
    '''
    Função para exportar o dataframe para um arquivo csv ou parquet
    
    Parameters DataFrame, tipo_arquivo
    
    '''
    for i in tipo_arquivo:
        if i == "csv":
            df.to_csv("loading.csv", index=False)
        elif i == "parquet":
            df.to_parquet("loading.parquet", index=False)


```

Esta função recebe dois argumentos: um DataFrame e uma lista de tipos de arquivo.
Percorre a lista de tipos de arquivo e exporta o DataFrame para cada tipo especificado.
Se o tipo de arquivo for "csv", o DataFrame é exportado para um arquivo CSV chamado "loading.csv" usando o método to_csv() do Pandas.
Se o tipo de arquivo for "parquet", o DataFrame é exportado para um arquivo Parquet chamado "loading.parquet" usando o método to_parquet() do Pandas.

## Para rodar o arquivo

Para rodar esse arquivo foi criado o pipeline.py que chama essas minhas funções

```python

# vai chamar as minhas funções e executar o pipeline
from etl import lendo_arquivos, criando_coluna_total, exportando_arquivo


pasta: str = "data"
tipo_arquivo: list = ["csv", "parquet"]
df_final = lendo_arquivos(pasta)
df_total = criando_coluna_total(df_final)
exportando_arquivo(df_total, tipo_arquivo )

```


No geral, este script fornece funcionalidades para ler arquivos JSON de uma pasta, processar os dados e exportá-los para formatos de arquivo como CSV ou Parquet.
