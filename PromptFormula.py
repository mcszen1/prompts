import streamlit as st

topico = st.text_input('Insira o Tópico do Prompt:')

tom = st.selectbox('Escolha o Tom:', ['Formal', 'Casual', 'Informativo', 'Persuasivo', 'Técnico'])
publico = st.selectbox('Escolha o Público:', ['Estudantes', 'Profissionais', 'Investidores', 'Público Geral'])
formato = st.selectbox('Escolha o Formato:', ['Esboço', 'Ensaio', 'Pontos Principais', 'Diálogo', 'Parágrafos'])
atuar_como = st.selectbox('Atuar como:', ['Especialista', 'Crítico', 'Entusiasta', 'Observador'])
objetivo = st.selectbox('Escolha o Objetivo:', ['Informar', 'Persuadir', 'Entreter', 'Educar', 'Inspirar'])

if st.button('Gerar Prompt'):
    prompt_gerado = f"{topico} - {tom}, {publico}, {formato}, {atuar_como}, {objetivo}"
    st.write('Prompt Gerado:', prompt_gerado)