'''
Created on Nov 9, 2017

@author: Mark
'''
def num_matches(list1, list2):
    """returns the number of elements that the two lists have in common"""
    list1.sort()
    list2.sort()
    if list1 == [] or list2 == []:
        return 0
    if list1[0] == list2[0]:
        return 1 + num_matches(list1[1:], list2[1:])
    if list1[0] < list2[0]:
        return num_matches(list1[1:], list2)
    if list1[0] > list2[0]:
        return num_matches(list1, list2[1:])
    
def num_matches_loop(list1, list2):
    list1.sort()
    list2.sort()
    matches = i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def keep_matches(list1, list2):
    """returns a list of the elements that the two lists have in common"""
    list1.sort()
    list2.sort()
    matches = i = j = 0
    lst = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            lst.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return (matches, lst)

def drop_matches(list1, list2):
    """returns a list of the elements that the two lists have in common"""
    list1.sort()
    list2.sort()
    matches = i = j = 0
    lst = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            lst.append(list1[i])
            i += 1
        else:
            lst.append(list2[j])
            j += 1
    while i < len(list1):
        lst.append(list1[i])
        i += 1
    while j < len(list2):
        lst.append(list2[j])
        j += 1
    return lst
        
print(drop_matches(['b', 'c', 'd', 'e', 'f', 'k'], ['b', 'd', 'f', 'g', 'h', 'i', 'k']))    