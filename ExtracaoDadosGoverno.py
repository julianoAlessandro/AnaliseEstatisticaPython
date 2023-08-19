import requests
import pandas as pd
import io
import urllib3

http = urllib3.PoolManager(maxsize=10)
urllib3.disable_warnings()

dfs = []
anos = range(2018,2024)

for ano in anos:
    print(f"\nDados de Exportação do ano de {ano}")

    url = f'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_{ano}_MUN.csv'
    arquivos = requests.get(url, verify=False)
    arquivos.encoding = 'utf-8'
    
    csvio = io.StringIO(arquivos.text, newline="")
    df = pd.read_csv(csvio, delimiter=';')
    dfs.append(df)
    print(df.head(3))

combined_df = pd.concat(dfs, ignore_index=True)

combined_df.to_csv('C:\\Users\\juliano\\Documents\\ExtracaoDados\\Exportacoes20182023.csv', index=False)

