def index_exists(list, index):
    return True if 0 <= index < len(list) else False

# table[n] - the number of katas solved at n day

john_table = [0]
ann_table = [1]

def j(n):
    return john_helper(n, john_table)

def john_helper(n, table):
    if index_exists(table, n):
        return table[n]
    else:
        temp = n
        while not index_exists(table, temp):
            temp -= 1
        while temp != n:
            temp += 1
            table.append((temp - a(john_helper(temp-1, john_table))))
        return table[n]
    
def a(n):
    return ann_helper(n, ann_table)

def ann_helper(n, table):
    if index_exists(table, n):
        return table[n]
    else:
        temp = n
        while not index_exists(table, temp):
            temp -= 1
        while temp != n:
            temp += 1
            table.append((temp - j(ann_helper(temp-1, ann_table))))
        return table[n]

def john(n):
    list = []
    while n > 0:
        list.append(j(n-1))
        n -= 1
    list.reverse()
    return list
    
def ann(n):
    list = []
    while n > 0:
        list.append(a(n-1))
        n -= 1
    list.reverse()
    return list
    
def sum_john(n):
    return sum(john(n))
      
def sum_ann(n):
    return sum(ann(n))


print(j(10))
print(john_table)
print(ann_table)