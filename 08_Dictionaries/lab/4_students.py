students = {}
module = ""

while True:
    command = input()
    if ":" in command:
        name, id, lesson = command.split(":")
        if lesson not in students:
            students[lesson] = []
        students[lesson].append(f"{name} - {id}")
    else:
        if "_" in command:
            module = command.replace("_", " ")
            break
        else:
            module = command
            break

print("\n".join(students[module]))
