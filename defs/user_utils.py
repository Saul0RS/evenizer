from defs.utils import show_title, show_message, show_options
from defs.file_utils import *

# these UPPERCASE VARIABLES are CONSTANTS which means you should NOT change them
USERS_FILE_PATH = "database/users.txt"
TRY_AGAIN_MESSAGE = "Verifique seus dados e tente novamente."


def add_user():
    show_title("Criar Conta")    

    name = input("Digite seu nome: ")
    email = input("Digite seu email: ")

    while not "@" in email or email.count("@") != 1:
        print("Email inválido.")
        email = input("Digite seu email: ")

    password = input("Digite sua senha: ")

    while len(password) < 6 or not (any(char.isalpha() for char in password) and any(char.isdigit() for char in password)):
        print("Senha muito fraca. Use letras, números e ao menos 6 caracteres.")
        password = input("Digite sua senha: ")

    if get_by_filter(USERS_FILE_PATH, email):
        show_message(TRY_AGAIN_MESSAGE)
        return 1
 
    save(USERS_FILE_PATH, f"{name},{email},{password}\n")
    show_message("Usuário cadastrado com sucesso!") 
    return 0


def login():
    show_title("Login")

    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    
    if get_by_filter(USERS_FILE_PATH, f"{email},{senha}"):
        show_message("Login bem-sucedido!")
        return email
    show_message(TRY_AGAIN_MESSAGE)
    return False


def update_user(email):
    show_title("Atualizar Dados")
    try:
        name = input("Digite seu nome: ")
        password = input("Digite sua senha: ")
    
        update_line(USERS_FILE_PATH, email, f"{name},{email},{password}\n")

        show_message("Sucesso!")

    except:
        print("Erro.")


def delete_user(email):
    try:
        user_data = get_by_filter(USERS_FILE_PATH, email)
        if (user_data):
            delete_line(USERS_FILE_PATH, user_data)

            show_message("Sucesso!")
        show_message("Verifique seus dados e tente novamente.")

    except FileNotFoundError:
        print("Erro Interno. Por favor, contate o suporte.")
    except:
        print("Erro inesperado. Por favor, contate o suporte.")


def profile(email):
    show_title("Perfil")
    try:
        user = get_by_filter(USERS_FILE_PATH, email)

        if user:
            name, email, password = user.split(",")
            print(f"{'Nome':<10}{name:^20}")
            print(f"{'Email':<10}{email:^20}")
            print('-' * 30)
            opt = show_options(["Atualizar dados", "Excluir conta", "Voltar"])

            if opt == 1:
                show_title("Atualizar Dados")

                name = input("Digite seu nome: ")
                password = input("Digite sua senha: ")
            
                update_line(USERS_FILE_PATH, email, f"{name},{email},{password}\n")

                show_message("Sucesso!")

            elif opt == 2:
                delete_user(email)
            
            else:
                return
    except:
        print("Erro inesperado. Saindo do sistema...")
        quit()