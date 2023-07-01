snowballs_number = int(input())
value_snowball = 0
parameters_snowball = ""
for snowball in range(snowballs_number):
    weight_snowball = int(input())
    time_to_target = int(input())
    quality_snowball = int(input())
    if (weight_snowball / time_to_target) ** quality_snowball > value_snowball:
        value_snowball = (weight_snowball / time_to_target) ** quality_snowball
        parameters_snowball = f"{weight_snowball} : {time_to_target} = {int(value_snowball)} ({quality_snowball})"
print(parameters_snowball)