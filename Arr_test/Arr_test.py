from timeit import default_timer as timer


def most_efficient_search_algorithm(l1, n, num, pos=0):
    if pos != n-1 and l1[pos] != num:
        pos = pos + 1
        res = most_efficient_search_algorithm(l1, n, num, pos)
    elif num == l1[pos]:
        res = pos
    else:
        res = -1
    return res


l1 = [1, 4, 6, 2, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
start_t = timer()
a = most_efficient_search_algorithm(l1, 24, 25)
print(a)
end_t = timer()
time = end_t - start_t
print(f'{time:.7f}')
