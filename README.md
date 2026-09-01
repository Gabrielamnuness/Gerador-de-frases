# Gerador de Frases - "Para Lembrar"

Aplicativo web em Python que obtém frases motivacionais aleatórias de uma API pública, traduz para português e exibe com um design moderno e elegante. Inclui funcionalidade de compartilhamento direto no WhatsApp.

## Acesso Online

Acesse o aplicativo diretamente no navegador (sem necessidade de instalação):

**https://gerador-de-frases.streamlit.app/**

## Funcionalidades

- Busca frases aleatórias em tempo real da API `https://dummyjson.com/quotes/random`
- Traduz automaticamente de inglês para português usando `deep-translator`
- Interface visual moderna com tema dark mode personalizado
- Botão "Nova Frase" para gerar frases ilimitadamente
- Compartilhamento direto no WhatsApp com a frase gerada
- Frase padrão de fallback caso a API esteja indisponível
- Design responsivo e centralizado
- Sem anúncios ou cabeçalhos/rodapés do Streamlit

## Requisitos

- Python 3.8+
- Dependências do projeto (listadas em `requirements.txt`):
  - `streamlit` - Framework web
  - `requests` - Requisições HTTP
  - `deep-translator` - Tradução de textos

## Instalação

1. Clone ou baixe o projeto:
```bash
git clone <seu-repositorio>
cd Gerador-de-frases
```

2. Abra um terminal na pasta do projeto

3. (Opcional) Crie um ambiente virtual:
```bash
python -m venv .venv
```

4. Ative o ambiente virtual:
   - **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   - **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

5. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Execute o aplicativo com Streamlit:

```bash
streamlit run gerador_frases.py
```

O aplicativo será aberto automaticamente no navegador (geralmente em `http://localhost:8501`).

### Como usar:
1. A frase motivacional e seu autor serão exibidos automaticamente
2. Clique em **"Nova Frase"** para gerar uma nova frase motivacional
3. Clique em **"Compartilhar no WhatsApp"** para enviar a frase para um contato ou grupo

## Design

- **Tema:** Dark Mode com acentos em vermelho (#ff4757) e verde WhatsApp (#25D366)
- **Layout:** Centralizado e responsivo
- **Tipografia:** Moderna e clara
- **Efeitos:** Transições suaves nos botões

## Observações

- O script faz requisições HTTP a uma API externa em tempo real
- Requer conexão com a internet para funcionamento completo
- Tradução está limitada ao Google Translator (pode ter limitações de taxa)
- O compartilhamento no WhatsApp requer um cliente WhatsApp instalado

## APIs Utilizadas

- **Quotes API:** `https://dummyjson.com/quotes/random` - Fornece citações em inglês
- **Google Translator:** Integrado via `deep-translator` - Traduz para português
