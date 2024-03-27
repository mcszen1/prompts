import streamlit as st
import pandas as pd
import re

# Função para carregar tipos de imagens de um arquivo CSV
def carregar_tipos_de_imagens(file_path):
    df = pd.read_csv(file_path)
    return df

# Função ajustada para gerar prompt com base no tipo selecionado e valores das variáveis
def gerar_prompt(tipo_imagem, prompt_text, valores_variaveis):
    # Substituir variáveis na estrutura do prompt pelos valores fornecidos
    for variavel, valor in valores_variaveis.items():
        prompt_text = prompt_text.replace(f"[{variavel}]", valor)
    return prompt_text

# Interface do usuário com Streamlit
st.image("NIDLogo.jpg")
st.title("Ferramenta de Geração de Prompts para Imagens de Produtos")
st.write("Conheça o trabalho do NID nas áreas de Treinamento, Consultoria e Desenvolvimento")
st.write("Link - https://labcomdigital.wixsite.com/nucleodedados")
st.write("Conheça outras aplicações do NID em https://www.nidlab.com.br/")

# Carregar tipos de imagens a partir de um arquivo CSV
file_path = 'TarefasPrompt.csv'
if file_path is not None:
    df_tipos_imagens = carregar_tipos_de_imagens(file_path)

    # Selecionar o tipo de imagem
    tipo_selecionado = st.selectbox("Selecione o tipo de imagem:", df_tipos_imagens["CATEGORIA"])

    # Obter a estrutura do prompt para o tipo selecionado
    prompt_text = df_tipos_imagens[df_tipos_imagens["CATEGORIA"] == tipo_selecionado]["TAREFA"].iloc[0]

    # Encontrar variáveis marcadas entre colchetes na estrutura do prompt
    variaveis = re.findall(r'\[(.*?)\]', prompt_text)

    # Criando um dicionário para armazenar os valores das variáveis
    valores_variaveis = {}

    # Coletar os valores das variáveis antes de gerar o prompt
    for variavel in variaveis:
        valores_variaveis[variavel] = st.text_input(f"Digite o valor para '{variavel}':", key=variavel)

    # Gerar prompt e exibir para o usuário
    if st.button("Gerar Prompt"):
        prompt_gerado = gerar_prompt(tipo_selecionado, prompt_text, valores_variaveis)
        st.write("Prompt Gerado:")
        st.code(prompt_gerado, language='plaintext')
