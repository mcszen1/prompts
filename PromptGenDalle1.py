import streamlit as st

st.image('labcom_logo_preto.jpg')
st.title("ASSISTENTE DE PROMPT DESIGN PARA IMAGENS")
# Títulos e Introdução

st.subheader("Defina as características da sua imagem")

# Entrada do usuário para descrição do objeto e ambiente
objeto = st.text_input("Descreva o objeto para a imagem:")
ambiente = st.text_input("Descreva o ambiente onde o objeto estará:")

# Seleção de Aspect Ratio, Medium, etc.
aspect_ratio = st.selectbox("Escolha o Aspect Ratio:", ["Quadrado", "16:9", "9:16"])
medium = st.selectbox("Escolha o Medium:", ["photo", "watercolor", "illustration", "3D model", "pixel art"])

# Opções de Scene
viewpoint = st.selectbox("Escolha o Ponto de Vista:", ["Visão em Primeira Pessoa", "Vista aérea", "Vista de Baixo", "Vista do Solo", "Close-up", "Vista Frontal", "Vista Lateral", "Vista de Trás", "Visão Panorâmica", "Portal View", "Cross-Section View","Satellite View", "Lente Olho de Peixe","Visão Isométrica", "Ângulo Diagonal", "Nenhum"])
main_setting = st.selectbox("Escolha o Ambiente Principal:", ["Praia", "Floresta", "Cidade", "Montanhas", "Espaço", "Subaquático", "Nenhum"])
timing = st.selectbox("Escolha o Tempo:", ["Manhã", "Tarde", "Noite", "Futuro", "Passado", "Nenhum"])
atmosphere = st.selectbox("Escolha a Atmosfera:", ["Sereno", "Movimentado", "Misterioso", "Caótico", "Pacífico", "Nenhum"])
weather = st.selectbox("Escolha o Clima:", ["Ensolarado", "Ventoso", "Mares Calmos", "Tempestuoso", "Nevoso", "Nebuloso", "Nenhum"])
depth_details = st.selectbox("Escolha os Detalhes de Profundidade:", ["Do primeiro plano ao fundo", "Em camadas", "Plano", "Profundidade dinâmica", "Nenhum"])
lighting = st.selectbox("Escolha a Iluminação:", ["Suave", "Contraluz", "Hora Dourada", "Nublado", "Brilhante", "Tenebrismo", "Sombras Duras", "Nenhum"])
movement = st.selectbox("Escolha o Movimento:", ["Estático", "Dinâmico", "Rápido", "Câmera Lenta", "Nenhum"])
# Opções de Estilo
artistic_era = st.selectbox("Escolha a Era Artística:", ["Impressionismo", "Estilo Van Gogh", "Renascimento", "Surrealismo", "Modernismo", "Barroco", "Nenhum"])
color_palette = st.selectbox("Escolha a Paleta de Cores:", ["Vívida", "Pastel", "Monocromático", "Tons Quentes", "Tons Frios", "Neon", "Nenhum"])
detail_level = st.selectbox("Escolha o Nível de Detalhe:", ["Minimalista", "Rústico", "Refinado", "Hiper-realista", "Abstrato", "Estilizado", "Nenhum"])
themes = st.selectbox("Escolha Temas:", ["Art Nouveau com motivos florais", "Futurista", "Medieval", "Steampunk", "Cyberpunk", "Inspirado na Natureza", "Nenhum"])
brushwork = st.selectbox("Escolha o Tipo de Pincelada:", ["Pinceladas", "Pontilhismo", "Hachura", "Esfumado", "Pincel Seco", "Respingos", "Nenhum"])



# Lista para armazenar características escolhidas
caracteristicas = []

# Adiciona características à lista se não forem "None"
if viewpoint != "Nenhum": caracteristicas.append(viewpoint)
if main_setting != "Nenhum": caracteristicas.append(main_setting)
if timing != "Nenhum": caracteristicas.append(timing)
if atmosphere != "Nenhum": caracteristicas.append(atmosphere)
if weather != "Nenhum": caracteristicas.append(weather)
if depth_details != "Nenhum": caracteristicas.append(depth_details)
if lighting != "Nenhum": caracteristicas.append(lighting)
if movement != "Nenhum": caracteristicas.append(movement)
if artistic_era != "Nenhum": caracteristicas.append(artistic_era)
if color_palette != "Nenhum": caracteristicas.append(color_palette)
if detail_level != "Nenhum": caracteristicas.append(detail_level)
if themes != "Nenhum": caracteristicas.append(themes)
if brushwork != "Nenhum": caracteristicas.append(brushwork)

# Concatena as características escolhidas
caracteristicas_str = ", ".join(caracteristicas)

# Formata o prompt final
prompt = f"Gere uma imagem com quatro opções e as seguintes características: {medium} de {objeto} num ambiente descrito como {ambiente}, {caracteristicas_str}"

# Exibir o prompt
st.write("Prompt Gerado:")
st.write(prompt)

# Rodar o aplicativo
# Para rodar, salve este script como app.py e execute 'streamlit run app.py' no terminal
