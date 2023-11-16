import streamlit as st

topico = st.text_input('Insira o Tópico do Prompt:')

tom = st.selectbox('Escolha o Tom:', ['Formal', 'Casual', 'Informativo', 'Persuasivo', 'Técnico'])
publico = st.selectbox('Escolha o Público:', ['Estudantes', 'Profissionais', 'Investidores', 'Público Geral'])
formato = st.selectbox('Escolha o Formato:', ['Esboço', 'Ensaio', 'Pontos Principais', 'Diálogo', 'Parágrafos'])
atuar_como = st.selectbox('Atuar como:', ['Especialista', 'Crítico', 'Entusiasta', 'Observador'])
objetivo = st.selectbox('Escolha o Objetivo:', ['Informar', 'Persuadir', 'Entreter', 'Educar', 'Inspirar'])

if st.button('Gerar Prompt'):
    prompt_gerado = f"Você é um {atuar_como} com grande conhecimento sobre {topico}. Quero que gere um texto do tipo {formato}, com tom {tom} e focado num público formado por {publico}. O principal objetivo do texto será {objetivo}."
    st.write('Prompt Gerado:', prompt_gerado)
