def bubble_sort(inp):
    for _ in range(len(inp)):
        for j in range(len(inp) - 1):
            if inp[j] > inp[j+1]:
                # easily swap them using property of tuples
                inp[j],inp[j+1] = inp[j+1],inp[j]
    return inp