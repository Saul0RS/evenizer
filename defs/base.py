
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

    with open("database/users.txt", "a") as file:
        file.write(f"\"nome\": \"{nome}\", \"senha\": \"{senha}\"\n")

def login():

    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    with open("database/users.txt", "r") as file:
        if f"\"nome\": \"{nome}\", \"senha\": \"{senha}\"" in file.read():
            print("Login bem-sucedido!")
            return True
    print("Verifique suas credenciais.")
    return False