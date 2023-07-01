array_data = input().split()
command = input().split()

while command[0] != "3:1":
    current_command = command[0]

    if current_command == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(array_data):
            end_index = len(array_data) - 1
        for merging in range(start_index + 1, end_index + 1):
            array_data[start_index] += array_data[merging]
            array_data[merging] = ""

    elif current_command == "divide":
        divided_words = []
        element_for_divide = int(command[1])
        amount_partitions = int(command[2])
        one_partition = len(array_data[element_for_divide]) // amount_partitions
        for parts in range(1, amount_partitions + 1):
            if parts == amount_partitions and len(array_data[element_for_divide]) % amount_partitions != 0:
                divided_words.append(array_data[element_for_divide][::])
            else:
                divided_words.append(array_data[element_for_divide][:one_partition])
                array_data[element_for_divide] = array_data[element_for_divide][one_partition:]
        array_data.pop(element_for_divide)
        for elements in reversed(divided_words):
            array_data.insert(element_for_divide, elements)
    array_data = [x for x in array_data if x != ""]
    command = input().split()

print(" ".join(array_data))