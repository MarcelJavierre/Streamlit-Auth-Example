"""
Módulo responsável pela autenticação do usuário.
"""

import streamlit as st
import streamlit_authenticator as stauth
import yaml

# Abre o arquivo com as configurações e armazena seu conteúdo no formato de dicionário
with open("config.yaml", "r", encoding="UTF-8") as configFile:
    configContent: dict = yaml.load(configFile, yaml.SafeLoader)

# Cria o objeto responsável pela autenticação
authenticator = stauth.Authenticate(
    configContent["credentials"],
    configContent["cookie"]["name"],
    configContent["cookie"]["key"],
    configContent["cookie"]["expiry_days"],
)

def authenticate() -> bool:
    """
    Função para verificar a autenticação do usuário.

    Retorna:

    Verdadeiro caso a autenticação tenha sido bem-sucedida ou falso
    senão.
    """
    # Se as variáveis de autenticação não tiverem sido iniciadas, inicia elas com o valor "None"
    if "name" not in st.session_state: st.session_state["name"] = None
    if "authentication_status" not in st.session_state: st.session_state["authentication_status"] = None
    if "username" not in st.session_state: st.session_state["username"] = None

    # Cria a tela de login
    st.session_state["name"], st.session_state["authentication_status"], st.session_state["username"] = authenticator.login("Login", "main")

    # Se a autenticação for bem-sucedida, retorna verdadeiro
    if st.session_state["authentication_status"]:
        return True
    # Senão, se a autenticação não for bem-sucedida, mostra para o
    # usuário uma mensagem de erro e retorna falso
    elif st.session_state["authentication_status"] == False:
        # Mostra para o usuário uma mensagem de erro
        st.error("Nome de usuário e/ou senha incorreto(s).")

        # Retorna falso
        return False
    # Senão, mostra para o usuário uma mensagem para ele inserir seu
    # nome de usuário e senha e retorna falso
    else:
        # Mostra para o usuário uma mensagem de solicitação
        st.warning("Por favor, insira seu nome de usuário e a senha.")

        # Retorna falso
        return False
