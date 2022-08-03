def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_number + 1
        else:
            right_index = mid_number - 1

    return -1


def binary_search_all_occurrences(numbers_list, number_to_find):
    find_index = binary_search(numbers_list, number_to_find)
    prev_index = find_index - 1
    all_occurrences = []

    if find_index == -1:
        return -1

    if numbers_list[prev_index] == number_to_find:
        while numbers_list[prev_index] == number_to_find:
            all_occurrences.insert(0, prev_index)
            prev_index -= 1

    while numbers_list[find_index] == number_to_find:
        all_occurrences.append(find_index)
        find_index += 1

    return all_occurrences


# Find index of all occurrences of a number in a sorted list
numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
number_to_find = 15

print(binary_search_all_occurrences(numbers, number_to_find))
