# Evenizer

Evenizer é um gerenciador simples de eventos e tarefas em linha de comando. Ele usa arquivos de texto para armazenar usuários, eventos e atividades.

## Como usar

1. Execute `python app.py` no diretório do projeto.
2. No menu inicial, escolha entre criar conta, entrar ou sair.
3. Após login, use o menu de eventos para criar e gerenciar eventos, tarefas e dados do usuário.

## Menus existentes em `defs/base.py`

| Menu | Opção | Descrição |
|---|---|---|
| `initial_menu` | `Criar Conta` | Cria novo usuário em `database/users.txt`. |
|  | `Entrar` | Faz login com email e senha. |
|  | `Sair` | Encerra o programa. |
| `events_menu` | `Novo Evento` | Cria um novo evento para o usuário logado. |
|  | `Meus Eventos` | Lista eventos do usuário com status de data. |
|  | `Atualizar Evento` | Atualiza dados de um evento existente. |
|  | `Excluir Evento` | Remove um evento. |
|  | `Nova Tarefa` | Cria uma tarefa vinculada a um evento existente. |
|  | `Atualizar tarefa` | Atualiza uma tarefa existente. |
|  | `Excluir Tarefa` | Remove uma tarefa vinculada aos eventos do usuário. |
|  | `Gerenciar Usuário` | Abre o menu de gerenciamento de conta. |
|  | `Sair` | Encerra o programa. |
| `gerencia_user` | `Atualizar Conta` | Atualiza nome e senha do usuário logado. |
|  | `Excluir Conta` | Remove usuário de `database/users.txt`. |
|  | `Suporte` | Exibe informações de suporte. |
|  | `Voltar` | Retorna ao menu anterior. |

## Funções e explicações

### `initial_menu()`
- Exibe o menu inicial.
- Permite criar conta, entrar no sistema ou sair do aplicativo.

### `events_menu(email)`
- Menu principal depois do login.
- Opções para gerenciar eventos, tarefas e usuário.
- Recebe `email` do usuário logado para filtrar eventos e tarefas.

### `gerencia_user(email)`
- Menu de gerenciamento da conta do usuário.
- Permite atualizar ou excluir a conta, ver suporte ou voltar ao menu de eventos.

### Funções de usuário (`defs/user_utils.py`)
- `add_user()`: cria um novo usuário e grava em `database/users.txt`.
- `login()`: valida email e senha no arquivo de usuários.
- `find_me(email)`: busca dados do usuário pelo email.
- `update_user(email)`: atualiza nome e senha do usuário logado.
- `delete_user(email)`: remove o usuário do arquivo.

### Funções de evento (`defs/event_utils.py`)
- `add_event(email)`: cria evento novo com nome, tipo, data, local e orçamento.
- `list_event(email)`: lista eventos do usuário e retorna IDs disponíveis.
- `add_tarefa(id)`: cria tarefa vinculada a um ID de evento.
- `delete_event(email)`: exclui evento do usuário logado.
- `update_tafera()`: altera nome e custo de uma tarefa existente.
- `update_event(email)`: atualiza campos de um evento.
- `delete_atividade(email)`: exclui tarefa associada aos eventos do usuário.

### Funções utilitárias (`defs/utils.py`)
- `clear()`: limpa a tela do terminal.
- `wait(wait_time)`: pausa o programa por alguns segundos.
- `show_title(title, size=30)`: mostra cabeçalho formatado.
- `show_options(options)`: exibe um menu numerado e lê a escolha do usuário.
- `quit()`: sai do programa.
- `gera_id(file)`: gera um ID único para eventos e tarefas.
- `event_date_status(data_str)`: calcula e exibe o status da data do evento.
- `show_error()`: mostra mensagem de erro genérica.
- `help()`: exibe informações de suporte.

## Estrutura de arquivos

- `app.py`: ponto de entrada do aplicativo.
- `defs/base.py`: menus principais e lógica de navegação.
- `defs/user_utils.py`: funções de criação, login, atualização e exclusão de usuário.
- `defs/event_utils.py`: funções de criação, listagem, atualização e exclusão de eventos e atividades.
- `defs/utils.py`: funções auxiliares de interface e manipulação de dados.
- `database/users.txt`: dados dos usuários.
- `database/events.txt`: dados dos eventos.
- `database/activities.txt`: dados das tarefas.

## Execução

Execute no terminal:

```bash
python app.py
```

Siga as instruções exibidas nos menus para usar o software.
