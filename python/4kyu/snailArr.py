def snail(snail_map):
    if not snail_map:
        return []
    return list(snail_map[0]) + snail(list(zip(*snail_map[1:]))[::-1])

print(snail([[1,2,3], 
             [4,5,6], 
             [7,8,9]]))