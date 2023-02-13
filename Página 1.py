"""
Módulo responsável por criar a página 1.
"""

import streamlit as st

from auth import authenticator, authenticate

# Se a autenticação for bem sucedida, escreve o conteúdo da página
if (authenticate()):
    # Abre o arquivo com o conteúdo da página e armazena seu conteúdo
    with open("markdown/Página 1.md", "r", encoding="UTF-8") as pageFile:
        pageContent = pageFile.read()

    # Escreve o conteúdo da página
    st.write(pageContent)

    # Adiciona um botão na página que encerra a sessão do usuário ao ser clicado
    authenticator.logout("Logout")
