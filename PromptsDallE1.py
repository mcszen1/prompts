import streamlit as st
import pandas as pd
import re

# Função para carregar tipos de imagens de um arquivo CSV
def carregar_tipos_de_imagens(file_path):
    df = pd.read_csv(file_path)
    return df

# Função para gerar prompt com base no tipo selecionado
def gerar_prompt(tipo_imagem, prompt_text, variaveis):
    # Substituir variáveis na estrutura do prompt pelos inputs do usuário
    for variavel in variaveis:
        valor = st.text_input(f"Digite o valor para '{variavel}':")
        prompt_text = prompt_text.replace(f"[{variavel}]", valor)
    
    return prompt_text

# Interface do usuário com Streamlit
st.image("NIDLogo.jpg")
st.title("Ferramenta de Geração de Prompts para Imagens")

# Carregar tipos de imagens a partir de um arquivo CSV
file_path = st.file_uploader("Carregar arquivo CSV contendo tipos de imagens", type="csv")
if file_path is not None:
    df_tipos_imagens = carregar_tipos_de_imagens(file_path)

    # Selecionar o tipo de imagem
    tipo_selecionado = st.selectbox("Selecione o tipo de imagem:", df_tipos_imagens["CATEGORIA"])

    # Obter a estrutura do prompt para o tipo selecionado
    prompt_text = df_tipos_imagens[df_tipos_imagens["CATEGORY"] == tipo_selecionado]["PROMPT"].iloc[0]

    # Encontrar variáveis marcadas entre colchetes na estrutura do prompt
    variaveis = re.findall(r'\[(.*?)\]', prompt_text)

    # Gerar prompt e exibir para o usuário
    if st.button("Gerar Prompt"):
        prompt_gerado = gerar_prompt(tipo_selecionado, prompt_text, variaveis)
        st.write("Prompt Gerado:")
        st.code(prompt_gerado, language='plaintext')
