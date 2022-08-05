def get_median(elements, i):
    if i % 2 == 1:
        return elements[i // 2]
    else:
        return (elements[i // 2] + elements[(i // 2) - 1]) / 2


def running_median(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        print(get_median(elements, i))
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor

    print(get_median(elements, len(elements)))


if __name__ == "__main__":
    sequence = [2, 1, 5, 7, 2, 0, 5]
    running_median(sequence)
