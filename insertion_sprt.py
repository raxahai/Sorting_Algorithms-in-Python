def insertion_sort(inp):
    for i in range(len(inp) - 1):
        j = i
        while j >= 1 and inp[j-1] > inp[j]:
            inp[j-1],inp[j] = inp[j],inp[j-1]
            j = j - 1
    return inp