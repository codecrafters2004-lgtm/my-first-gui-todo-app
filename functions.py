filepath = 'todos.txt'

def get_todos(filepath=filepath):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
        return todos_local

def write_todos(todos, filepath=filepath):
    with open(filepath, 'w') as file:
            file.writelines(todos)

    
