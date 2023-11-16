import streamlit as st

st.image('labcom_logo_preto.jpg')
st.title("ASSISTENTE DE PROMPT DESIGN")
st.write('Informe sobre o que quer escrever e especifique como vai usar')
st.write('Com as suas escolhas o PROMPT será mais efetivo e os resultados melhores. ')
topico = st.text_input('Insira o TEMA para a geração do texto:')
st.write('Agora escolha faça as escolhas para o tipo de utilização que quer fazer ')
tom = st.selectbox('Escolha o Tom:', ['Formal', 'Casual', 'Informativo', 'Persuasivo', 'Técnico'])
publico = st.selectbox('Escolha o Público:', ['Estudantes', 'Profissionais', 'Investidores', 'Público Geral'])
formato = st.selectbox('Escolha o Formato:', ['Esboço', 'Ensaio', 'Pontos Principais', 'Diálogo', 'Parágrafos'])
atuar_como = st.selectbox('Atuar como:', ['Especialista', 'Crítico', 'Entusiasta', 'Observador'])
objetivo = st.selectbox('Escolha o Objetivo:', ['Informar', 'Persuadir', 'Entreter', 'Educar', 'Inspirar'])

if st.button('Gerar Prompt'):
    prompt_gerado = f"Você é um {atuar_como} com grande conhecimento sobre {topico}. Quero que gere um texto do tipo {formato}, com tom {tom} e focado num público formado por {publico}. O principal objetivo do texto será {objetivo}."
    st.write('Prompt Gerado:')
    st.write(prompt_gerado)
    st.write("Copie e cole esse prompt no CHATGPT ou em qualquer outra ferramenta de IA")
