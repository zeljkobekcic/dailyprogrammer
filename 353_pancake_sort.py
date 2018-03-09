import random

def flip(pancakes, position):
    flipped_pancakes = list(reversed(pancakes[:position]))
    not_flipped_pancakes = pancakes[position:]
    return flipped_pancakes + not_flipped_pancakes

def pancake_sort(pancakes):
    number_of_pancakes = len(pancakes)
    number_of_flips = 0
    for left in reversed(list(range(1, number_of_pancakes))):
        biggest_pancake = max(pancakes[0:left+1])
        pancake_index = pancakes[0:left + 1].index(biggest_pancake)

        if pancake_index != 0:
            pancakes = flip(pancakes, pancake_index+1)
            number_of_flips += 1
        pancakes = flip(pancakes, left+1)
        number_of_flips += 1

    return pancakes, number_of_flips

if __name__ == "__main__":
    pancakes = [4, 2, 1, 5, 7, 9, 10, 3, 8, 6]
    print(pancake_sort(pancakes))
    pancakes = [1, 9, 7, 5, 6, 2, 3, 8, 10, 4]
    print(pancake_sort(pancakes))
