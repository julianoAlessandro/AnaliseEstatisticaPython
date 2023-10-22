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
- SQL Server
- Pentaho
- GitHub
- ChatGPT
- Google Colab
- Docker
- Powerpoint
- WBS Chart Pro
- DBdiagram.io
- GanttProject

  ### Linguagem de Programação usada 👨‍💻
  - Python

  # Pipelines de Dados

A função primordial de um engenheiro de dados é construir pipelines eficientes para uma empresa. Neste contexto, entendemos que os pipelines são responsáveis por transportar dados de um local para outro, realizando os devidos tratamentos durante essa passagem. Portanto, as principais etapas que serão abordadas durante este projeto são as seguintes:

**Extração:**
- Nesta etapa, os dados brutos são coletados de várias fontes para serem armazenados na área de preparação.

**Transformação:**
- Esta fase é responsável por processar os dados brutos, de modo que eles adquiram valor e contribuam para a tomada de decisões.

**Carregamento:**
- Os dados processados são finalmente direcionados para o destino final, onde podem ser utilizados por um Analista de Dados.

<img src="https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/e7e4f090-140d-4f33-9854-4845cec6036d" >

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
<img src = "https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/1e3bdb6d-df2a-4854-9205-485e1e083cc6">

# Etapa 3: Transformação dos Dados 🔄

O processo de transformação é uma etapa fundamental para um engenheiro de dados. Tal etapa consiste em padronizar um conjunto de dados seguindo uma regra de negócio específica. No projeto apresentado, o tratamento dos arquivos CSV foi padronizado seguindo as regras envolvidas em um Banco de Dados Relacional. Nesse contexto, a ferramenta Pentaho foi de suma importância para algumas etapas de transformação dos dados, juntamente com o Banco de Dados SQL Server. Portanto, a união dessas duas ferramentas garante a consistência e integridade dos dados ao longo deste projeto.

## Pentaho

A incorporação do Pentaho desempenhou um papel essencial na otimização de certos processos de transformação que, de outra forma, exigiriam um extenso esforço manual no SQL Server. Assim, foi crucial estabelecer uma conexão efetiva entre essa ferramenta e o banco de dados alvo. Isso permitiu que, ao concluir a transformação, os dados fossem automaticamente integrados ao banco.

<img src = "https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/e18d72c8-5e0c-4c6f-b808-d7dab1d8c2ee" width="1000px">

## Transformações

No decorrer desta etapa, foram realizadas diversas transformações e limpezas nos dados, sendo as mais utilizadas:

1. Ordenamento dos valores presentes nos campos.
2. Remoção de valores duplicados.
3. Criação de uma chave primária (PK).
4. Mudança da tipagem dos dados.
5. Criação das chaves estrangeiras (FK).
6. Seleção das colunas desejadas.
7. Granularização dos campos Dim_Data.
8. Adição de colunas.
9. Alteração dos nomes das tabelas.

### Ordenamento dos valores presentes nos campos

Para conseguir remover os dados duplicados, antes de tudo, é necessário ordenar os valores presentes no campo.

### Remoção de valores duplicados e criação de chaves primárias

Como estamos normalizando os dados para o Padrão Relacional, torna-se necessário um campo do tipo PK em nossa base de dados. Para garantir que um campo seja considerado PK, o mesmo tem algumas restrições que devem ser seguidas para garantir a integridade dos relacionamentos. Uma dessas restrições é que a chave não tenha valor duplicado, portanto, foi necessário fazer a retirada de valores duplicados ao longo desta tabela. Em seguida, no SQL Server, alterar o tipo do campo para PK. A seguir, serão ilustrados tais processos:

<img src="https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/45069be9-30e3-4b3a-b54d-615991b1e096" width="1000px">
<img src="https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/44056fc9-788f-44eb-9438-e22ef7ed46a2" width="1000px">
<img src="https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/92c01813-0bec-46ec-8d8e-19a4e6c0c023" width="1000px">


### Mudança da tipagem dos dados e criação de chaves estrangeiras

Ao criar uma chave estrangeira para assegurar relacionamentos com tabelas de dimensões, é crucial que os dados sejam compatíveis a fim de garantir essa conexão. Em algumas situações, foi necessário ajustar a tipagem dos dados nas tabelas de dimensões para assegurar essa correspondência.

<img src = "https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/5568e5c6-0b43-411e-b9f9-9782b8e87aec" width = "1000px">

### Seleção das colunas desejadas

Para a criação da tabela Dim_Data, foi necessário selecionar algumas colunas desejadas, como "CO_ANO" e "CO_MES", de um arquivo CSV que possui mais de 7 campos. Logo, foi necessário excluir alguns campos e priorizar os dois campos mencionados utilizando a função `SELECT VALUES` do Pentaho. Dessa forma, o resultado foi obtido com sucesso.

<img src = "https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/099207db-3b25-4f07-bf4b-0f7e3f701898" width = "1000px">

### Granularização dos campos Dim_Data

O processo de granularização envolve o aumento do nível de detalhamento de uma tabela, expandindo o número de campos. Esse procedimento adquire extrema relevância em cenários de larga escala, onde auxilia as empresas na tomada de decisões fundamentais. Nesse contexto, os campos CO_ANO e CO_MES passaram por essa operação, conforme ilustrado na imagem abaixo:
 <img src= "https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/37a55bcd-0824-4dfb-9815-3fa5bbd10fb3" width="1000px">

### Adição de Coluna

Na construção da tabela fato, foi necessário utilizar um identificador desse campo, já que o mesmo não possuía um campo que realizava determinada ação antes de ser tratado. Com isso, o campo ID_EXPORTAÇÕES foi criado.

<img src="https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/56a34820-4ad3-4145-94b2-543182a08e49" width = "1000px">

### Alteração dos nomes das tabelas

Para seguir a padronização do modelo Estrela, que consiste em ter tabelas com o sufixo "Dim" e "Fato", foi necessário alterar o nome das tabelas extraídas do site do governo. Isso foi realizado pelo Pentaho, permitindo assim enviar tal alteração para o SQL SERVER.

# Etapa 4: Carregamento de Dados 💾

Para garantir a organização e o armazenamento eficiente dos dados, é imperativo que eles tenham um ambiente dedicado no SQL Server. Para atender a essa necessidade, é estabelecido um DataWarehouse, que funciona como um repositório centralizado capaz de armazenar e gerenciar os dados previamente existentes no SQL Server. Isso não apenas assegura a integridade dos dados, mas também fornece uma estrutura adequada para análises e consultas estratégicas.

<img src = "https://github.com/julianoAlessandro/AnaliseEstatisticaPython/assets/111141842/015d375a-71ff-4069-88d0-610cd7a83df5" width = "1000px">

