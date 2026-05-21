import os 

def show_options(options):

    limit = range(1, len(options) + 1)
    for i, option in enumerate(options):
        print(f"{i + 1} - {option}")
    opt = int(input("Digite a opcao: "))

    while opt not in limit:
        print("Opcao invalida!")
        opt = int(input("Digite a opcao: "))
    return opt

def initial_menu():

    opcao = show_options(["Cadastrar", "Entrar", "Visualizar Eventos", "Sair"])
    
    os.system("cls")
    if opcao == 1:
        add_user()
    elif opcao == 2:
        login()
    elif opcao == 3:
        print("Visualizar Eventos")
    elif opcao == 4:
        print("Sair")
    

def add_user():

    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    #Colocar perguntas e respostas de segurança aqui para recuperação de senha no login()  
    with open("database/users.txt", "a", encoding="utf-8") as file:
        file.write(f"\"nome\": \"{nome}\", \"senha\": \"{senha}\"\n")

def login():
    #while True
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    with open("database/users.txt", "r", encoding="utf-8") as file:
        if f"\"nome\": \"{nome}\", \"senha\": \"{senha}\"" in file.read():
            print("Login bem-sucedido!")
            return True
        else: 
            print("Login incorreto !!!")
            n = input("Deseja recuperar sua senha? Sim ou Não?").upper()
            os.system("cls")
            if n == 'S' or n == "SIM":
                esqueci_senha()
                os.system("cls")
                print("Tente o login novamente com a nova senha !!!")
                #continue pro while True aqui
            elif n == 'N' or n == "NÃO" or n == "NAO":
                return False
            else:
                os.system("cls")
                print("Tente o login novamente novamente !!!")
                #continue pro while True aqui



def esqueci_senha():
    nome = input("Digite seu nome: ").capitalize()
    with open("database/users.txt", "r", encoding="utf-8") as file:
        for linha in file:
            if f"\"nome\": \"{nome}\"" in linha:
                inicio = linha.find('"question":')
                fim = linha.find(",", inicio)
                pergunta = linha[inicio:fim]
                print(pergunta)
                return pergunta
            else:
                return print("n deu certo !!!")
                
            
