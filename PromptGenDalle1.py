import streamlit as st

# Títulos e Introdução
st.title("Assistente de Criação de Prompts para DALL-E 3")
st.subheader("Defina as características da sua imagem")

# Entrada do usuário para descrição do objeto e ambiente
objeto = st.text_input("Descreva o objeto para a imagem:")
ambiente = st.text_input("Descreva o ambiente onde o objeto estará:")

# Seleção de Aspect Ratio, Medium, etc.
aspect_ratio = st.selectbox("Escolha o Aspect Ratio:", ["Square", "Wide", "Tall"])
medium = st.selectbox("Escolha o Medium:", ["photo", "watercolor", "illustration", "3D model", "pixel art"])
# Adicione aqui as outras categorias e opções...

# Opções de Scene
viewpoint = st.selectbox("Escolha o Viewpoint:", ["bird's-eye", "ground", "close-up", "side view", "diagonal angle"])
main_setting = st.selectbox("Escolha o Main Setting:", ["beach", "forest", "city", "mountains", "space", "underwater"])
timing = st.selectbox("Escolha o Timing:", ["time of day", "season", "era", "future", "past"])
atmosphere = st.selectbox("Escolha o Atmosphere:", ["serene", "bustling", "mysterious", "chaotic", "peaceful"])
weather = st.selectbox("Escolha o Weather:", ["sunny", "windy", "calm seas", "stormy", "snowy", "foggy"])
depth_details = st.selectbox("Escolha o Depth Details:", ["foreground to background", "layered", "flat", "dynamic depth"])
lighting = st.selectbox("Escolha o Lighting:", ["soft", "backlit", "golden hour", "overcast", "glowing", "tenebrism", "harsh shadows"])
movement = st.selectbox("Escolha o Movement:", ["static", "dynamic", "fast-paced", "slow motion"])
cultural_touches = st.selectbox("Escolha o Cultural Touches:", ["stalls", "festivals", "attire", "architecture", "local customs"])
# Opções de Style
artistic_era = st.selectbox("Escolha a Artistic Era:", ["impressionism", "Van Gogh style", "renaissance", "surrealism", "modernism", "baroque"])
color_palette = st.selectbox("Escolha a Color Palette:", ["vivid", "pastel", "monochrome", "warm tones", "cool tones", "neon"])
detail_level = st.selectbox("Escolha o Detail Level:", ["minimalist", "rough", "refined", "hyper-realistic", "abstract", "stylized"])
themes = st.selectbox("Escolha Themes:", ["Art Nouveau with floral motifs", "futuristic", "medieval", "steampunk", "cyberpunk", "nature-inspired"])
brushwork = st.selectbox("Escolha o Brushwork:", ["strokes", "stippling", "hatching", "blending", "dry brush", "splattering"])


# Concatenar as escolhas para formar o prompt
prompt = f"{aspect_ratio} {medium}: {objeto} in {ambiente}, {viewpoint}, {main_setting}, {timing}, {atmosphere}, {weather}, {depth_details}, {lighting}, {movement}, {cultural_touches}"
# Adicione aqui a concatenação das outras categorias...

# Exibir o prompt
st.write("Prompt Gerado:")
st.write(prompt)

# Rodar o aplicativo
# Para rodar, salve este script como app.py e execute 'streamlit run app.py' no terminal
