# p.29
def selection_sort(array_to_sort):
    if len(array_to_sort) < 2:
        return array_to_sort

    for i in range(0, len(array_to_sort)):
        minPosition = i
        for j in range (i, len(array_to_sort)):
            if array_to_sort[j] < array_to_sort[minPosition]:
                minPosition = j

        array_to_sort[minPosition], array_to_sort[i] = array_to_sort[i], array_to_sort[minPosition]
    return


array_to_sort = [23, 134, 14, 45, 62, 1, 2, 4, 5, 7, 345, 128]
selection_sort(array_to_sort)
print(array_to_sort)
