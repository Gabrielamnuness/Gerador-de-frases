import streamlit as st
import requests
from deep_translator import GoogleTranslator
import urllib.parse
import random

st.set_page_config(page_title="Frase do dia", page_icon="✨", layout="centered")

st.html("""
    <style>
        /* Fundo escuro total do aplicativo */
        .stApp {
            background-color: #151515 !important;
            color: #ffffff !important;
        }
        
        /* Caixa principal que envelopa o conteúdo */
        .stMainBlockContainer {
            max-width: 550px !important;
            padding: 40px 30px !important;
            background-color: #222 !important; 
            border-radius: 12px !important; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important; 
            margin: 60px auto !important; 
            text-align: center !important;
        }
        
        /* Título estilizado */
        .titulo-principal {
            color: #ff4757;
            font-size: 2.2rem;
            font-weight: bold;
            margin-bottom: 25px;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        
        /* Frase motivacional */
        .texto-dinamico {
            font-style: italic;
            font-size: 1.4rem;
            line-height: 1.6;
            color: #ffffff;
            margin: 25px 0 35px 0 !important;
            text-align: center;
        }
        
        /* FORÇA A CENTRALIZAÇÃO DOS BOTÕES DENTRO DA CAIXA */
        [data-testid="stButton"], [data-testid="stLinkButton"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 100% !important;
            text-align: center !important;
        }
        
        /* Estilização dos botões (Vermelho e Verde) */
        .stButton > button, .stLinkButton > a {
            border: none !important;
            padding: 12px 24px !important;
            font-size: 1rem !important;
            border-radius: 6px !important;
            font-weight: bold !important;
            transition: 0.3s !important;
            width: 75% !important; /* Tamanho proporcional para não quebrar o texto */
            min-width: 250px !important; /* Garante que o texto não quebre em duas linhas */
            margin: 10px auto !important; /* Centraliza no meio exato da caixa */
            display: inline-flex !important;
            justify-content: center !important;
            align-items: center !important;
            text-align: center !important;
            text-decoration: none !important;
        }
        
        /* Botão "Nova Frase" (Vermelho) */
        .stButton > button {
            background-color: #ff4757 !important;
            color: white !important;
        }
        .stButton > button:hover {
            background-color: #e84118 !important;
        }
        
        /* Botão "Compartilhar" (Verde do WhatsApp) */
        .stLinkButton > a {
            background-color: #25D366 !important;
            color: white !important;
        }
        .stLinkButton > a:hover {
            background-color: #128C7E !important;
        }
        
        /* Oculta elementos padrões do Streamlit */
        header, footer, [data-testid="stHeader"] { visibility: hidden !important; }
    </style>
""")

def buscar_frase_da_api():
    try:
        cache_buster = random.randint(1, 999999)
        url_com_busto = f"https://adviceslip.com{cache_buster}"
        
        resposta = requests.get(url_com_busto, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            frase_ingles = dados["slip"]["advice"]
            frase_traduzida = GoogleTranslator(source='en', target='pt').translate(frase_ingles)
            return frase_traduzida
    except Exception:
        pass
    return "A persistência é o caminho do êxito."

st.markdown('<p class="titulo-principal">Para Lembrar</p>', unsafe_allow_html=True)

frase_gerada = buscar_frase_da_api()
st.markdown(f'<p class="texto-dinamico">"{frase_gerada}"</p>', unsafe_allow_html=True)

# Botão de Nova Frase
if st.button("🔄 Nova Frase"):
    st.rerun()

mensagem_formatada = f"*Frase Motivacional do Dia:*\n\n\"{frase_gerada}\"\n\n_Gerado via App Streamlit_"
link_whatsapp = f"https://whatsapp.com{urllib.parse.quote(mensagem_formatada)}"

# Botão do WhatsApp
st.link_button("Compartilhar no WhatsApp", link_whatsapp)