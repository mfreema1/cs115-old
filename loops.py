import sys
def mapSqr(L):
    M = []
    for item in L:
        M.append(item * item)
    return M
print(mapSqr([2, 4, 6]))

def maximumFor(L):
    if L == []:
        return None
    result = L[0]
    for item in L:
        if result < item:
            result = item
    return result

def find_min_max(lst):
    if lst == [0]:
        return None
    max_val = min_val = lst[0]
    for x in lst:
        if min_val > x:
            min_val = x
        elif max_val < x:
            max_val = x
    return (min_val, max_val)

def sequential_search(lst, key):
    i = 0
    for x in lst:
        if key == x:
            return i
        i += 1
    return -1

print(find_min_max([1, 4, 5, 62, 6]))
print(sequential_search([], 5))