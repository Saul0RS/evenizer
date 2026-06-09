from defs.utils import show_title, show_options

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
