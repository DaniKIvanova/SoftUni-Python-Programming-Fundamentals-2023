initial_schedule = input().split(", ")
course_start = False

while not course_start:
    list_commands = input()
    if list_commands == "course start":
        course_start = True
        break

    list_commands = list_commands.split(":")
    current_command = list_commands[0]
    if current_command == "Add":
        lesson = list_commands[1]
        if lesson not in initial_schedule:
            initial_schedule.append(lesson)
    elif current_command == "Insert":
        lesson = list_commands[1]
        index_for_insert = int(list_commands[2])
        if lesson not in initial_schedule:
            initial_schedule.insert(index_for_insert, lesson)
    elif current_command == "Remove":
        lesson = list_commands[1]
        if lesson in initial_schedule:
            initial_schedule.remove(lesson)
        if lesson + "-Exercise" in initial_schedule:
            initial_schedule.remove(lesson + "-Exercise")
    elif current_command == "Swap":
        lesson = list_commands[1]
        second_lesson = list_commands[2]
        if lesson in initial_schedule and second_lesson in initial_schedule:
            first_index_for_swap = initial_schedule.index(lesson)
            second_index_for_swap = initial_schedule.index(second_lesson)
            initial_schedule[first_index_for_swap], initial_schedule[second_index_for_swap] = \
                initial_schedule[second_index_for_swap], initial_schedule[first_index_for_swap]
            if lesson + "-Exercise" in initial_schedule:
                initial_schedule.remove(lesson + "-Exercise")
                initial_schedule.insert(second_index_for_swap + 1, lesson + "-Exercise")
            if second_lesson + "-Exercise" in initial_schedule:
                initial_schedule.remove(second_lesson + "-Exercise")
                initial_schedule.insert(first_index_for_swap + 1, second_lesson + "-Exercise")
    elif current_command == "Exercise":
        lesson = list_commands[1]
        if lesson not in initial_schedule:
            initial_schedule.append(lesson)
            initial_schedule.append(lesson + "-Exercise")
        elif lesson + "-Exercise" not in initial_schedule:
            index_for_exercise = initial_schedule.index(lesson)
            initial_schedule.insert(index_for_exercise + 1, lesson + "-Exercise")

number_of_lesson = 1
for schedule in initial_schedule:
    print(f"{number_of_lesson}.{schedule}")
    number_of_lesson += 1