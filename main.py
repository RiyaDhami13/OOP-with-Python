# Initialize an empty to-do list
to_do_list = []

# Function to display to-do list
def show_list():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            status = "Done" if task['completed'] else "Yet to Complete"
            print(f"{index}. {task['task']} - {status}")

# Function to add a task to the to-do list
def add_task(task):
    to_do_list.append({"task": task, "completed": False})
    print(f"Added task: {task}")

# Function to mark a task as completed
def mark_task_completed(task_number):
    if 0 < task_number <= len(to_do_list):
        to_do_list[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(task_number):
    if 0 < task_number <= len(to_do_list):
        removed_task = to_do_list.pop(task_number - 1)
        print(f"Deleted task: {removed_task['task']}")
    else:
        print("Invalid task number.")

# Main loop for the interaction
while True:
    print("\nOptions:")
    print("1. Show To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_list()
    elif choice == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "3":
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_task_completed(task_number)
    elif choice == "4":
        task_number = int(input("Enter the task number to delete: "))
        delete_task(task_number)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

