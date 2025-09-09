import modules

my_tasks = modules.load_tasks()


def menu():
    print("======================")
    print("GERENCIADOR DE TAREFAS")
    print("======================")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Remover tarefa")
    print("4. Sair")
    print("======================")


while True:
    menu()

    try:
        option = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite uma opção válida!")
        continue

    if option == 1:
        new_task = input("Nova tarefa: ")
        modules.add_tasks(my_tasks, new_task)
        print("Tarefa adicionada com sucesso!")
    elif option == 2:
        modules.view_tasks(my_tasks)
    elif option == 3:
        try:
            i = int(input("Digite o número da tarefa a ser removida: "))
            modules.remove_tasks(my_tasks, i)
        except ValueError:
            print("Digite um número válido!")
    elif option == 4:
        print("Adeus!")
        break
    else:
        ("Opção inválida. Escolha um número de 1 a 4.")
