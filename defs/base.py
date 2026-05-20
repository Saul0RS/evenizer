
def show_options(options):

    limit = range(len(options))
    for i, option in enumerate(options):
        print(f"{i} - {option}")
    opt = int(input("Digite a opcao: "))

    while opt not in limit:
        print("Opcao invalida!")
        opt = int(input("Digite a opcao: "))
    return opt

def entrada_menu():

    opcao = show_options(["Cadastrar", "Entrar", "Visualizar Eventos", "Sair"])

def add_user():

    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")