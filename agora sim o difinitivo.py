from datetime import datetime
def update_event(email):
    eventos = []
    try:
        arq = open("database/events.txt" , "r", encoding="utf-8")
        colunas = arq.readlines()
        arq.close()
    finally:
        if arq is None:
            print('deu erro kkkkkkk')
    
        for linhas in colunas:
         if colunas:
                separa = linhas.split(',')
                id_evento = int(separa[0]),
                nome = [separa[1]]  
                tipo = int(separa[2]) 
                data = int(separa[3]) 
                local = (separa[4]) 
                orcamento = float(separa[5]) 
                email_dono = separa[6].strip()
                eventos.append([id_evento, nome, tipo, data, local, orcamento, email_dono])
   
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

    evento = eventos[escolha]

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
