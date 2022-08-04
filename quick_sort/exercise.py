def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def quick_sort(arr, lo, hi):
    if lo >= hi or lo < 0:
        return

    # Partition array and get the pivot index
    p = partition(arr, lo, hi)

    # Sort the two partitions
    quick_sort(arr, lo, p - 1)  # Left side of pivot
    quick_sort(arr, p + 1, hi)  # Right side of pivot


def partition(arr, lo, hi):
    # Choose last element as pivot
    pivot = arr[hi]

    # Temporary pivot index
    i = lo - 1

    for j in range(lo, hi):
        # If current element is less than or equal to pivot
        if arr[j] <= pivot:
            # Move the temporary pivot index forward
            i += 1

            # Swap the current element with the element at the temp pivot index
            swap(i, j, arr)

    # Move the pivot element to the correct pivot position (between the smaller and larger elements)
    i += 1
    swap(i, hi, arr)
    return i


if __name__ == "__main__":
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f"sorted array: {elements}")
