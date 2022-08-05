def is_odd(num):
    return 0 if num % 2 == 0 else 1

def add_for_odd(list, size):
    temp = 2
    squared = size*size
    list.append(squared)
    while (len(list) != size):
        list.append(squared + temp)
        list.append(squared - temp)
        temp += 2

def add_for_even(list, size):
    temp = 1
    squared = size*size
    while (len(list) != size):
        list.append(squared + temp)
        list.append(squared - temp)
        temp += 2

def odd_row(n):
    lst = []
    add_for_odd(lst, n) if is_odd(n) else add_for_even(lst, n)
    return sorted(lst)