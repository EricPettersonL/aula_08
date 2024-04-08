import pandas as pd
import os
import glob

# ler o arquivo e concatenar em um só dataframe

def lendo_arquivos(path: str)-> pd.DataFrame:
    '''
    Função para ler os arquivos json e concatenar em um dataframe
    
    Parameters Pasta data
    
    '''
    json_files = glob.glob(os.path.join(path, "*.json"))

    df = pd.concat((pd.read_json(f) for f in json_files), ignore_index=True)

    return df


# Criar uma coluna total com a multiplicação das colunas quantidade e venda

def criando_coluna_total(df: pd.DataFrame)-> pd.DataFrame:
    '''
    Função para criar uma coluna total com a multiplicação das colunas quantidade e venda
    
    Parameters DataFrame
    
    '''
    df["Total"] = df["Quantidade"] * df["Venda"]

    return df

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
   


    
    