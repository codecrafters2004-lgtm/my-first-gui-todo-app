import functions
# pyrefly: ignore[missing-import]
import FreeSimpleGUI as sg


label = sg.Text("Please Enter a Todo")
input_box = sg.InputText(tooltip="Enter a Todo", key='Todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="Todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button], [list_box, edit_button], [complete_button, exit_button]], font=('Helvetica', 20))


while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['Todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['Todos'].update(values=todos)
            window['Todo'].update(value='')
        
        case 'Edit':
            todo_to_edit = values['Todos'][0]
            new_todo = values['Todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['Todos'].update(values=todos)

        case 'Complete':
            todo_to_complete = values['Todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['Todos'].update(values=todos)
            window['Todo'].update(value='')
        
        case 'Exit':
            break

        case 'Todos':
            window['Todo'].update(value=values['Todos'][0])

        case sg.WIN_CLOSED:
            break



window.close()