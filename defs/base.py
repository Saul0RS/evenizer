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
        opcao = show_options(["Novo Evento", "Meus Eventos", "Atualizar Evento", "Excluir Evento", "Nova Tarefa", "Atualizar tarefa", "Excluir Tarefa", "Gerenciar Usuário", "Sair"])
        
        clear()
        if opcao == 1:
            add_event(email)
        
        elif opcao == 2:
            list_event(email)

        elif opcao == 3:
            update_event(email)
        
        elif opcao == 4:
            delete_event(email)
        
        elif opcao == 5:
            id = list_event(email)
            add_tarefa(id)

        elif opcao == 6:
            update_tafera()

        elif opcao == 7:
            delete_atividade(email)

        elif opcao == 8:
            gerencia_user(email)

        elif opcao == 9:
            quit()


def gerencia_user(email):
        show_title("Gerenciar Conta")
        opcao = show_options(["Atualizar Conta", "Excluir Conta", "Suporte", "Voltar"])

        clear()
        if opcao == 1:
            update_user(email)

        elif opcao == 2:
            delete_user(email)

        elif opcao == 3:
            help()

        elif opcao == 4:
            return



