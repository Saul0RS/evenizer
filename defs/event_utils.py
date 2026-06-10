from datetime import datetime
from defs.utils import show_options, show_title, gera_id, show_error, event_date_status


def add_event(email):
    show_title("Novo Evento")
    with open("database/events.txt", "a+") as file:  
        pkevent = gera_id(file)
        name = input("Digite o nome do evento: ")
        try:
            type = show_options(["Aniversário", "Casamento", "Reunião", "Outro"])
            data = input("Digite a data do evento (Ex: 09/12/2006): ").strip()
            datetime.strptime(data, "%d/%m/%Y")
            location = input("Digite o local do evento: ")
            budget = float(input("Digite o orçamento do evento: R$ "))

        except (ValueError, TypeError):
            show_error()
            return

        owner_email = email

        file.seek(0)
        if f"{name},{type},{data},{location}" not in file.read():
            file.write(f"{pkevent},{name},{type},{data},{location},{budget},{owner_email}\n")
            print(f"Evento {name} cadastrado com sucesso.")   
            input("Pressione ENTER para continuar... ")                   

        else:
            print("Não pode criar eventos iguais, tente novamente.")
            input("Pressione ENTER para continuar... ")


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
            #status = event_date_status(i[3])
            print(f"{i[0]} - {i[1]}, {i[2]}, {i[3]}, {i[4]}, {event_date_status(i[3])}")
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
        try:
            custo = float(input("Digite o custo do evento: "))

        except (ValueError, TypeError):
            show_error()
            return
        
        file.write(f"{pktask},{nome},{custo},{id_event}\n")
        print(f"Tarefa {nome} cadastrada com sucesso.")
        input("Pressione ENTER para continuar... ")

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

def update_tafera():
    id_tafera = input("Digite o id da tafera que deseja alterar: ")
    with open('database/activities.txt', 'r') as file:
        linhas = file.readlines()

    alterou = False

    for i,linha in enumerate(linhas):
        dados = linha.split(",")
        if dados[0].strip() == id_tafera:

            print(f"Nome atual:{dados[2].strip()}")
            novo_nome = input("Digite o novo nome: ")

            print(f"Custo atual:{dados[2].strip()}")
            novo_custo = input("Digite o custo: ")

            if(novo_nome.strip() == dados[1].strip() and novo_custo.strip() == dados[2].strip()):
                print("Nenhuma alterção foi realizada.")

            else:
                linhas[i] = f"{dados[0].strip()},{novo_nome},{novo_custo},{dados[3].strip()}\n"
                alterou = True
            break
    if alterou:
        with open('database/activities.txt', 'w') as file:
            file.writelines(linhas)
        print("tarefa alterada com sucesso")
    input("Pressione ENTER para continuar... ")



def update_event(email):
    eventos = []
    arq = open("database/events.txt" , "r", encoding="utf-8")
    colunas = arq.readlines()
    arq.close()
        
    for linhas in colunas:
        if colunas:
            separa = linhas.split(',')
            id_evento = int(separa[0])
            nome = separa[1]
            tipo = int(separa[2]) 
            data = separa[3]
            local = separa[4]
            orcamento = float(separa[5]) 
            email_dono = separa[6].strip()
            eventos.append([id_evento, nome, tipo, data, local, orcamento, email_dono])

    if not eventos:
        print("Nenhum evento cadastrado.")
        input("Pressione ENTER para continuar... ")
        return
    
    print("Eventos disponíveis:")
    for i in range(len(eventos)):
        ev = eventos[i]
        #status = event_date_status(ev[3])
        print(f"{i+1}. ID: {ev[0]} | Nome: {ev[1]} | Data: {ev[3]} | {event_date_status(ev[3])} | Local: {ev[4]} | Orçamento: R$ {ev[5]}")

    try:
        escolha = int(input("Número do evento a editar: "))
        if escolha <= 0 or escolha > len(eventos):
            print("Número inválido.")
            input("Pressione ENTER para continuar... ")
            return
    except ValueError:
        show_error()
        return

    evento = eventos[escolha - 1]

    print("aperte enter para manter do mesmo jeito.")

    novo_nome = input(f"Nome atual: {evento[1]}\nNovo nome: ").strip()
    if novo_nome:
        evento[1] = novo_nome

    try:
        nova_data = input(f"Data atual: {evento[3]}\nNova data (dd/mm/aaaa): ").strip()
        if nova_data:
            datetime.strptime(nova_data, "%d/%m/%Y")
            evento[3] = nova_data

        novo_local = input(f"Local atual: {evento[4]}\nNovo local: ").strip()
        if novo_local:
            evento[4] = novo_local

        novo_orcamento = input(f"Orçamento atual: R$ {evento[5]}\nNovo orçamento: R$ ").strip()
        if novo_orcamento:
            evento[5] = float(novo_orcamento)

    except (ValueError, TypeError):
        show_error()
        return

    colunas = open("database/events.txt", "w", encoding="utf-8")
    for ev in eventos:
        linha = f"{ev[0]},{ev[1]},{ev[2]},{ev[3]},{ev[4]},{ev[5]},{ev[6]}"
        colunas.write(linha + "\n")
    colunas.close()
    print("Evento atualizado :O")
    input("Pressione ENTER para continuar... ")

def delete_atividade(email_usuario):
    show_title("Excluir Tarefa")
    eventos_usuario_ids = []
    try:
        with open("database/events.txt", "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(',')
                    email_dono = partes[6].strip()
                    if email_dono == email_usuario:
                        id_evento = int(partes[0])
                        eventos_usuario_ids.append(id_evento)
    except FileNotFoundError:
        print("Arquivo de eventos não encontrado.")
        return

    if not eventos_usuario_ids:
        print("Você não possui eventos cadastrados.")
        return
    tarefas_usuario = []
    try:
        with open("database/activities.txt", "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(',')
                    id_tarefa = int(partes[0])
                    nome_tarefa = partes[1].strip()
                    custo = float(partes[2])
                    id_evento = int(partes[3])
                    if id_evento in eventos_usuario_ids:
                        tarefas_usuario.append([id_tarefa, nome_tarefa, custo, id_evento])
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado.")
        return

    if not tarefas_usuario:
        print("Nenhuma tarefa encontrada nos seus eventos.")
        return

    
    opcoes = []
    for t in tarefas_usuario:
        opcoes.append(f"{t[1]} (R$ {t[2]:.2f}) - Evento ID {t[3]}")
    opcoes.append("Cancelar")

    print("\n")
    escolha = show_options(opcoes)

    if escolha == len(opcoes):  
        print("Operação cancelada.")
        return

    
    removida = tarefas_usuario.pop(escolha - 1)
    print(f"\nTarefa '{removida[1]}' removida (ID {removida[0]})")

    todas_tarefas = []
    try:
        with open("database/activities.txt", "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(',')
                    id_tarefa = int(partes[0])
                    if id_tarefa != removida[0]:
                        todas_tarefas.append(linha)
    except FileNotFoundError:
        print("Erro ao ler arquivo de tarefas.")
        return
    try:
        with open("database/activities.txt", "w", encoding="utf-8") as f:
            for linha in todas_tarefas:
                f.write(linha + "\n")
        print("Arquivo de tarefas atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar: {e}")
