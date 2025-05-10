#estruturas e selecao ou condicao
#login basico
email = input("digite seu email: ")
senha = input("digite sua senha: ")
confirmasenha = input("digite a senha de novo ")
if ( senha == confirmasenha):
    print("cadastro finalizado :) ")
else:
    print("a confirmacao de senha nao bate ")

loginemail = input("digite seu email: ")
loginsenha = input("digite sua senha: ")

if(loginemail == email) and ( loginsenha == senha):
    print("logado com sucesso ")
else:
    print("Informacoes invalidas")