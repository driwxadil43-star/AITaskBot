def main():
    print("Welcome to AITaskBot!")
    print("I am a simple AI assistant to help you manage tasks.")
    
    tasks = []
    while True:
        action = input("\nChoose an action: [add, list, quit]: ").lower()
        if action == "add":
            task = input("Enter task name: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")
        elif action == "list":
            print("\nYour Current Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action, please try again.")

if __name__ == "__main__":
    main()
