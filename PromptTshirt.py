import streamlit as st

st.image('labcom_logo_preto.jpg')
st.title("T-SHIRT DESIGN - Crie sua camisa com IA")
# Títulos e Introdução

st.subheader("Defina os elementos principais da sua camisa:")

# Entrada do usuário para descrição do objeto e ambiente
objeto = st.text_input("Descreva o elemento principal da camisa. Ex : um dragão")

color=st.text_input("Escolha a cor da camisa. Use apenas uma cor básica. Ex: Branca, Preta, Azul, Vermelha")

letras = st.checkbox('Inserir letras.Se quiser, digite uma palavra simples para inserir na imagem da camisa, lembrando que a geração de textos ainda não é precisa.')

if letras:
    palavra = st.text_input("Digite uma palavra simples:")		

# Seleção de Estilo da Camisa.

medium = st.selectbox("Escolha o Estilo:", ["Geométrico","Pop Art","Botânico","Mítico","Pixel Art", "Origami","Festivo","Mangá","Magia","Wired","Fractal","Renascentista","Zodíaco","Escultura","Mecânico","Tecido","Watercolor","Etéreo","Rock Style","Kawaii Style", "Expressionismo Abstrato","Grafite" ])

# Formata o prompt final

prompt=f"Wide vector designs printed on a {color} t-shirt showcasing a {detalhe} {object}"
if palavra:
	prompt1=f"Wide vector designs printed on a {color} t-shirt showcasing a {detalhe} {object} with a text {letras}"

# Opções de Estilo
detalhe=""
if medium == "Geométrico": detalhe="geometric"
if medium == "Pop Art" : detalhe="a pop art portrait of a "
if medium == "Botânico" : detalhe="a bold botanical illustration of a "
if medium == "Mítico" : 
	origem=st.selectbox("Escolha a mitologia:",["Chinese", "Greek", "Nordic", "Indigenous"])
	detalhe=f"a legendary creature from a {origem} mitology"
if medium == "Pixel Art" : detalhe="a pixel art representation of"
if medium == "Origami" : detalhe="inspired by origami art"
if medium == "Festivo" : 
	festa=st.selectbox("Escolha uma data festiva:", ["New Year", "Christmas","Carnaval"])
	detalhe=f"celebrating the festive occasion of {festa} with fireworks"
if medium == "Mangá" : detalhe = "in a manga art style"
if medium == "Magia" : detalhe = " inspired by the fairtale of"
if medium == "Wired" : detalhe = " constructed from a interwined wires"
if medium == "Fractal" : detalhe = f"a fractal pattern centered around a {objeto}" 
if medium == "Renascentista" : detalhe = " in a Renaissance art style"
if medium == "Zodíaco" : 
	signzod=st.text_input("Digite um signo - Ex: leao")
	detalhe = f"a zen art style representation of the zodiac sign of {signzod}"

if medium == "Escultura" : detalhe = " sketch resembling a 3d sculpture of "
if medium == "Mecânico" : detalhe = "a mechanical version of "
if medium == "Tecido" : detalhe = " a whimsical weavings in the pattern of a "
if medium == "Watercolor" : detalhe = "a watercolor illustration of"
if medium == "Etéreo" : detalhe = "rendered with a soft watercolor texture"
if medium == "Rock Style" : detalhe = " in a dynamic rockstar pose with eletric waves and splashes of color emanating form the instrument"
if medium == "Kawaii Style" : detalhe = " with a pastel colored kawaii style"
if medium == "Expressionismo Abstrato" : detalhe = "in a vibrant and abstract representation of"
if medium == "Grafite" : detalhe = f"the minimalist word {letras} styled in bold graffiti font, radiating with neon hues"







# Exibir o prompt
st.write("Prompt Gerado:")
st.write(prompt)
if palavra:
	st.write(prompt1)

# Rodar o aplicativo
# Para rodar, salve este script como app.py e execute 'streamlit run app.py' no terminal
