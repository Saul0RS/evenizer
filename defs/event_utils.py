from datetime import datetime
from defs.utils import show_options, show_title

def add_event(email):
    show_title("Novo Evento")
    event = {}
    event["name"] = input("Digite o nome do evento: ")
    event["type"] = show_options(["Aniversário", "Casamento", "Reunião", "Outro"])

    while True:
        try:
            event["date"] = input("Digite a data do evento (Ex: 09/12/2006): ")
        except:
            print(f"Data inválida. Tente novamente.")
        break

    event["location"] = input("Digite o local do evento: ")
    event["budget"] = float(input("Digite o orçamento do evento: R$ "))
    event["tasks"] = []
    print("Deseja adicionar tarefas ao evento agora? [S/N]")
    while True:
        opt = show_options(["Sim", "Não"])
        if opt == 1:
            print("Função de adicionar tarefas aqui")
            break
        elif opt == 2:
            break

    event["owner_email"] = email
    with open("database/events.txt", "a+") as file:  
        file.seek(0)
        if str(event) not in file.read(): # ler o arquivo e faz o ponteiro voltar para o final, para ai sim acrescentar a informação
            file.write(str(event) + "\n")
            print(f"Evento '{event['name']}' cadastrado com sucesso.")                      

        else: 
            print("O evento não pode ocorrer no mesmo lugar, ao mesmo tempo e no mesmo dia que outro evento. Tente novamente.")
