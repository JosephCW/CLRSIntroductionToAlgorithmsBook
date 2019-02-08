def merge_sort(l):
    n = len(l)
    if n == 1 or n == 0:
        return l
    mid = n // 2
    first_half = merge_sort(l[:mid])
    second_half = merge_sort(l[mid:])
    return merge(first_half, second_half)


def merge(l1, l2):
    merged = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    merged.extend(l1[i:])
    merged.extend(l2[j:])
    return merged


print(str(merge_sort([1, 5, 6, 3, 12, 27, 1, 18, 25, 25, 1, 3, 4, 5, 19])))
