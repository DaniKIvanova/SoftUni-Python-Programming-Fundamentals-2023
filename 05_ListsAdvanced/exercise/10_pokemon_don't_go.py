sequence_of_pokemons = list(map(int, input().split()))
summed_elements = 0
while True:
    indexes = int(input())
    if indexes >= len(sequence_of_pokemons):
        element_for_work = sequence_of_pokemons[-1]
        sequence_of_pokemons[-1] = sequence_of_pokemons[0]
    elif indexes < 0:
        element_for_work = sequence_of_pokemons[0]
        sequence_of_pokemons[0] = sequence_of_pokemons[-1]
    else:
        element_for_work = sequence_of_pokemons[indexes]
        sequence_of_pokemons.pop(indexes)
    for index, pokemon in enumerate(sequence_of_pokemons):
        if element_for_work >= pokemon:
            sequence_of_pokemons[index] += element_for_work
        else:
            sequence_of_pokemons[index] -= element_for_work

    summed_elements += element_for_work
    if len(sequence_of_pokemons) == 0:
        break

print(summed_elements)