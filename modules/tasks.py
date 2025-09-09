import json


def load_tasks():
    try:
        with open("script.txt", "r") as file:
            content = file.read()
            return json.loads(content)
    except:
        return []


def save_tasks(tasks):
    with open("script.txt", "w") as file:
        file.write(json.dumps(tasks))


def add_tasks(tasks, new_task):
    tasks.append(new_task)
    load_tasks()


def view_tasks(tasks, i):
    try:
        tasks.pop(i)
        load_tasks()
    except IndexError:
        return "Índice Inválido"
