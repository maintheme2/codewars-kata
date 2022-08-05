def next_smaller(n):
    digits = [int(x) for x in str(n)]
    if len(digits) == 1 or sorted(digits) == digits:
        return -1
    else:
        for i in range(len(digits)-1,0,-1) :
            if digits[i-1] > digits[i]:
                pos_x = i - 1
                x = digits[i-1]
                break
        pre_max = -1
        for i in range(pos_x, len(digits)):
            if pre_max < digits[i] and x > digits[i]:
                pre_max = digits[i]
                pos_y = i
        y = pre_max
        digits[pos_x], digits[pos_y] = digits[pos_y], digits[pos_x]
        right_part = [digits[i] for i in range(pos_x + 1, len(digits))]
        left_part = [digits[i] for i in range(0, pos_x + 1)]
        right_part.sort(reverse=1)
        digits = left_part + right_part
        res = ''.join(map(str,digits))
        return int(res)  if res[0] != '0' else -1

str = next_smaller(123456789)
print(str)
      
# 1262347
# x = 6, y = 4(to the right of x and the biggest but smaller than x) 
# swap x,y
# sort in descending everything to the right of y