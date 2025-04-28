import streamlit as st
import re
import datetime


#Configuração da página
st.set_page_config(
    page_title="Biblioteca Virtual",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="auto",
)


#Título
st.title("Cadastro de usuário")
st.write("Seja bem-vindo ao sistema de cadastro de usuários da biblioteca virtual!")

#Inicialização da variável de login na sessão
if "userLogin" not in st.session_state:
    st.session_state.userLogin = None

#Função para coletar dados simples
def dadosSimples():
    nome = st.text_input("Digite seu nome", max_chars=20)
    sobrenome = st.text_input("Digite seu último sobrenome", max_chars=20)
    emailUsuario = st.text_input("Digite seu email")
    dataNascimentoUsuario = st.date_input(
        "Selecione sua data de nascimento", 
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today()
    )
    
    usuarioSenha = st.text_input("Digite uma senha de 6 dígitos", type="password")
    return nome, sobrenome, emailUsuario, dataNascimentoUsuario, usuarioSenha

#Função para coletar dados do bibliotecário
def dadosBibliotecario():
    nome, sobrenome, emailUsuario, dataNascimentoUsuario, usuarioSenha = dadosSimples()
    registroBibliotecario = st.number_input("Digite seu registro de bibliotecário", step=1, format="%d")
    registroBibliotecario = int(registroBibliotecario)
    return nome, sobrenome, emailUsuario, dataNascimentoUsuario, usuarioSenha, registroBibliotecario

#Função para validar o e-mail
def validar_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

#Função para validar a senha
def validar_senha(senha):
    return len(senha) == 6 and senha.isdigit()

#Função para realizar o login de administrador
def fazer_login():
    st.subheader("Login de Administrador")
    login = st.text_input("Digite seu usuário (adm)", key="login")
    senha = st.text_input("Digite sua senha", type="password", key="senha")
    if st.button("Fazer Login"):
        if login == "adm" and senha == "123456":
            st.session_state.userLogin = "adm"
            st.success("Login realizado com sucesso! Redirecionando...")
            st.rerun()  # Redefine a sessão e recarrega a página
        else:
            st.error("Usuário ou senha incorretos.")

#Se o administrador estiver logado
if st.session_state.userLogin == "adm":
    st.success("Você está logado como Administrador.")
    st.header("Cadastro de Bibliotecário 📖")
    
    nome, sobrenome, emailUsuario, dataNascimentoUsuario, usuarioSenha, registroBibliotecario = dadosBibliotecario()

    if st.button("Cadastrar Bibliotecário"):
        if not nome or not sobrenome or not emailUsuario or not usuarioSenha:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        elif not validar_email(emailUsuario):
            st.error("Email inválido.")
        elif not validar_senha(usuarioSenha):
            st.error("Senha deve ter exatamente 6 dígitos numéricos.")
        else:
            st.success("Bibliotecário cadastrado com sucesso!")

else:
    #Se não estiver logado como administrador, exibe o cadastro de usuário comum
    st.header("Cadastro de Usuário Comum 👤")
    
    nome, sobrenome, emailUsuario, dataNascimentoUsuario, usuarioSenha = dadosSimples()

    if st.button("Cadastrar Usuário"):
        if not nome or not sobrenome or not emailUsuario or not usuarioSenha:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        elif not validar_email(emailUsuario):
            st.error("Email inválido.")
        elif not validar_senha(usuarioSenha):
            st.error("Senha deve ter exatamente 6 dígitos numéricos.")
        else:
            st.success("Usuário cadastrado com sucesso!")
    
    st.divider()

    st.info("Se você é administrador, faça login abaixo para cadastrar bibliotecários.")
    fazer_login()
