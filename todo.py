
from os import system
# CRUD / BREAD





tasks = []  # empty list
# MAIN LOOP ###################

while True:
    system ("clear")
    print('MENU')
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Change Task")
    print("5. Swap Task A with Task B")
    print("0. Exit")
    option = int(input(">>>> "))
    if option ==1:
        system ("clear")
        # ADD a new task to the list
        while True:
            new_task = input('Name your next task:')
            if new_task == "":
                break
            if new_task not in tasks:
                tasks.append( new_task )

    if option == 2:
        system ("clear")
        ############ PRINT TASKS #################
        print ("\nYour tasks: ")

        for i in range(len(tasks)):
            print(i+1, " >>> ", tasks[i])
        
        input("Hit ENTER to continue: ")

############################ REMOVE A TASK ####################################       
# HW1  p 3 ask for the index -> remove / python list metods
#     * print the task title / confirm yes/no ?
    if option == 3:
        system("clear")
        while True:
            index = int(input("Enter the task number you want to delete :")) - 1
            print("Show task to remove >>>", tasks[index])
            i = input("Write YES/NO to remove the indicated task:") 
            if i == "YES":
                tasks.pop(index)
                input("Hit ENTER to Exit: ")
                break
            if i == "NO":
                break
            


    if option == 4:
        system("clear")
        #EDIt A TASK #######
        index = int(input("Enter task position: ")) - 1
        new_task = input ("Enter new task title: ")
        tasks[index] = new_task

 ######## HW 2 "option 5" ---- Swap Task 1 with task 2 -> Index 1, Index 2 #############
    if option == 5:
        system("clear")
        task1 =int(input("Enter number Task 1: "))
        print(tasks[task1-1])
        task2 =int (input("Enter number Task 2: "))
        print(tasks[task2-1])
        tasks[task1-1], tasks[task2-1] = tasks[task2-1], tasks[task1-1] 
            
    if option == 0:
        break







