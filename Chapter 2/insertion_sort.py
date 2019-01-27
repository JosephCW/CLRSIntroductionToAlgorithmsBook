# p.18
def insertion_sort(array_to_sort):
    if len(array_to_sort) < 2:
        return array_to_sort

    for i in range(1, len(array_to_sort)):
        key = array_to_sort[i]
        # Insert array_to_sort[j] into the sorted sequence array_to_sort[1..j - 1].
        # What the while loop does is move all the values up, overriding the key.
        # We save the key so we can just put the value exactly where we need it at.
        k = i
        while k > 0 and array_to_sort[k - 1] > key:
            array_to_sort[k] = array_to_sort[k - 1]
            k -= 1
        # array_to_sort[i] is less than the key, so I will go after the lower value
        array_to_sort[k] = key

    return array_to_sort


def reverse_insertion_sort(array_to_sort):
    if len(array_to_sort) < 2:
        return array_to_sort

    for i in range(1, len(array_to_sort)):
        key = array_to_sort[i]
        # Insert array_to_sort[j] into the sorted sequence array_to_sort[1..j - 1].
        # What the while loop does is move all the values up, overriding the key.
        # We save the key so we can just put the value exactly where we need it at.
        k = i
        while k > 0 and array_to_sort[k - 1] < key:
            array_to_sort[k] = array_to_sort[k - 1]
            k -= 1
        # array_to_sort[i] is less than the key, so I will go after the lower value
        array_to_sort[k] = key

    return array_to_sort


my_array = [2, 1, 120, 60, 4, 5, 6, 3, 2, 12, 27, 12, 3, 5]
print(insertion_sort(my_array))
print(reverse_insertion_sort(my_array))
