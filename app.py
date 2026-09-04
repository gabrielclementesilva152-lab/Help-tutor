%%write app.py
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Help - Tutor Escolar", page_icon="🎓")

st.title("🎓 Help: Seu Tutor Escolar Inteligente")
st.write("Estou aqui para te guiar no aprendizado, estimulando seu raciocínio!")

# Insira sua chave da API do Gemini aqui entre as aspas
GOOGLE_API_KEY = "SUA_CHAVE_DE_API_AQUI"
genai.configure(api_key=GOOGLE_API_KEY)

Diretrizes_help = (
    "Você é o Help, um tutor escolar polivalente e adaptável, focado em ensinar.\n"
    "1. JAMAIS dê a resposta ou o código pronto. Faça perguntas guiadas para estimular o raciocínio.\n"
    "2. Você domina todas as matérias escolares (Matemática, Português, Física, História, Biologia, Geografia, entre outras) além de Programação.\n"
    "3. Adapte sua linguagem de acordo com a disciplina e o nível do aluno, usando analogias claras e exemplos práticos.\n"
    "4. JAMAIS ensine programação perigosa ou hacking, nem conteúdo inadequado para estudantes."
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=Diretrizes_help
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Qual é a sua dúvida de hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("O Help está pensando..."):
            chat = model.start_chat(history=[])
            response = chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "
