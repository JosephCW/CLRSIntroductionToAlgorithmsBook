# p.31
def python_merge_sort(list):
    if len(list) > 1:
        mid = len(list)//2
        first_half = list[:mid]
        last_half = list[mid:]

        python_merge_sort(first_half)
        python_merge_sort(last_half)

        index_first_half = 0
        index_last_half = 0
        index_final_array = 0

        while index_first_half < len(first_half) and index_last_half < len(last_half):
            if first_half[index_first_half] <= last_half[index_last_half]:
                list[index_final_array] = first_half[index_first_half]
                index_final_array += 1
                index_first_half += 1
            else:
                list[index_final_array] = last_half[index_last_half]
                index_final_array += 1
                index_last_half += 1

        while index_first_half < len(first_half):
            list[index_final_array] = first_half[index_first_half]
            index_final_array += 1
            index_first_half += 1

        while index_last_half < len(last_half):
            list[index_final_array] = last_half[index_last_half]
            index_final_array += 1
            index_last_half += 1


list_to_sort = [24, 12, 123, 2345, 3567435, 34, 2345, 2, 452, 2, 1234, 1]
python_merge_sort(list_to_sort)
print('list: ' + str(list_to_sort))