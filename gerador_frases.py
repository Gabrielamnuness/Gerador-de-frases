import streamlit as st
import requests
from deep_translator import GoogleTranslator

# 1. Configuração da página e injeção do visual idêntico à página web
st.set_page_config(page_title="Frase do dia", page_icon="✨", layout="centered")

st.html("""
    <style>
        /* Fundo escuro do app */
        .stApp {
            background-color: #151515 !important;
            color: #ffffff !important;
        }
        /* Caixa centralizada do projeto */
        .main-container {
            background-color: #222;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            text-align: center;
            max-width: 500px;
            margin: 40px auto;
        }
        /* Estilo do título principal */
        .titulo {
            color: #ff4757;
            font-size: 2.2rem;
            font-weight: bold;
            margin-bottom: 20px;
            text-align: center;
        }
        /* Estilo da frase dinâmica */
        .texto-frase {
            font-style: italic;
            font-size: 1.4rem;
            line-height: 1.6;
            color: #ffffff;
            margin-bottom: 15px;
            text-align: center;
        }
        /* Esconde cabeçalhos nativos do Streamlit */
        header, footer {visibility: hidden;}
    </style>
""")

# 2. Função em Python que consulta a API externa em tempo real
def buscar_frase_da_api():
    try:
        # Consulta uma API pública e estável de conselhos/frases aleatórias
        resposta = requests.get("https://adviceslip.com", timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            frase_ingles = dados["slip"]["advice"]
            
            # Traduz a frase dinamicamente usando Python
            frase_traduzida = GoogleTranslator(source='en', target='pt').translate(frase_ingles)
            return frase_traduzida
    except Exception:
        pass
    # Caso sua internet ou a API falhem temporariamente, exibe uma frase reserva
    return "A persistência é o caminho do êxito."

# 3. Montagem da interface na tela
st.markdown('<p class="titulo">✨ Frase Motivacional</p>', unsafe_allow_html=True)
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Gera a frase dinamicamente puxando a API a cada atualização da página
frase_dinamica = buscar_frase_da_api()
st.markdown(f'<p class="texto-frase">"{frase_dinamica}"</p>', unsafe_allow_html=True)

# Botão nativo do Streamlit que recarrega o script e busca uma frase inédita na API
if st.button("🔄 Nova Frase", use_container_width=True):
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)