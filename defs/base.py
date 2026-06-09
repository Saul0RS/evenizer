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
        opcao = show_options(["Novo Evento", "Nova Tarefa", "Meus Eventos","Atualizar Evento", "Excluir Evento" ,"Sair"])
        
        clear()
        if opcao == 1:
            add_event(email)
        
        elif opcao == 2:
            id = list_event(email)
            add_tarefa(id)

        elif opcao == 3:
            list_event(email)

        elif opcao == 4:
            update_event(email)
        
        elif opcao == 5:
            delete_event(email)
        elif opcao == 6:
            quit()



