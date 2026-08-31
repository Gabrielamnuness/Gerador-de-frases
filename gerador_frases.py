import streamlit as st
import requests
from deep_translator import GoogleTranslator
import pyjokes

# 1. Configuração da página e injeção do visual CSS personalizado
st.set_page_config(page_title="Frase do dia", page_icon="✨", layout="centered")

st.html("""
    <style>
        .stApp {
            background-color: #151515 !important;
            color: #ffffff !important;
        }
        .main-container {
            background-color: #222;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            text-align: center;
            max-width: 500px;
            margin: 40px auto;
        }
        .titulo {
            color: #ff4757;
            font-size: 2.2rem;
            font-weight: bold;
            margin-bottom: 20px;
            text-align: center;
        }
        .texto-frase {
            font-style: italic;
            font-size: 1.4rem;
            line-height: 1.6;
            color: #ffffff;
            margin-bottom: 15px;
            text-align: center;
        }
        .texto-autor {
            color: #ffa502;
            font-weight: bold;
            font-size: 1.1rem;
            text-align: center;
            margin-bottom: 25px;
        }
        header, footer {visibility: hidden;}
    </style>
""")

# 2. Nova Lógica Segura para Gerar Frases/Pensamentos de Programação
def obter_nova_frase():
    try:
        # Tenta buscar na API original primeiro
        resposta = requests.get("https://quotable.io", timeout=3)
        if resposta.status_code == 200:
            dados = resposta.json()
            frase_en = dados["content"]
            autor = dados["author"]
            frase_pt = GoogleTranslator(source='en', target='pt').translate(frase_en)
            return frase_pt, autor
    except Exception:
        pass # Se der erro na API externa, o Python pula direto para o plano B local abaixo
        
    try:
        # Plano B: Gera um pensamento/piada de computação local em inglês e traduz instantaneamente
        frase_computacao = pyjokes.get_joke()
        frase_pt = GoogleTranslator(source='en', target='pt').translate(frase_computacao)
        return frase_pt, "Pensamento Dev"
    except Exception:
        return "No meio da dificuldade encontra-se a oportunidade.", "Albert Einstein"

# 3. Construção da interface visual estruturada
st.markdown('<p class="titulo">✨ Frase Motivacional</p>', unsafe_allow_html=True)
st.markdown('<div class="main-container">', unsafe_allow_html=True)

frase, autor = obter_nova_frase()

st.markdown(f'<p class="texto-frase">"{frase}"</p>', unsafe_allow_html=True)
st.markdown(f'<p class="texto-autor">- {autor}</p>', unsafe_allow_html=True)

if st.button("🔄 Nova Frase", use_container_width=True):
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)