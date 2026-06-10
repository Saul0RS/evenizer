from defs.user_utils import *
from defs.event_utils import *
from defs.utils import *

def events_menu(email):
        show_title("EVENTOS")
        opcao = show_options(["Novo Evento", "Meus Eventos", "Voltar"])
        
        clear()
        if opcao == 1:
            add_event(email)
        
        elif opcao == 2:
            list_events(email)
        
        else:
            logged_in_menu(email)


def logged_in_menu(email):
    show_title("HOME")
    opcao = show_options(["Eventos", "Perfil", "Suporte", "Sair"])

    if opcao == 1:
        events_menu(email)

    elif opcao == 2:
        profile(email)

    elif opcao == 3:
        help()

    else:
        quit()