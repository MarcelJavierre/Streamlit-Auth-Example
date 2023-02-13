"""
Módulo responsável por converter senhas para o formato hash.
"""

import streamlit_authenticator as stauth

passwords = ["123456"]

hashList = stauth.Hasher(passwords).generate()

for hash in hashList:
    print(hash)
