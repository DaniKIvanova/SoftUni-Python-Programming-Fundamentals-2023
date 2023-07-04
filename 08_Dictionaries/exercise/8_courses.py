courses = {}

while True:
    command = input()

    if command == "end":
        break

    course, student = command.split(" : ")

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for key, value in courses.items():
    print(f"{key}: {len(value)}")

    for i in range(len(value)):
        print(f"-- {value[i]}")

