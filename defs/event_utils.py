from datetime import datetime
from defs.utils import show_options, show_title, gera_id, show_message
from defs.file_utils import get_lines_by_filter, get_by_filter


EVENTS_FILE_PATH = "database/events.txt"
ACTIVITIES_FILE_PATH = "database/activies.txt"


def add_event(owner_email):
    show_title("Novo Evento")
    with open(EVENTS_FILE_PATH, "a+") as file:  
        pkevent = gera_id(file)
        name = input("Digite o nome do evento: ")
        try:
            type = show_options(["Aniversário", "Casamento", "Reunião", "Outro"])
            data = input("Digite a data do evento (Ex: 09/12/2006): ").strip()
            datetime.strptime(data, "%d/%m/%Y")
            location = input("Digite o local do evento: ")
            budget = float(input("Digite o orçamento do evento: R$ "))

        except (ValueError, TypeError):
            show_message()
            return

        file.seek(0)
        if f"{name},{type},{data},{location}" not in file.read():
            file.write(f"{pkevent},{name},{type},{data},{location},{budget},{owner_email}\n")
            print(f"Evento {name} cadastrado com sucesso.")   
            input("Pressione ENTER para continuar... ")                   

        else:
            print("Não pode criar eventos iguais, tente novamente.")
            input("Pressione ENTER para continuar... ")


def list_events(email):
    show_title("Meus Eventos")
    events = get_lines_by_filter(EVENTS_FILE_PATH, email)
    events_ids = [event.split(",")[0] for event in events]

    if len(events) > 0:
        for event in events:
            print(event.replace(",", ", "))
        opt = show_options(["Editar Evento", "Excluir Evento", "Voltar"])

        if opt == 1:
            event_id = input("Digite o ID do evento: ")
                
            while event_id not in events_ids:
                show_message("ID inválido. Tente novamente.")
                event_id = input("Digite o ID do evento: ")
            update_event(event_id)
        elif opt == 2:
            delete_event(email)

        else:
            return
    else:
        show_message("Você não tem eventos cadastrados.")


def update_event(event_id):
    
    event = get_by_filter(EVENTS_FILE_PATH, event_id).split(",")
    
    print(f"ID: {event[0]} | Nome: {event[1]} | Data: {event[3]} | Local: {event[4]} | Orçamento: R$ {event[5]}")

    while True:
        opt = input("Deseja atualizar este evento? [S/N] ")
        if opt not in "SN":
            continue
        elif opt == "N":
            show_message("Evento não atualizado. Retornando para menu anterior.")
            return
        else:
            break

    print(f"Nome atual: {event[1]}")
    novo_nome = input("Novo nome: ").strip()
    if novo_nome:
        event[1] = novo_nome

    try:
        print(f"Data atual: {event[3]}")
        nova_data = input("Nova data (dd/mm/aaaa): ").strip()
        if nova_data:
            datetime.strptime(nova_data, "%d/%m/%Y")
            event[3] = nova_data

        print(f"Local atual: {event[4]}")
        novo_local = input("Novo local: ").strip()
        if novo_local:
            event[4] = novo_local

        print(f"Orçamento atual: R$ {event[5]}")
        novo_orcamento = input("Novo orçamento: R$ ").strip()
        if novo_orcamento:
            event[5] = float(novo_orcamento)

    except (ValueError, TypeError):
        show_message()
        return

    show_message("Evento atualizado :O")


def delete_event(email):

    id = list_events(email)
    while True:
        opcao = input('Digite o id do evento que deseja excluir: ')
        if opcao in id:
            break
        else:
            print('opçao invalida')
    with open(EVENTS_FILE_PATH, 'r') as file:
        linhas = file.readlines()
    novas_linas = []
    for linha in linhas:
        dados = linha.split(",")
        if dados[0].strip() != opcao:
            novas_linas.append(linha)
    with open(EVENTS_FILE_PATH, 'w') as file:
        file.writelines(novas_linas)
    show_message("Evento excluido com sucesso")
