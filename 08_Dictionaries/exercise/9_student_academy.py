trainings_dict = {}
pair_of_rows = int(input())

for _ in range(pair_of_rows):
    student_name, grade = input(), float(input())

    if student_name not in trainings_dict:
        trainings_dict[student_name] = []
    trainings_dict[student_name].append(grade)

for key, value in trainings_dict.items():
    if (sum(value) / len(value)) >= 4.50:
        print(f"{key} -> {(sum(value) / len(value)):.2f}")

