from storage import load_tasks,save_tasks

def add_task():
    """Add a new task to the to-do list."""
    tasks= load_tasks()
    tasks_name=input("Enter task description:")
    priority = input("Enter priority (Low/Medium/High):")
    deadline = input("Enter deadline (YYYY-MM-DD or leave blank):")

    new_id = max([task["id"] for task in tasks],default=0)+1
    new_task={
        "id":new_id,
        "task":tasks_name,
        "completed":False,
        "priority":priority,
        "deadline":deadline if deadline else None
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task {tasks_name} added successfully!")


    


def view_tasks():
    """Display all tasks in the to-do list."""
    tasks=load_tasks()
    if not tasks:
        print("no Tasks found!!")
        return
    print("\nYour Tasks:")
    print("ID | Task | Status | Priority | Deadline")
    print("-"*50)
    for task in tasks:
        status = "completed" if task["completed"] else "not completed"
        print(f"{task["id"]} | {task["task"]} | {status} | {task["priority"]} | {task["deadline"]}")

    


def mark_task_completed():
    """Mark a specific task as completed."""
    tasks=load_tasks()
    task_id= int(input("Enter task id to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task {task["task"]} marked as completed.")
            return
    print("task not found.")


def delete_task():
    """Delete a specific task from the to-do list."""
    tasks=load_tasks()
    task_id = int(input("Enter task ID to delete: "))
    updated_tasks = [task for task in tasks if task["id"]!= task_id]

    if len(updated_tasks) == len(tasks):
        print("task not found.")
    else:
        save_tasks(updated_tasks)
        print(f"Task{task_id} deleted successfully.")
