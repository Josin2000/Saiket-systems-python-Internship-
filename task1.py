class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "**done**" if self.completed else "!pending!"
        return f"[{status}] {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")


def main():
    todo_list = ToDoList()

    while True:
        print("\n######## TO-DO LIST #########")
        print("\n-----------------------------")
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_task_as_completed(index)
        elif choice == "3":
            print("\n--- Tasks ---")
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()



