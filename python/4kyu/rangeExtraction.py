def has_next(num1, num2):
    return True if num1 + 1 == num2 else False

def solution(args):
    result = ''
    finish = '' 
    start = args[0]
    for i in range (len(args)-1):
        if has_next(args[i], args[i+1]):
            if args[-1] == args[i+1]: 
                if start + 1 == args[-1]: result += str(start) + ',' + str(args[-1])
                else: result += str(start) + '-' + str(args[-1])
            continue
        else:
            finish = args[i]
            if start == finish:
                result += str(start) + ','
            elif start + 1 == finish:
                result += str(start) + ',' + str(finish) +  ','
            else:
                result += str(start) + '-' + str(finish) + ','
            start = args[i+1]
            if start == args[-1]:
                result += str(start)
        
    return result

print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))