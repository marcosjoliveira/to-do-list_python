#To-do List Projeto
import os, time

def clean(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("----- Options -----\n")
    print("[1] - Show Tasks")
    print("[2] - Add Task")
    print("[3] - Remove Task")
    print("[4] - Close program")
    select = int(input("Enter the value: "))
    return select

def show_tasks():
    with open("task.txt", "r") as files:
        for item in files:
            print(item)

def add_task(task):
    with open("task.txt", "a") as files:
        files.write(task + '\n')

# def remove_task():
#     with open("task.txt", "r+") as files:
#         task = files.readlines()
#         for item in enumerate(task): #remover tarefa
#             print(item)
#         index = int(input("Input the index that you wanna to delete: "))
#         task.pop(index)

#         for item in task: #atualizar a lista
#             with open("task.txt", "w") as file:
#                 file.write(str(task[item]))


while True:    
    
    select = show_menu()

    if select == 1: #mostrar tarefas
        clean()
        show_tasks()
        time.sleep(2.5)
    
    elif select == 2: #adicionar tarefas
        clean()
        add = input("Write the new task: ")
        add_task(add)
        time.sleep(2.5)
        clean()
        print("Updated tasks: ", show_tasks())
        time.sleep(2.5)
    
    # elif select == 3: #remover tarefas
    #     clean()
    #     remove_task()
    
    elif select == 4: #finalizar tarefas
        clean()
        print("Program finished! Thanks for use.")
        break