from datetime import datetime, timedelta
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

    limit = range(1, len(options) + 1)
    for i, option in enumerate(options):
        print(f"{i + 1} - {option}")
    opt = int(input("Digite a opcao: "))

    while opt not in limit:
        print("Opcao invalida!")
        opt = int(input("Digite a opcao: "))
    return opt

def quit():
    show_title("Obrigado por usar o Evenizer!")
    exit()