import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """تحميل المهام من ملف JSON إذا كان موجوداً."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def save_tasks(tasks):
    """حفظ قائمة المهام في ملف JSON."""
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def main():
    print("Welcome to AITaskBot (v2.0)!")
    print("I can now save and load your tasks automatically.")
    
    tasks = load_tasks()
    if tasks:
        print(f"Loaded {len(tasks)} tasks from previous session.")
    
    while True:
        action = input("\nChoose an action: [add, list, quit]: ").lower().strip()
        if action == "add":
            task = input("Enter task name: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"Task '{task}' added and saved successfully!")
            else:
                print("Task name cannot be empty.")
        elif action == "list":
            if not tasks:
                print("\nYour task list is empty.")
            else:
                print("\nYour Current Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif action == "quit":
            print("Goodbye! Your tasks are safe.")
            break
        else:
            print("Invalid action, please try again.")

if __name__ == "__main__":
    main()
