from defs.utils import show_title, show_message, gera_id
from defs.file_utils import get_lines_by_filter, get_by_filter

ACTIVITIES_FILE_PATH = "database/activities.txt"
EVENTS_FILE_PATH = "database/events.txt"

def add_tarefa(id):
    while True:
        opcao = input("Digite o ID do evento que voce deseja criar a tarefa: ")
        if opcao in id:
            event_id = opcao
            break
        else:
            print("Opção incorreta")

    show_title("Nova tarefa")  

    opt = input("Sem ideias para atividades? Pressione 1 para sugestões.")
    if opt == 1:
        event = get_by_filter(EVENTS_FILE_PATH, event_id)
        event_type = int(event.split(",")[2])
        number_of_guests = int(event.split(",")[5])
        suggestions = activities_suggestion(event_type, number_of_guests)
    
        if (type(suggestions) == dict):
            for key, value in suggestions.items():
                print(f"{key}: {', '.join(value)}")

        else:
            print(", ".join(suggestions))
    

    with open(ACTIVITIES_FILE_PATH, "a+") as file:   
        id = gera_id(file)
        
        nome = input("Digite o nome da tarefa: ")
        try:
            custo = float(input("Digite o custo do evento: "))

        except (ValueError, TypeError):
            show_message()
            return
        
        file.write(f"{id},{nome},{custo},{event_id}\n")
        show_message(f"Tarefa {nome} cadastrada com sucesso.")


def list_activities(event_id):

    activities = get_lines_by_filter(ACTIVITIES_FILE_PATH, event_id)

    for activity in activities:
        id, nome, custo, event_id = activity.split(",")
        print(f"ID: {id}, Nome: {nome}, Custo: {custo}, ID Evento: {event_id}")


def activities_suggestion(event_type, number_of_guests):

    # Aniversário
    if event_type == 1:
        if number_of_guests <= 20:
            return {
                "Kids/Teens": ["Pinhata", "Dança da Cadeira", "Pula Pirata", "Twister"], 
                "Adultos": ["Verdade ou Pinga", "Pula Pirata com Taser"],
                "Geral": ["Impostor", "Stop", "Dixit", "Abertura dos Presentes", "Música ao vivo", "Competição de Dança"]
            }
        elif number_of_guests > 20:
            return {
                "Kids/Teens": ["Pega-pega", "Esconde-Esconde", "Anão-Gigante/Morto-Vivo", "Dança da Cadeira"],
                "Adultos": ["Verdade ou Pinga", "Brincadeira do ai", "repetição de palavras com vodka"],
                "Geral": ["Impostor", "Stop", "Dixit", "Abertura dos Presentes", "Música ao vivo", "Competição de Dança"]
            }
    
    # Casamento
    if event_type == 2:
        return {
            "Kids/Teens": ["Stop/Adedonha", "Amarelinha", "Comer bolo sem usar as mãos", "Dança das Cadeiras"],
            "Adultos": ["Pega Buquê", "Roda de Fofoca", "Dança", "Abertura dos Presentes"],
            "Geral": ["Música ao vivo", "Brincadeiras com os noivos", "Dança dos Noivos"]
        }
    
    # Reunião
    if event_type == 3:
        return ["Tomar café", "Fofocar", "Estudar até cair", "Marcar outra reunião", "Apresentação de Slides"]
    
    # Outro
    if event_type == 4:
        return ["Tomar café", "Fofocar", "Pula Pirata", "Estudar até cair", "Música ao vivo"]