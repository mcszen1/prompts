import streamlit as st

def app_gerecao_imagem():
    st.title("Criação de Prompt para Geração de Imagem")

    # Campos do formulário
    descricao = st.text_area("1. Descrição do Conteúdo:", help="Descreva o que você deseja que apareça na imagem.")
    
    estilo_artistico = st.selectbox("2. Estilo Artístico:", ['Selecione', 'Realismo', 'Impressionismo', 'Surrealismo', 'Estilo de Van Gogh', 'Estilo de Picasso', 'Fotorealismo'], index=0)
    
    paleta_de_cores = st.selectbox("3. Paleta de Cores:", ['Selecione', 'Vibrante', 'Pastel', 'Monocromático', 'Cores Quentes', 'Cores Frias'], index=0)
    
    atmosfera = st.selectbox("4. Atmosfera e Emoção:", ['Selecione', 'Alegre', 'Sombria', 'Pacífica', 'Caótica', 'Misteriosa'], index=0)
    
    composicao = st.selectbox("5. Composição e Perspectiva:", ['Selecione', 'Close-up', 'Médio', 'Amplo'], index=0)
    
    meio = st.selectbox("6. Meio:", ['Selecione', 'Foto', 'Ilustração', 'Aquarela', '3D'], index=0)
    
    detalhes_especificos = st.text_area("7. Detalhes Específicos e Contexto:", help="Adicione detalhes específicos importantes para a imagem.")
    
    limitacoes = st.text_area("8. Limitações ou Exclusões:", help="Mencione o que você definitivamente não quer que apareça na imagem.")
    
    outras_preferencias = st.text_area("9. Outras Preferências (opcional):", help="Alguma outra preferência ou requisito para a imagem?")

    # Botão para gerar o prompt
    if st.button('Gerar Prompt'):
        prompt = f"Por favor, crie uma imagem que mostre {descricao}."
        if estilo_artistico != 'Selecione':
            prompt += f" Estilo artístico: {estilo_artistico}."
        if paleta_de_cores != 'Selecione':
            prompt += f" Cores: {paleta_de_cores}."
        if atmosfera != 'Selecione':
            prompt += f" Atmosfera/emocão: {atmosfera}."
        if composicao != 'Selecione':
            prompt += f" Composição/perspectiva: {composicao}."
        if meio != 'Selecione':
            prompt += f" Meio: {meio}."
        if detalhes_especificos:
            prompt += f" Detalhes específicos/contexto: {detalhes_especificos}."
        if limitacoes:
            prompt += f" Evitar: {limitacoes}."
        if outras_preferencias:
            prompt += f" Outras preferências: {outras_preferencias}."
        
        st.write("## Seu Prompt Final:")
        st.write(prompt)

# Executar o app
if __name__ == '__main__':
    app_gerecao_imagem()