import os 
from datetime import datetime
import random
from utils import clear

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
    while True:
        opcao = show_options(["Cadastrar usuario", "Entrar com usuario", "Sair do programa"])
        
        clear()
        if opcao == 1:
            add_user()
            continue
        elif opcao == 2:
            email = login()
            if email:
                menu_login(email)
            else:
                continue
        elif opcao == 3:
            break


def menu_login(email):
    while True:
        opcao = show_options(["Cadastrar evento ou tarefa", "Visualizar", "Modificar", "Excluir", "Voltar"])
        
        clear()
        if opcao == 1:
            menu_cadastro(email)
            continue
        elif opcao == 2:
            print("Colocar função de visualizar aqui !!!")
            continue
        elif opcao == 3:
            print("Colocar função de modificar aqui !!!")
            continue
        elif opcao == 4:
            print("Colocar função de excluir aqui !!!")
        elif opcao == 5:
            break

            
def menu_cadastro(email):
    while True:
        opcao = show_options(["Cadastrar evento", "Cadastrar tarefa", "Voltar"])
        
        clear()
        if opcao == 1:
            pk = add_event(email)
            continue
        elif opcao == 2:
            print("Colocar função de visualizar aqui !!!")
            continue
        elif opcao == 3:
            break


def add_user():
    while True:
        email = input("Digite seu email: ")

        with open("database/users.txt", "a+") as file: # ponteiro do arquivo começa no final pq abriu como "a"
            file.seek(0)  # coloca ponteiro no inicio para ler o arquivo
            if f"\"email\": \"{email}\"" not in file.read(): # ler o arquivo e faz o ponteiro voltar para o final, para ai sim acrescentar a informação
                if "@" in email:
                    nome = input("Digite seu nome: ")    
                    senha = input("Digite sua senha: ")
                    clear()
                    pergunta = input("Digite uma pergunta de segurança, para recuperação de senha posteriormente:\n--> ")
                    resposta = input("Digite a sua resposta para a pergunta: ")

                    file.write(f"\"nome\": \"{nome}\", \"email\": \"{email}\", \"senha\": \"{senha}\", \"pergunta:\": \"{pergunta}\", \"resposta\": \"{resposta}\"\n")
                    print("Usuario adicionado com sucesso !!!")
                    break

                else:
                    print("Esse email não é valido !!! tente novamente !!!")

            else:
                print("Esse email já existe !!! tente um diferente !!!")
                continue

def login():

    email = input("Digite o seu email: ")
    senha = input("Digite sua senha: ")

    with open("database/users.txt", "r") as file:
        if f"\"email\": \"{email}\", \"senha\": \"{senha}\"" in file.read():
            print("Login bem-sucedido!")
            return email
        else:
            print("Login incorreto tente novamente !!!")
            return False


def add_event(email):
    while True:
        nome = input("Digite o nome do evento: ")
        tipo = input("Digite o tipo de evento: ")

        while True:
            data = input("Digite a data do evento (Ex: 09/12/2006): ")
            try:
                datetime.strptime(data, "%d/%m/%y")
            except:
                print("Data em formato invalido !!! tente novamente")
                continue
            break

        local = input("Digite o local do evento: ") 
        orçamento = float(input("Digite o orçamento do evento: "))

        with open("database/events.txt", "a+") as file: # ponteiro do arquivo começa no final pq abriu como "a"    
            file.seek(0)
            if f"\"nome\": \"{nome}\", \"data\": \"{data}\", \"local\": \"{local}\"" not in file.read(): # ler o arquivo e faz o ponteiro voltar para o final, para ai sim acrescentar a informação
                file.write(f"\"nome\": \"{nome}\", \"tipo\": \"{tipo}\", \"data\": \"{data}\", \"local\": \"{local}\", \"orçamento\": \"{orçamento}\", \"emailuser\": \"{email}\"\n")
                print("Evento cadastrado com sucesso !!!")                      
                break

            else: 
                print("O evento não pode ocorrer no mesmo lugar, ao mesmo tempo e no mesmo dia que outro evento !!! tente novamente !!!")
                continue
        


