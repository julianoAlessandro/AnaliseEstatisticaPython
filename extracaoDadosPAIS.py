import requests
import pandas as pd
import io

url = 'https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv'
arquivos = requests.get(url, verify=False)
csvio = io.StringIO(arquivos.text, newline="")
df = pd.read_csv(csvio, delimiter=';', encoding = 'utf-8-sig')
colunas_desejadas = ['CO_PAIS','NO_PAIS']
coluna_filtrada = df[colunas_desejadas]
print(coluna_filtrada.head(8)) 
df.to_csv('C:\\Users\\juliano\\Documents\\ExtracaoDados\\PAIS.csv', index=False)



