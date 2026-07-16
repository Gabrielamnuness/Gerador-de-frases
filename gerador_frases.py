import streamlit as st
import requests
from deep_translator import GoogleTranslator

def obter_frase():
    url = "https://api.quotable.io/random"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        frase = response.json() ["content"]
        frase = traduzir_texto(frase)
        autor = response.json() ["author"]
        return f'"{frase}" - {autor}'
    else:
        print("Erro ao obter frase", "Desconhecido")
        return None
    
def traduzir_texto(texto):
    tradutor = GoogleTranslator(source='en', target='pt')
    return tradutor.translate(texto)        

print(traduzir_texto(obter_frase()))
        
def exibir_frase():
    frase = obter_frase()
    if frase:
        st.write(frase)
    else:
        st.write("Não foi possível obter uma frase no momento.")

exibir_frase()
