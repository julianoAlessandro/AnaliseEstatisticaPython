import requests
import pandas as pd
import io

url = 'https://balanca.economia.gov.br/balanca/bd/tabelas/VIA.csv'
arquivos = requests.get(url, verify=False)
arquivos.encoding = 'utf-8'
csvio = io.StringIO(arquivos.text, newline="")
df = pd.read_csv(csvio, delimiter=';')
print(df.head(11)) 
df.to_csv('C:\\Users\\juliano\\Documents\\ExtracaoDados\\VIA3.csv', index=False)

