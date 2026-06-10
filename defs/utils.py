from datetime import datetime, timedelta
import random
import os


def clear():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


def wait(wait_time):
    end = datetime.now() + timedelta(seconds=wait_time)

    while datetime.now() < end:
        pass


def show_title(title, size=30):
    clear()
    print("=" * size)
    print(f"{title:^{size}}")
    print("=" * size)


def show_options(options):
    try:
        limit = range(1, len(options) + 1)
        for i, option in enumerate(options):
            print(f"{i + 1} - {option}")
        opt = int(input("Digite a opcao: "))

        while opt not in limit:
            print("Opcao invalida!")
            opt = int(input("Digite a opcao: "))
    except ValueError:
        show_error()
        return 0
    return opt


def quit():
    show_title("Obrigado por usar o Evenizer!")
    exit()


def gera_id(file):
    pk = str(random.randint(1, 10**6))
    file.seek(0) # coloca ponteiro no inicio para ler o arquivo
    while str(pk) in file.read():
        pk = str(random.randint(1, 10**6))
        file.seek(0) # coloca ponteiro no inicio para ler o arquivo
    return pk


def event_date_status(data_str):
    try:
        event_date = datetime.strptime(data_str, "%d/%m/%Y").date()
    except ValueError:
        return "Data inválida"

    today = datetime.now().date()
    delta = (event_date - today).days

    if delta > 0:
        return f"Faltam {delta} dias"
    if delta == 0:
        return "Hoje é o evento"
    return f"Já se passaram {abs(delta)} dias"


def show_error():
    print("Valor invalido, tente novamente")
    input("Pressione ENTER para continuar... ")