from datetime import datetime
from utils import show_options, show_title

def add_event(email):
    show_title("Novo Evento")
    nome = input("Digite o nome do evento: ")
    tipo = show_options(["Aniversário", "Casamento", "Reunião", "Formatura", "Festa de empresa", "Outro"])

    while True:
        try:
            data = input("Digite a data do evento (Ex: 09/12/2006): ")
            datetime.strptime(data, "%d/%m/%Y")
        except Exception as e:
            print(f"Data inválida. Tente novamente: {e}")
            continue
        break

    local = input("Digite o local do evento: ") 
    orçamento = float(input("Digite o orçamento do evento: "))

    with open("database/events.txt", "a+") as file: # ponteiro do arquivo começa no final pq abriu como "a"    
        file.seek(0)
        if f"\"nome\": \"{nome}\", \"data\": \"{data}\", \"local\": \"{local}\"" not in file.read(): # ler o arquivo e faz o ponteiro voltar para o final, para ai sim acrescentar a informação
            file.write(f"\"nome\": \"{nome}\", \"tipo\": \"{tipo}\", \"data\": \"{data}\", \"local\": \"{local}\", \"orçamento\": \"{orçamento}\", \"emailuser\": \"{email}\"\n")
            print("Evento cadastrado com sucesso !!!")                      

        else: 
            print("O evento não pode ocorrer no mesmo lugar, ao mesmo tempo e no mesmo dia que outro evento !!! tente novamente !!!")
