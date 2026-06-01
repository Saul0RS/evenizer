def update_event(email):
    
    arquivo = open("database/events.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    
    eventos = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            eventos.append(eval(linha))
    
    
    for i in range(len(eventos)):
        print(f"{i+1}. {eventos[i]['name']} - {eventos[i]['date']}")
    
    
    escolha = int(input("Número para editar: ")) - 1
    evento = eventos[escolha]
    
    
    evento['name'] = input(f"Novo nome ({evento['name']}): ") or evento['name']
    evento['date'] = input(f"Nova data ({evento['date']}): ") or evento['date']
    evento['location'] = input(f"Novo local ({evento['location']}): ") or evento['location']
    evento['budget'] = float(input(f"Novo orçamento ({evento['budget']}): ") or evento['budget'])
    evento['type'] = int(input(f"Novo tipo (1-Aniv,2-Casam,3-Reun,4-Outro) ({evento['type']}): ") or evento['type'])
    
    
    arquivo = open("database/events.txt", "w")
    for ev in eventos:
        arquivo.write(str(ev) + "\n")
    arquivo.close()
    
    print("Evento atualizado!")
