import streamlit as st
import pandas as pd
import plotly.express as px

# Função para preparar o CSV, substituindo valores conforme dicionários fornecidos
def preparar_csv(df):
    df = df.drop(df.columns[0], axis=1)  # Remove a primeira coluna que é o Timestamp

    substituicoes_frequencia = {'Nunca': 0, 'Raramente': 1, 'Às vezes': 2, 'Frequentemente': 3, 'Sempre': 4}
    substituicoes_acordo = {'Discordo Totalmente,': 0,'Discordo Totalmente': 0, 'Discordo Parcialmente': 1, 'Neutro': 2, 'Concordo Parcialmente': 3, 'Concordo Totalmente': 4}

    df = df.replace(substituicoes_frequencia)
    df = df.replace(substituicoes_acordo)
    
    return df

# Função para ler o arquivo CSV e processar os dados
def carregar_dados(arquivo):
    try:
        # Tenta ler o CSV com diferentes opções de delimitador e aspas
        df = pd.read_csv(arquivo, delimiter=',', quotechar='"', encoding='utf-8', engine='python')

        #st.write("CSV carregado com sucesso. Aqui estão as primeiras linhas do DataFrame:")

        # Prepara o DataFrame
        df = preparar_csv(df)
        
        #st.write("DataFrame após preparação:")
        #st.write(df.head())

        categorias = {
            "Liderança Capacitadora": [0, 1, 2],
            "Ministérios Orientados pelos Dons": [3, 4, 5],
            "Espiritualidade Contagiante": [6, 7, 8],
            "Estruturas Eficazes": [9, 10, 11],
            "Culto Inspirador": [12, 13, 14, 15, 16],
            "Grupos Pequenos": [17, 18, 19],
            "Evangelização Orientada para as Necessidades": [20, 21, 22],
            "Relacionamentos Marcados pelo Amor Fraternal": [23, 24, 25]
        }

        num_colunas = len(df.columns)
        num_indices_max = max([max(indices) for indices in categorias.values()])

        #st.write(f"Número de colunas no DataFrame: {num_colunas}")
        #st.write(f"Índices máximos necessários: {num_indices_max + 1}")

        if num_colunas < num_indices_max + 1:
            st.error("O arquivo CSV não tem colunas suficientes para processar todas as categorias.")
            return None, None

        medias = {categoria: df.iloc[:, indices].mean(axis=1).mean() for categoria, indices in categorias.items()}
        
        # Arredondar as médias para duas casas decimais
        medias = {categoria: round(media, 2) for categoria, media in medias.items()}

        #st.write("Médias calculadas:")
        #st.write(medias)

        # Calcular a soma das notas de cada coluna
        somas_colunas = df.sum().sort_values(ascending=False)

        #st.write("Somas das colunas:")
        #st.write(somas_colunas)

        return medias, somas_colunas
    
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo CSV: {str(e)}")  # Converte o erro para string
        return None, None

# Função para gerar um gráfico de barras interativo usando Plotly
def gerar_grafico_interativo(medias):
    categorias = list(medias.keys())
    valores = list(medias.values())

    fig = px.bar(
        x=categorias, 
        y=valores, 
        labels={'x':'Categorias', 'y':'Média'},
        title="Veja aqui seus pontos fortes e fracos:",
        text=valores
    )
    fig.update_layout(
        yaxis=dict(range=[0, 4]),
        xaxis_title="Categorias",
        yaxis_title="Média",
        width=800,  # Ajuste a largura conforme necessário
        height=500  # Ajuste a altura conforme necessário
    )
    fig.update_traces(marker_color='indigo', textposition='outside')

    st.plotly_chart(fig)

# Interface do Streamlit
st.title("Análise de Qualidade da Igreja")

uploaded_file = st.file_uploader("Escolha o arquivo CSV", type="csv")

if uploaded_file is not None:
    medias, somas_colunas = carregar_dados(uploaded_file)

    if medias:
        gerar_grafico_interativo(medias)
        
        st.markdown("###")
        st.markdown("---")

        # Exibir a marca com menor média
        marca_minima = min(medias, key=medias.get)
        st.write(f"### A marca com menor média é: {marca_minima} com média de {medias[marca_minima]:.2f}")

        # Exibir a marca com maior média
        marca_maxima = max(medias, key=medias.get)
        st.write(f"### A marca com maior média é: {marca_maxima} com média de {medias[marca_maxima]:.2f}")
        
        st.markdown("---")
        
        # Exibir a soma das notas de cada coluna em ordem decrescente com numeração
        st.write("### Soma das notas de cada pergunta (em ordem decrescente):")
        ordenado_por_soma = somas_colunas.sort_values(ascending=False)
        for i, (coluna, soma) in enumerate(ordenado_por_soma.items(), start=1):
            st.write(f"{i}. {coluna}: {soma:.2f}")
