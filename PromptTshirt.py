import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from openai import OpenAI
client = OpenAI()

def gen_image (prompt): 
	response=client.images.generate(model="dall-e-3",prompt=prompt1, n=1, size="1024x1792")
	response_json = response.json()
	#image_url = response_json['data'][0]['url']
	#image_url = response['data'][0]['url']
	image_url = response.data[0].url
	camiseta= requests.get(image_url)
	img = Image.open(BytesIO(camiseta.content))

	st.image(img, caption="Imagem Gerada", use_column_width=True)
	
def download_image(image, filename="image.png"):
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

st.image('labcom_logo_preto.jpg')
st.title("T-SHIRT DESIGN - Crie sua camisa com IA")
# Títulos e Introdução
detalhe=""
st.subheader("Defina os elementos principais da sua camisa:")

# Entrada do usuário para descrição do objeto e ambiente
objeto = st.text_input("Descreva o elemento principal da camisa. Ex : um dragão")

color=st.radio(
    "Escolha a cor da sua camisa. O algoritmo pode inserir variações neste elemento. Recomendamos usar branco ou preto",
    ["White", "Black", "Red", "Blue"],
    captions = ["Branca", "Preta", "Vermelha", "Azul"])

letras = st.checkbox('Inserir letras. Digite uma palavra simples para inserir na imagem da camisa. ATENÇÃO : a geração de textos ainda não é precisa.')

if letras:
    palavra = st.text_input("Digite uma palavra simples:")		
else:
    palavra = ""
# Seleção de Estilo da Camisa.

medium = st.selectbox("Escolha o Estilo:", ["Geométrico","Pop Art","Botânico","Mítico","Pixel Art", "Origami","Festivo","Mangá","Magia","Wired","Fractal","Renascentista","Zodíaco","Escultura","Mecânico","Tecido","Watercolor","Etéreo","Rock Style","Kawaii Style", "Expressionismo Abstrato","Grafite" ])

# Opções de Estilo

if medium == "Geométrico": detalhe="a geometric"
if medium == "Pop Art" : detalhe=" a pop art portrait of a "
if medium == "Botânico" : detalhe=" a bold botanical illustration of a "
if medium == "Mítico" : 
	origem=st.selectbox("Escolha a mitologia:",["Chinese", "Greek", "Nordic", "Indigenous"])
	detalhe=f" a legendary creature from a {origem} mitology of a "
if medium == "Pixel Art" : detalhe="a pixel art representation of"
if medium == "Origami" : detalhe="a inspired by origami art"
if medium == "Festivo" : 
	festa=st.selectbox("Escolha uma data festiva:", ["New Year", "Christmas","Carnaval"])
	detalhe=f"a celebration of the festive occasion of {festa} with fireworks"
if medium == "Mangá" : detalhe = "in a manga art style of a "
if medium == "Magia" : detalhe = " an illustration inspired by the fairtale of"
if medium == "Wired" : detalhe = " an illustration constructed from a interwined wires of a "
if medium == "Fractal" : detalhe = f"a fractal pattern centered around a " 
if medium == "Renascentista" : detalhe = " an illustration in a Renaissance art style of a "
signos_zodiaco_dict = {
    "Áries": "Aries",
    "Touro": "Taurus",
    "Gêmeos": "Gemini",
    "Câncer": "Cancer",
    "Leão": "Leo",
    "Virgem": "Virgo",
    "Libra": "Libra",
    "Escorpião": "Scorpio",
    "Sagitário": "Sagittarius",
    "Capricórnio": "Capricorn",
    "Aquário": "Aquarius",
    "Peixes": "Pisces"
}
if medium == "Zodíaco" : 
	signzod= st.selectbox("Qual signo quer representar ?",(
    "Áries",
    "Touro",
    "Gêmeos",
    "Câncer",
    "Leão",
    "Virgem",
    "Libra",
    "Escorpião",
    "Sagitário",
    "Capricórnio",
    "Aquário",
    "Peixes"), index=None, placeholder="Escolha o seu signo",)
	way= st.selectbox("Como quer o representação do signo",(
    "a zen art",
    "a modern art",
    "a tech",
    "a  watercolor art",
    "a 3d model",
    "a pixel art",
    "an art nouveaux with floral elements",
    "a futuristic",
    "a medieval",
    "a cyberpunk",
    "a surrealist",
    "a magic"), index=None, placeholder="Escolha a sua inspiração",)
	if signzod:
		sign_en = signos_zodiaco_dict[signzod]
		detalhe = f"{way} style representation of the zodiac sign of {sign_en}"

if medium == "Escultura" : detalhe = " sketch resembling a 3d sculpture of "
if medium == "Mecânico" : detalhe = "a mechanical version of "
if medium == "Tecido" : detalhe = " a whimsical weavings in the pattern of a "
if medium == "Watercolor" : detalhe = "a watercolor illustration of"
if medium == "Etéreo" : detalhe = "rendered with a soft watercolor texture"
if medium == "Rock Style" : detalhe = " in a dynamic rockstar pose with eletric waves and splashes of color emanating form the instrument"
if medium == "Kawaii Style" : detalhe = " with a pastel colored kawaii style"
if medium == "Expressionismo Abstrato" : detalhe = "in a vibrant and abstract representation of"
if medium == "Grafite" : detalhe = f"the minimalist word {letras} styled in bold graffiti font, radiating with neon hues"


# Formata o prompt final

if palavra !="":
	prompt1=f"Wide vector designs of a {objeto}, printed on a {color} t-shirt showcasing a {detalhe} {objeto} with a text {palavra}. Show the image always using a frontal  view, with 0 (zero) rotation."
else:
	prompt1=f"Wide vector designs of a {objeto}, printed on a {color} t-shirt showcasing {detalhe} {objeto}. Show the image always using a frontal  view, with 0 (zero) rotation."

# Exibir o prompt
st.write("Prompt Gerado:")
st.write(prompt1)

if st.button("Gerar imagem"):
    if prompt1:
	    with st.spinner('Gerando imagem...'):
		    generated_image = gen_image(prompt1)
		    st.write(generated_image)
		    buffer = download_image(img)
		    st.download_button(label="Baixar imagem",
                               data=buffer,
                               file_name="dalle_generated_image.png",
                               mime="image/png")
        else:
            st.error("Falha ao gerar a imagem. Por favor, tente novamente.")
    else:
        st.warning("Por favor, insira um prompt antes de gerar a imagem.")
