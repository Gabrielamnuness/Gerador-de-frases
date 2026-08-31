import streamlit as st
import requests
from deep_translator import GoogleTranslator
import urllib.parse

# 1. Configuração da página e injeção do visual CSS definitivo (Centralizado e Sem Ícones)
st.set_page_config(page_title="Frase do dia", layout="centered")

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
            margin: 25px 0 10px 0 !important;
            text-align: center;
        }

        /* Nome do Autor estilizado */
        .texto-autor {
            color: #ffa502;
            font-weight: bold;
            font-size: 1.1rem;
            text-align: center;
            margin-bottom: 35px !important;
        }
        
        /* FORÇA A CENTRALIZAÇÃO ABSOLUTA DOS BOTÕES DO STREAMLIT NA TELA */
        [data-testid="stVerticalBlockBorder"] > div {
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            text-align: center !important;
        }

        [data-testid="stElementContainer"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 100% !important;
        }

        [data-testid="stButton"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 100% !important;
            margin: 0 auto !important;
        }
        
        /* Estilização dos dois botões (Vermelho e Verde) para ficarem idênticos */
        .stButton > button {
            border: none !important;
            padding: 12px 24px !important;
            font-size: 1rem !important;
            border-radius: 6px !important;
            font-weight: bold !important;
            transition: 0.3s !important;
            width: 280px !important; 
            margin: 5px auto !important;
            display: inline-flex !important;
            justify-content: center !important;
            align-items: center !important;
            text-align: center !important;
        }
        
        /* Botão 1: "Nova Frase" (Vermelho) */
        .stButton:nth-of-type(1) > button {
            background-color: #ff4757 !important;
            color: white !important;
        }
        .stButton:nth-of-type(1) > button:hover {
            background-color: #e84118 !important;
        }
        
        /* Botão 2: "Compartilhar no WhatsApp" (Verde) */
        .stButton:nth-of-type(2) > button {
            background-color: #25D366 !important;
            color: white !important;
        }
        .stButton:nth-of-type(2) > button:hover {
            background-color: #128C7E !important;
        }
        
        /* Oculta os cabeçalhos e menus nativos do Streamlit */
        header, footer, [data-testid="stHeader"] { visibility: hidden !important; }
    </style>
""")

# 2. Função em Python que busca uma frase e autor REAL na internet em tempo real
def buscar_frase_da_internet():
    try:
        # Puxa uma frase totalmente aleatória da API global do DummyJSON
        resposta = requests.get("https://dummyjson.com", timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            frase_ingles = dados["quote"]
            autor = dados["author"]
            
            # Traduz a frase dinamicamente usando Python
            frase_traduzida = GoogleTranslator(source='en', target='pt').translate(frase_ingles)
            return frase_traduzida, autor
    except Exception:
        pass
    return "A persistência é o caminho do êxito.", "Charles Chaplin"

# 3. Construção dos elementos visuais na tela
st.markdown('<p class="titulo-principal">Para Lembrar</p>', unsafe_allow_html=True)

# Faz a chamada da API em tempo real a cada carregamento
frase_gerada, autor_original = buscar_frase_da_internet()

st.markdown(f'<p class="texto-dinamico">"{frase_gerada}"</p>', unsafe_allow_html=True)
st.markdown(f'<p class="texto-autor">- {autor_original}</p>', unsafe_allow_html=True)

# Botão Vermelho: Nova Frase (Apenas recarrega a página para puxar outra frase na internet)
if st.button("Nova Frase"):
    st.rerun()

# Configuração automática da mensagem que o WhatsApp vai ler
mensagem_formatada = f"*Para Lembrar:*\n\n\"{frase_gerada}\"\n- {autor_original}"
link_whatsapp = f"https://whatsapp.com{urllib.parse.quote(mensagem_formatada)}"

# Botão Verde: Compartilhar no WhatsApp (Usa Javascript para forçar o navegador a abrir sem dar bloqueio)
if st.button("Compartilhar no WhatsApp"):
    st.html(f"""
        <script type="text/javascript">
            window.top.location.href = "{link_whatsapp}";
        </script>
    """)