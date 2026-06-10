import random
import os


def clear():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


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
        print('-' * 30)
        opt = int(input("Digite a opção: "))

        while opt not in limit:
            print("Escolha inválida. Tente novamente.")
            opt = int(input("Digite a opção: "))
        
        return opt
    
    except ValueError:
        show_message()
        return 0
    
    except Exception as e:
        print("Um erro inesperado ocorreu. Por favor, contate o suporte.")
        # NOTE: comment in prod
        # print(f"Erro: {e}")


def quit():
    show_title("Obrigado por usar o Evenizer!")
    exit()


def gera_id(file):
    id = str(random.randint(1, 10**6))
    
    while str(id) in file.read():
        id = str(random.randint(1, 10**6))
    return id


def show_message(message="Valor inválido. Tente novamente."):
    print(message)
    input("Pressione ENTER para continuar... ")


def help():
    show_title("SUPORTE")
    print("WhatsApp: +55 99 99999-9999")
    print("Email: suporte@evenizer.com")
    print("Instagram: @evenizer")
    input("Aperte ENTER para voltar...")