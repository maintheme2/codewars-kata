def is_valid(opening, closing):
    flag = False
    if len(opening) == len(closing):
        for i in range(len(opening)):
            for j in range(len(closing)):
                if i == j:
                    flag = True if closing[i] > opening[i] else False
                else:
                    continue
            if flag == False: break
    return flag

def valid_parentheses(string):
    if string == "":
        return True
    opening_pars_indices, closing_pars_indices = [], []
    for i in range(len(string)):
        if string[i] == "(":
            opening_pars_indices.append(i)
        elif string[i] == ")":
            closing_pars_indices.append(i)
    return is_valid(opening_pars_indices, closing_pars_indices)

print(valid_parentheses("hi(hi)()"))