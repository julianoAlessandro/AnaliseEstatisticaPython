import requests
import pandas as pd
import io
url = 'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM.csv'
arquivos = requests.get(url, verify=False)
csvio = io.StringIO(arquivos.text, newline="")
df = pd.read_csv(csvio, delimiter=';', encoding='utf-8-sig')
colunas_desejadas = ['CO_NCM','NO_NCM_POR']
df_filtrado = df[colunas_desejadas]
     
print(df_filtrado.head(2)) 
df_filtrado.to_csv('C:\\Users\\juliano\\Documents\\ExtracaoDados\\NCM.csv', index=False)


