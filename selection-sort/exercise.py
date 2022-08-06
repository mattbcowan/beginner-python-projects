from pprint import pprint


def selection_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


# def selection_sort_multi(arr, keys):
#     size = len(arr)

#     for i in range(size - 1):
#         min_index = i
#         for j in range(min_index + 1, size):
#             curr_key_index = 0
#             if arr[j][keys[curr_key_index]] == arr[min_index][keys[curr_key_index]]:
#                 if (
#                     arr[j][keys[curr_key_index + 1]]
#                     < arr[min_index][keys[curr_key_index + 1]]
#                 ):
#                     min_index = j
#             if arr[j][keys[curr_key_index]] < arr[min_index][keys[curr_key_index]]:
#                 min_index = j

#         if i != min_index:
#             arr[i], arr[min_index] = arr[min_index], arr[i]


def selection_sort_multi(arr, keys):
    for key in keys[-1::-1]:
        for x in range(len(arr)):
            min_index = x
            for y in range(x, len(arr)):
                if arr[y][key] < arr[min_index][key]:
                    min_index = y
                if x != min_index:
                    arr[x], arr[min_index] = arr[min_index], arr[x]


if __name__ == "__main__":
    elements = [
        {"First Name": "Raj", "Last Name": "Nayyar"},
        {"First Name": "Suraj", "Last Name": "Sharma"},
        {"First Name": "Karan", "Last Name": "Kumar"},
        {"First Name": "Jade", "Last Name": "Canary"},
        {"First Name": "Raj", "Last Name": "Thakur"},
        {"First Name": "Raj", "Last Name": "Sharma"},
        {"First Name": "Kiran", "Last Name": "Kamla"},
        {"First Name": "Armaan", "Last Name": "Kumar"},
        {"First Name": "Jaya", "Last Name": "Sharma"},
        {"First Name": "Ingrid", "Last Name": "Galore"},
        {"First Name": "Jaya", "Last Name": "Seth"},
        {"First Name": "Armaan", "Last Name": "Dadra"},
        {"First Name": "Ingrid", "Last Name": "Maverick"},
        {"First Name": "Aahana", "Last Name": "Arora"},
    ]
    selection_sort_multi(elements, ["First Name", "Last Name"])

    pprint(elements)
