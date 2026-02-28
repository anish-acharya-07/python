#add task
#remove task
#modify task
#view task

TASKS = []


def add_task(TASKS) :
    
    print("\n-------ADD TASK-------\n")

    while True :

        TASKS.append(input("enter task to add : "))

        print("\nadding tasks..")
        print("task added sucessfully \n")
        
        user_choice_to_add_task = input("do you want to add another task ? (y/n) : ")

        if user_choice_to_add_task.lower() != "y" :

            user_choice_to_view_task = input("wanna view the added tasks ? (y/n) : ")

            if user_choice_to_view_task.lower() != "y" :
                break
            
            else :
                view_task(TASKS)

            break

        


    print("\n----------------------")




def remove_task() :
    print("\n-------REMOVE TASK-------\n")
    
    view_task(TASKS)


    



    print("\n----------------------")     


def modify_task() :
    pass

def view_task(TASKS) :

    if not TASKS :
        print("no task to display\n")

    else :
        print("\n-------VIEW TASK-------\n")

        print("TASKS : ")
        for i in range(len(TASKS)) :
            print(f"{i+1}. {TASKS[i]}")

    print("\n----------------------\n")


def main(TASKS) :
        
    print("\n**********WELCOME TO TASK MANAGER**********\n")

    while True :
            
        print("what would you like to do ? \n" \
        "1. add task \n" \
        "2. remove task \n" \
        "3. modify task \n" \
        "4. view task \n")

        user_choice = input("enter your choice ( 1 , 2 , 3 , 4 ) : ")
        
        if user_choice == "1" :
            add_task(TASKS)

        elif user_choice == "2" :
            remove_task(TASKS)

        elif user_choice == "3" :
            pass

        elif user_choice == "4" :
            view_task(TASKS)

        else :
            pass


        end_or_continue = input("do you want to continue this program ? (y/n) : ").lower()

        if end_or_continue != "y" :
            print("exiting....")
            break


if __name__ == "__main__" :
     main(TASKS)
     