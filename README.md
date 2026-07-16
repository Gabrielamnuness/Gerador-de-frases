# Gerador de Frases

Aplicativo simples em Python que obtém frases motivacionais aleatórias de uma API pública e traduz o texto para português.

## Funcionalidades

- Busca uma frase aleatória da API `https://api.quotable.io/random`
- Traduz a frase de inglês para português usando `deep-translator`
- Exibe a frase com o autor usando Streamlit

## Requisitos

- Python 3.8+
- `streamlit`
- `requests`
- `deep-translator`

## Instalação

1. Clone ou baixe o projeto.
2. Abra um terminal na pasta do projeto.
3. Instale as dependências:

```bash
pip install streamlit requests deep-translator
```

## Uso

Execute o aplicativo com Streamlit:

```bash
streamlit run gerador_frases.py
```

O app será aberto no navegador e exibirá uma frase traduzida para português.

## Observações

- O script faz uma requisição HTTP a uma API externa.
- O parâmetro `verify=False` está definido para a requisição, o que ignora a verificação de certificado TLS. Em produção, recomenda-se remover esse parâmetro e usar uma conexão segura.
