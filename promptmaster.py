import streamlit as st

# Função para gerar prompts de insights baseados na atividade profissional
def gerar_prompts(atividade_profissional):
    prompts = [
        f"Quais são as tendências emergentes em {atividade_profissional}?",
        f"Como a tecnologia está mudando o campo de {atividade_profissional}?",
        f"Quais habilidades são mais valorizadas em {atividade_profissional} atualmente?",
        f"Como melhorar a eficiência e produtividade em {atividade_profissional}?",
        f"Quais são os maiores desafios enfrentados por profissionais de {atividade_profissional} hoje?",
        f"Como iniciar uma carreira em {atividade_profissional}?",
        f"Quais estratégias de networking são mais eficazes para alguém em {atividade_profissional}?",
        f"Como {atividade_profissional} pode contribuir para o desenvolvimento sustentável?",
        f"Quais são as melhores práticas para inovação em {atividade_profissional}?",
    ]
    return prompts

# Título do aplicativo
st.title("Gerador de Prompts para Insights Profissionais")

# Entrada do usuário
atividade_profissional = st.text_input("Digite sua atividade profissional:", "")

# Botão para gerar prompts
if st.button("Gerar Prompts"):
    if atividade_profissional:
        prompts = gerar_prompts(atividade_profissional)
        st.write("Aqui estão alguns prompts para explorar insights profissionais:")
        for prompt in prompts:
            st.write(f"- {prompt}")
    else:
        st.write("Por favor, insira uma atividade profissional.")