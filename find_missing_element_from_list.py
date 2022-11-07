"""find missing element from list with less time complexity"""


def has_missing_element(l):
    if l[-1] - l[0] + 1 == len(l):
        return False
    return True


def get_missing(l):
    if len(l) < 3:
        missing_element = l[0]+1
        return missing_element
    if not has_missing_element(l):
        return 'No missing element'
    half = len(l)//2
    l1 = l[:half]
    l2 = l[half:]
    if not has_missing_element(l1) and not has_missing_element(l2):
        missing_element = l1[-1] + 1
        return missing_element
    if has_missing_element(l1):
        return get_missing(l1)
    else:
        return get_missing(l2)


'''create list'''
l = [x for x in range(4, 1000)]

'''delete 77'''
del l[77]

print(get_missing(l))
