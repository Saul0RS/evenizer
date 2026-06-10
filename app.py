from defs.user_utils import *
from defs.event_utils import *
from defs.utils import *
from defs.menus import *

while True:

    show_title("Bem-vindo ao Evenizer")
    opcao = show_options(["Criar Conta", "Entrar", "Suporte", "Sair"])
        
    clear()
    if opcao == 1:
        add_user()
    
    elif opcao == 2:
        email = login()
        if email:
            while True:
                logged_in_menu(email)
    
    elif opcao == 3:
        help()
    
    else:
        quit()