a = [20, 35, -15, 7, 55, 1, -22]


def shell_short(a):
    arr_len = len(a)
    gap = arr_len / 2
    for i in range(gap, 0, -1):
        print gap
        i = gap / 2
        gap = gap / 2
        if gap <= 0:
            break
        for j in range(gap, arr_len):
            new_element = a[j]
            k = j
            while(k >= gap and a[k - gap] > new_element):
                a[k] = a[k - gap]
                k -= gap
            a[k] = new_element
    print a

shell_short(a)
