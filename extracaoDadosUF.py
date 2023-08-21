import requests
import pandas as pd
import io

url = 'https://balanca.economia.gov.br/balanca/bd/tabelas/UF.csv'
arquivos = requests.get(url, verify=False)
arquivos.encoding = 'utf-8'
csvio = io.StringIO(arquivos.text, newline="")
df = pd.read_csv(csvio, delimiter=';')
colunas_desejadas = ['CO_UF','NO_UF','NO_REGIAO']
df_filtrado = df[colunas_desejadas]
print(df_filtrado.head(2)) 
df_filtrado.to_csv('C:\\Users\\juliano\\Documents\\ExtracaoDados\\Estado.csv', index=False)




