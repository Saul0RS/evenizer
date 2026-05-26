from utils import show_title

def add_user():
    show_title("Criar Conta")    
    name = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    password = input("Digite sua senha: ")

    with open("database/users.txt", "a+") as file:
        # returns cursor to the beginning of the file
        file.seek(0)
        if f"\"email\": \"{email}\"" in file.read():
            print("Por favor, verifique os dados e tente novamente.")
            return 1
        
        file.write(f"{{\"nome\": \"{name}\", \"email\": \"{email}\", \"senha\": \"{password}\"}}\n")
        print("Usuário cadastrado com sucesso!")
        return 0

def login():
    show_title("Login")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    with open("database/users.txt", "r") as file:
        if f"\"email\": \"{email}\", \"senha\": \"{senha}\"" in file.read():
            print("Login bem-sucedido!")
            return email
        else:
            print("Login incorreto tente novamente !!!")
            return False