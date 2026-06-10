# NOTE: treat possible exceptions on call (e.g., FileNotFoundError)
def get_by_filter(path_to_file, filter):
    lines = get_lines(path_to_file)
    for line in lines:
        if filter in line:
            return line
    return None


def get_lines_by_filter(path_to_file, filter):
    lines = get_lines(path_to_file)
    data = []
    for line in lines:
        if filter in line:
            data.append(line)

    return data


# NOTE: treat possible exceptions on call (e.g., FileNotFoundError)
def get_lines(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as file:
        return file.readlines()


def save(path_to_file, data):
    try:
        with open(path_to_file, "a", encoding="utf-8") as file:
            file.write(data)
    except FileNotFoundError:
        print("Erro Interno! Por favor, contate o suporte.")
    except:
        print("Um erro inesperado aconteceu. Isso é tudo que sabemos.")


def delete_line(path_to_file, line_data):
    try:
        lines = get_lines(path_to_file)
        lines.remove(line_data)
        with open(path_to_file, "w", encoding="utf-8") as file:
            file.writelines(lines)

    except ValueError:
        print("Item não encontrado!")
    except FileNotFoundError:
        print("Erro Interno! Contate o suporte.")
    except Exception as e:
        print("Um erro inesperado aconteceu. Isso é tudo que sabemos.")
        # NOTE: comment when in prod
        # print(f"Erro: {e}")


"""
MINI-DOCS:
path_to_file - the name of the file you'll manipulate
filter - something that's unique on the file
new_line - the line that will replace the current line on the file
"""
def update_line(path_to_file, filter, new_line):
    
    try:
        line_to_update = get_by_filter(path_to_file, filter)
        
        if (line_to_update):
            delete_line(path_to_file, line_to_update)
            save(path_to_file, new_line)
        
    except ValueError:
        print("Item não encontrado.")

    except FileNotFoundError:
        print("Erro Interno. Por favor, contate o suporte.")

    except Exception as e:
        print("Um erro inesperado aconteceu. Isso é tudo que sabemos.")
        # NOTE: comment when in prod
        # print(f"Erro: {e}")