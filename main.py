from todo_manager import *
def show_menu():
    print("====================")
    print("TO DO LIST")
    print("====================")
    print("1. Add Task ")
    print("2. View Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("--------------------")


if __name__== "__main__":
    while True:  # keep showing menu until user exits
        show_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("⚠ Invalid input, please enter a number 1-5.")
            continue
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_task_completed()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice, try again!")
