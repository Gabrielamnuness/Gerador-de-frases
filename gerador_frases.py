import streamlit as st
import requests
from deep_translator import GoogleTranslator
import urllib.parse

# 1. Configuração da página e estilização dos elementos nativos do Streamlit
st.set_page_config(page_title="Frase do dia", page_icon="✨", layout="centered")

st.html("""
    <style>
        /* Fundo escuro total do aplicativo */
        .stApp {
            background-color: #151515 !important;
            color: #ffffff !important;
        }
        /* Centralização e estilo do bloco principal de conteúdo */
        .stMainBlockContainer {
            max-width: 500px !important;
            padding: 40px 20px !important;
            background-color: #222 !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
            margin: 60px auto !important;
            text-align: center !important;
        }
        /* Estilização do título principal */
        .titulo-principal {
            color: #ff4757;
            font-size: 2.2rem;
            font-weight: bold;
            margin-bottom: 25px;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        /* Estilização da frase motivacional */
        .texto-dinamico {
            font-style: italic;
            font-size: 1.4rem;
            line-height: 1.6;
            color: #ffffff;
            margin: 20px 0 !important;
            text-align: center;
        }
        /* Força todos os botões do Streamlit a ficarem bonitos */
        .stButton > button {
            border: none !important;
            padding: 12px 24px !important;
            font-size: 1rem !important;
            border-radius: 6px !important;
            font-weight: bold !important;
            transition: 0.3s !important;
            width: 100% !important;
            margin-top: 10px !important;
        }
        /* Botão "Nova Frase" (Vermelho) */
        .stButton:nth-of-type(1) > button {
            background-color: #ff4757 !important;
            color: white !important;
        }
        .stButton:nth-of-type(1) > button:hover {
            background-color: #e84118 !important;
        }
        /* Botão "Compartilhar" (Verde do WhatsApp) */
        .stButton:nth-of-type(2) > button {
            background-color: #25D366 !important;
            color: white !important;
        }
        .stButton:nth-of-type(2) > button:hover {
            background-color: #128C7E !important;
        }
        /* Oculta menus e rodapés padrões do Streamlit */
        header, footer, [data-testid="stHeader"] { visibility: hidden !important; }
    </style>
""")

# 2. Função em Python para buscar frases da API em tempo real
def buscar_frase_da_api():
    try:
        resposta = requests.get("https://adviceslip.com", timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            frase_ingles = dados["slip"]["advice"]
            frase_traduzida = GoogleTranslator(source='en', target='pt').translate(frase_ingles)
            return frase_traduzida
    except Exception:
        pass
    return "A persistência é o caminho do êxito."

# 3. Construção estruturada da interface
st.markdown('<p class="titulo-principal">Para lembrar</p>', unsafe_allow_html=True)

# Puxa a API em tempo real para gerar uma nova frase a cada atualização
frase_gerada = buscar_frase_da_api()
st.markdown(f'<p class="texto-dinamico">"{frase_gerada}"</p>', unsafe_allow_html=True)

# Botão 1: Recarrega a página e muda a frase automaticamente
if st.button("🔄 Nova Frase"):
    st.rerun()

# Criação dinâmica do link de compartilhamento para o WhatsApp
mensagem_formatada = f"*Frase Motivacional do Dia:*\n\n\"{frase_gerada}\"\n\n_Gerado via App Streamlit_"
link_whatsapp = f"https://whatsapp.com{urllib.parse.quote(mensagem_formatada)}"

# Botão 2: Redireciona o usuário para o WhatsApp com a frase pronta
st.link_button(" Compartilhar no WhatsApp", link_whatsapp)