import json

script = "script.txt"


def load_tasks():
    try:
        with open(script, "r") as file:
            content = file.read()
            return json.loads(content)
    except:
        return []


def save_tasks(tasks):
    with open("script.txt", "w") as file:
        file.write(json.dumps(tasks))


def add_tasks(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)


def remove_tasks(tasks, i):
    try:
        removed = tasks.pop(i)
        save_tasks(tasks)
        return f"Tarefa rremovida: {removed}"
    except IndexError:
        return "Índice Inválido"


def view_tasks(tasks):
    if not tasks:
        return "Nenhuma tarefa encontrada."
    return "\n".join(f"{i}. {task}" for i, task in enumerate(tasks))
