# Análise de Qualidade da Igreja
Este projeto utiliza Streamlit para criar uma aplicação interativa que analisa a qualidade de diferentes áreas da igreja com base em um arquivo CSV. A análise inclui a média das avaliações para diferentes categorias e a soma das notas para cada pergunta, apresentando essas informações de forma interativa e visual.

### Funcionalidades
1. Preparação dos Dados:
  
    * Leitura e processamento de um arquivo CSV.
    * Substituição de valores textuais por numéricos com base em categorias pré-definidas.
2. Análise dos Dados:
  
    * Cálculo da média das avaliações para várias categorias.
    * Cálculo da soma das notas para cada pergunta.
3. Visualização Interativa:

  * Geração de um gráfico de barras interativo que mostra a média das avaliações para cada categoria.
  * Exibição da soma das notas de cada pergunta, ordenada em ordem decrescente, com numeração.

### Requisitos
1. Python 3.x
2. Bibliotecas Python:
  * pandas
  * plotly
  * streamlit

### Faça o upload de um arquivo CSV para começar a análise.

### Estrutura do Projeto
1. app.py: Código principal da aplicação Streamlit.
2. requirements.txt: Lista de dependências do projeto (pode ser gerado com pip freeze > requirements.txt).
3. Exemplo de Arquivo CSV
 * O arquivo CSV deve estar formatado com as colunas representando perguntas e linhas representando respostas. As respostas devem ser substituídas pelos valores numéricos correspondentes de acordo com a seguinte tabela:

### Frequência:

  * 'Nunca' → 0
  * 'Raramente' → 1
  * 'Às vezes' → 2
  * 'Frequentemente' → 3
  * 'Sempre' → 4
### Concordância:

  * 'Discordo Totalmente' → 0
  * 'Discordo Parcialmente' → 1
  * 'Neutro' → 2
  * 'Concordo Parcialmente' → 3
  * 'Concordo Totalmente' → 4
