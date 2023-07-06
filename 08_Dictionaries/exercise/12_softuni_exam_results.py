data = input()
name_points = {}
language_counter = {}
banned = False

while data != "exam finished":

    if "banned" in data:
        user, action = data.split("-")

        for k in name_points.keys():
            if user in k:
                banned = True

        if banned:
            name_points.pop(k)
        banned = False

    else:
        student, language, points = data.split("-")
        points = int(points)

        if student in name_points.keys():
            language_counter[language] += 1

            if points > name_points[student][1]:
                name_points[student][1] = points

        else:
            name_points[student] = [language, points]

            if language in language_counter:
                language_counter[language] += 1

            else:
                language_counter[language] = 1

    data = input()

print("Results:")

for k, v in name_points.items():
    print(f"{k} | {v[1]}")
print("Submissions:")

for k, v in language_counter.items():
    print(f"{k} - {v}")

