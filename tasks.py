import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        print("Error: Corrupted JSON file. Starting with empty task list.")
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """Add a new task."""
    title = input("Enter task description: ").strip()

    if not title:
        print("Error: Task description cannot be empty.")
        return

    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def list_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nTask List:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{index}. [{status}] {task['title']}")


def mark_done(tasks):
    """Mark a task as completed."""
    if not tasks:
        print("No tasks to mark.")
        return

    list_tasks(tasks)

    try:
        number = int(input("Enter task number to mark as done: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
