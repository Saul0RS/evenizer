from datetime import datetime
from defs.utils import show_options, show_title

def add_event(email, valueError=None):
    show_title("Novo Evento")

    with open("database/events.txt", "a+") as file:  
        file.seek(0)
        v = file.read()
        id = len(v.splitlines()) + 1

        name = input("Digite o nome do evento: ")
        type = show_options(["Aniversário", "Casamento", "Reunião", "Outro"])

        while True:
            data = input("Digite a data do evento (Ex: 09/12/2006): ").strip()
            try:
                datetime.strptime(data, "%d/%m/%Y")
                break
            except valueError:
                print("Data em formato invalido !!! tente novamente")
                continue

        location = input("Digite o local do evento: ")
        budget = float(input("Digite o orçamento do evento: R$ "))

        owner_email = email

        file.seek(0)
        if f"{id}, {name}, {type}, {data}, {location}, {budget}, {owner_email}\n" not in file.read():
            file.write(f"{id}, {name}, {type}, {data}, {location}, {budget}, {owner_email}\n")
            print(f"Evento {name} cadastrado com sucesso.")                      

        else:   
            print("Não pode criar eventos iguais, tente novamente.")


def list_event(email):
    show_title("Listagem de eventos")
    with open("database/events.txt", "a+") as file:
        file.seek(0)
        matriz = []
        for line in file:
            lista = []
            if email in line:
                lista = line.split(",")
                matriz.append(lista)

        verificar = []
        for i in matriz:
            print(f"{i[0]} - {i[1]}, {i[2]}, {i[3]}, {i[4]}")
            verificar.append(i[0])
        input("Pressione ENTER para continuar... ")
        return verificar
    

def add_tarefa(id):
    while True:
        opcao = input("Digite o valor do evento que voce deseja criar a tarefa: ")
        if opcao in id:
            id_event = opcao
            break
        else:
            print("Opção incorreta")
            continue

    show_title("Novo tarefa")  

    with open("database/activities.txt", "a+") as file:
        file.seek(0)
        v = file.read()
        id_tarefa = len(v.splitlines()) + 1
        
        nome = input("Digite o nome da tarefa: ")
        custo = float(input("Digite o custo do evento: "))
             
        file.write(f"{id_tarefa}, {nome}, {custo}, {id_event}\n")
        print(f"Tarefa {nome} cadastrada com sucesso.")

def delete_event(email):

    id = list_event(email)
    while True:
        opcao = input('Digite o id do evento que deseja excluir: ')
        if opcao in id:
            break
        else:
            print('opçao invalida')
    with open('database/events.txt', 'r') as file:
        linhas = file.readlines()
    novas_linas = []
    for linha in linhas:
        dados = linha.split(",")
        if dados[0].strip() != opcao:
            novas_linas.append(linha)
    with open('database/events.txt', 'w') as file:
        file.writelines(novas_linas)
    print('Evento excluido com sucesso')