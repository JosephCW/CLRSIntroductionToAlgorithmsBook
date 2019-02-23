
length_values = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def rod_cut(length_values, the_rod):
    # i is the length of rod
    # r is the optimal value of a rod of lengh i
    # s is the length to cut off to get the optimal result
    i = [n for n in range(0, the_rod + 1)]
    r = [None] * (the_rod + 1)
    s = [None] * (the_rod + 1)
    # The value of a length 0 rod is always zero
    r[0] = 0
    s[0] = 0
    
    for length in range(1, the_rod + 1):
        best = -999999
        for i in range(1, length + 1):
            if best < length_values[i] + r[length - i]:
                best = length_values[i] + r[length - i]
                s[length] = i
        r[length] = best
    return r, s


def print_solution(r, s, n):
    print('total sale price for rod of length ' + str(n) + ': ', r[n])
    while (n > 0):
        print('cut ', s[n])
        n-= s[n]


def main():
    r, s = rod_cut(length_values, 3)
    print_solution(r, s, 3)

    r, s = rod_cut(length_values, 7)
    print_solution(r, s, 7)

    r, s = rod_cut(length_values, 8)
    print_solution(r, s, 8)

    r, s = rod_cut(length_values, 10)
    print_solution(r, s, 10)


if __name__ == '__main__':
    main()

