import functions
import time


current_time = time.strftime("%A %d, %Y, %H:%M:%S")
print("Today is: ", current_time)


while True:
    user_action = input("Please Select an Option? 'add', 'show', 'edit', 'complete', 'exit': ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if 'add' in user_action:
        todo = input("Please Enter the ToDo Item you want to add: ") + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

        
    
    elif 'show' in user_action:
        
        todos = functions.get_todos()
        
        for index, items in enumerate(todos):
            items = items.strip('\n')
            print(f"{index + 1}-{items}")
    
    elif 'edit' in user_action:
        try:
            number = int(input("Please Enter the Number of the ToDo you want to edit: "))
            number = number - 1

            todos = functions.get_todos()

            todos[number] = input("Please Enter the new ToDo: ") + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

            
    
    elif 'complete' in user_action:
        try:
            list_item = int(input("PLease enter the number of task you want to remove: "))

            todos = functions.get_todos()
            
            list_item = list_item - 1
            todo_to_remove = todos[list_item].strip('\n')
            todos.pop(list_item)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    
    elif 'exit' in user_action:
        break
    
    else:
        print("The Command is Not valid")

print("Bye!")