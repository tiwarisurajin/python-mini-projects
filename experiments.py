print("                   To Do List                 ")
print()
print()

task=[]
while True  :
    print("press 'd' to remove task and 's' to stop.")
    add_task = input("Add task : ")
    task.append(add_task)
    
    if add_task == 's'  :
        task.pop()
        break
    
    elif  add_task == 'd' : 
        task.pop()
        remove_task =int(input("Enter the place value to remove the task e.g 1'2'3 : "))
        remove_task2 = remove_task-1
        task.pop(remove_task2)
        print()
        print('Task removed succesfully')
        print()
        

    else:
        print()

    print('Task LIST')
    print()
    for i, t in enumerate(task ,start=1) :
        print(f"{i}. {t}")
    
        
 











