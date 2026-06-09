from datetime import datetime
from defs.utils import show_options, show_title, gera_id


def add_event(email):
    show_title("Novo Evento")

    with open("database/events.txt", "a+") as file:  
        pkevent = gera_id(file)
        name = input("Digite o nome do evento: ")
        type = show_options(["Aniversário", "Casamento", "Reunião", "Outro"])

        while True:
            data = input("Digite a data do evento (Ex: 09/12/2006): ").strip()
            try:
                datetime.strptime(data, "%d/%m/%Y")
                break  
            except ValueError:
                print("Data em formato invalido !!! tente novamente")
                continue

        location = input("Digite o local do evento: ")
        budget = float(input("Digite o orçamento do evento: R$ "))

        owner_email = email

        file.seek(0)
        if f"{pkevent}, {name}, {type}, {data}, {location}, {budget}, {owner_email}\n" not in file.read():
            file.write(f"{pkevent}, {name}, {type}, {data}, {location}, {budget}, {owner_email}\n")
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
        pktask = gera_id(file)
        
        nome = input("Digite o nome da tarefa: ")
        custo = float(input("Digite o custo do evento: "))
             
        file.write(f"{pktask}, {nome}, {custo}, {id_event}\n")
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
    def update_event(email):
        eventos = []
        try:
            arq = open("database/events.txt", "r", encoding="utf-8")
            colunas = arq.readlines()
            arq.close()
        except FileNotFoundError:
            print("deu erro kkkk.")
            return
    
        for linhas in colunas:
         if colunas:
                separa = linhas.split(',')
                id_evento = int(separa[0])
                nome = separa[1]  
                tipo = int(separa[2]) 
                data = (separa[3]) 
                local = (separa[4]) 
                orcamento = float(separa[5])
                email_dono = separa[6].strip()
                if email_dono == email:
                    eventos.append([id_evento, nome, tipo, data, local, orcamento, email_dono]))
   
        if not eventos:
          print("Nenhum evento cadastrado.")
          return
        
        print("Eventos disponíveis:")
        for i in range(len(eventos)):
            ev = eventos[i]
            print(f"{i+1}. ID: {ev[0]} | Nome: {ev[1]} | Data: {ev[3]} | Local: {ev[4]}")

        try:
            escolha = int(input("Número do evento a editar: "))
            if escolha < 0 or escolha >= len(eventos):
                print("Número inválido.")
                return
        except ValueError:
            print("Digite um número válido, por favor.")
            return

        evento = eventos[escolha - 1]

        print("aprete enter para manter do mesmo jeito.")

        novo_nome = input(f"Nome atual: {evento[1]}\nNovo nome: ").strip()
        if novo_nome:
            evento[1] = novo_nome

        nova_data = input(f"Data atual: {evento[3]}\nNova data (dd/mm/aaaa): ").strip()
        if nova_data:
            try:
                datetime.strptime(nova_data, "%d/%m/%Y")
                evento[3] = nova_data
            except ValueError:
                print("Data inválida! Mantendo a anterior.")

        novo_local = input(f"Local atual: {evento[4]}\nNovo local: ").strip()
        if novo_local:
            evento[4] = novo_local
            
        novo_orcamento = input(f"Orçamento atual: R$ {evento[5]}\nNovo orçamento: R$ ").strip()
        if novo_orcamento:
            try:
                evento[5] = float(novo_orcamento)
            except ValueError:
                print("Valor inválido. ainda vai tar com mesmo valor")
        try:
            colunas = open("database/events.txt", "w", encoding="utf-8")
            for ev in eventos:
                linha = f"{ev[0]},{ev[1]},{ev[2]},{ev[3]},{ev[4]},{ev[5]},{ev[6]}"
                colunas.write(linha + "\n")
            colunas.close()
            print("Evento atualizado :O")
        except Exception as e:
            print(f"Erro de salvar: {e}")
    
