# Iniciação Científica 👨‍🎓

## **Título do Projeto:** _Explorando Padrões do Comércio Exterior da região de Itapira: Uma análise Baseada em Dados._

### Área de Atuação: Ciência de Dados

**Ao longo do Projeto estarei exercendo as seguintes funções:**
- Arquiteto de Dados: Responsável por criar o design que será utilizado pelo Engenheiro de Dados
- Engenheiro de Dados: Coletar e armazenar os dados da Web
- Analista de Dados: Analisar, prever e evitar perdas usando os dados, com o intuito de auxiliar na tomada de decisão

**Disciplinas Relacionadas ao Projeto:**
- Técnicas de Programação
- Banco de Dados
- Estatística
- Banco de Dados não Relacional
- Mineração de Dados

**Objetivos:**
O objetivo deste projeto é realizar a extração, processamento, armazenamento, análise e visualização de Dados do comércio exterior da região de Itapira, com o intuito de identificar padrões, tendências e insights relevantes para auxiliar na compreensão e tomadas de decisões estratégicas no âmbito do comércio internacional. Especificamente, busca-se:
- Coletar e extrair dados relacionados às importações e exportações da região de Itapira, considerando produtos, países de origem, valores, volumes e outras variáveis relevantes;
- Realizar uma análise descritiva dos dados extraídos, identificando os principais fluxos comerciais, setores de destaque, sazonalidade e variações ao longo do tempo;
- Aplicar técnicas Estatísticas e de mineração de dados para identificar padrões, correlações e insights adicionais nos dados do comércio exterior;
- Desenvolver visualizações interativas e intuitivas dos dados extraídos, utilizando ferramentas adequadas, a fim de facilitar a compreensão e a exploração dos resultados.

# Etapas do Projeto 📆

## Mês: Agosto ⌛
**Atividades Previstas:**
- Definição do Problema de pesquisa
- Revisão da literatura sobre comércio exterior, análise de dados e visualização de informações.
- Identificação e acesso às fontes de dados relevantes do comércio exterior de Itapira.

## Mês: Setembro ⌛
**Atividades Previstas:**
- Estudo das ferramentas envolvidas no Projeto
- Coleta de dados do comércio Exterior.
- Limpeza e pré-processamento dos dados coletados.
- Análise Exploratória inicial dos dados, identificando padrões e características relevantes.

## Mês: Outubro ⌛
**Atividades Previstas:**
- Análise estatística dos dados.
- Desenvolvimento das visualizações iniciais dos dados do comércio exterior.
- Interpretação preliminar dos resultados obtidos.

## Mês: Novembro ⌛
**Atividades Previstas:**
- Refinamento das análises estatísticas e realização de análises mais profundas.
- Aperfeiçoamento das visualizações de dados, buscando maior clareza e impacto visual.
- Discussão dos resultados em relação às hipóteses ou objetivos propostos.

## Mês: Dezembro ⌛
**Atividades Previstas:**
- Análise final dos resultados, destacando insights e conclusões principais.
- Elaboração final do relatório do projeto, incluindo introdução, metodologia, resultados, discussão e conclusões.
- Revisão e formatação do relatório. Apresentação dos resultados e conclusões do projeto.

## Ferramentas Utilizadas 🔨

- Google Docs
- Vscode
- Power BI
- Azure Studio
- Pentaho
- GitHub
- Linguagem de Programação Python
- ChatGPT
- Google Acadêmico
- Google Colab
  # Etapa1: Extração e download dos arquivos no formato CSV

## Extração de Dados do site: _Estatísticas de Comércio Exterior em Dados Abertos_

[Link do site](https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta)

O objetivo primordial de um Engenharia de Dados é tornar os dados utilizáveis, através de um conjunto de técnicas para assim poder ser feita toda a análise de dados em cima para auxiliar na tomada de decisão. Logo, a extração de dados é a primeira etapa para todo Engenheiro. Em virtude disso, eu tive que utilizar as seguintes Bibliotecas para Extração:

- **request:** Utilizada para realizar a requisição ao site para dessa forma poder capturar e gravar os dados.
- **Pandas:** Utilizada para as consultas e leituras de dados de forma dinâmica.
- **io:** Utilizada para lidar com diversos tipos de entradas arquivos de texto, binário e dados brutos.
- **urllib3:** Essa biblioteca foi de fundamental utilidade no decorrer das atividades. Sempre que fazemos uma requisição ao servidor, algum tipo de erro pode acontecer no caminho impedindo assim nossa requisição. Nessa linha de pensamento, toda vez que eu fazia uma requisição ao servidor, eu era impedido de acessar o conteúdo por motivos de SSL, que tem o intuito de criptografar os dados e permitir segurança dos dados. Então, ele me impedia de pegar esses dados por segurança. No entanto, utilizando a referida biblioteca, eu pude ignorar essa chamada de atenção, conseguindo trazer os dados para o meu ambiente de desenvolvimento.

### Ilustração dos códigos:

![Imagem 1](https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/160762cf-2862-43ed-aab1-e5fc9366f620)

![Imagem 2](https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/e0490ea3-7dcb-434e-a23f-dc4406ec6d00)

# Etapa 2: Elaboração do Modelo Estrela ⭐

Após concluir a extração de todos os dados, surge a necessidade de armazená-los de maneira estruturada e segura. Isso é fundamental para possibilitar análises estatísticas posteriormente. Diante desse cenário, optou-se pela implementação do modelo de banco de dados estrela.

Esse modelo foi selecionado devido à sua capacidade de agilizar as consultas SQL. A abordagem se destaca ao utilizar uma tabela principal para centralizar todos os relacionamentos. Essa estrutura é especialmente vantajosa, uma vez que os demais relacionamentos não possuem conexões diretas entre si, mas sim apenas com a tabela de fatos.

Dessa forma, o uso do modelo estrela oferece maior eficiência na realização das análises estatísticas, ao mesmo tempo que garante a integridade e segurança dos dados armazenados.
<img src = "https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/2b49764c-07ba-4fed-9cf0-93f1fe45d16b">
