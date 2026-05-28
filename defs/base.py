from defs.user_utils import *
from defs.event_utils import *
from defs.utils import *

def initial_menu():
        show_title("Bem-vindo ao Evenizer")
        opcao = show_options(["Criar Conta", "Entrar", "Sair"])
        
        clear()
        if opcao == 1:
            add_user()
        
        elif opcao == 2:
            email = login()
            if email:
                while True:
                    events_menu(email)
        
        elif opcao == 3:
            quit()

def events_menu(email):
        show_title("Eventos")
        opcao = show_options(["Novo Evento", "Nova Tarefa", "Meus Eventos", "Sair"])
        
        clear()
        if opcao == 1:
            add_event(email)
        
        elif opcao == 2:
            add_tarefa(email)

        elif opcao == 3:
            print("Mostrar eventos do usuário como um menu aqui. A última opção do menu deve ser voltar para o menu anterior.")
        
        elif opcao == 4:
            quit()



