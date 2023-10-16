def task_manager() -> None:
    count = int(input("How many tasks should i handle?:"))
    tasks = [input(f"What's task number {i+1}?: ") for i in range(count)]

    print(f"I'm managing these tasks: {tasks}")


if __name__ == "__main__":
    task_manager()
