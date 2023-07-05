employee_dict = {}
command = input()

while command != "End":
    company, employee_id = command.split(" -> ")

    if company not in employee_dict.keys():
        employee_dict[company] = []
    if employee_id not in employee_dict[company]:
        employee_dict[company].append(employee_id)
    command = input()

for company, employee_sheet in employee_dict.items():
    print(company)

    for i in employee_sheet:
        print(f"-- {i}")

