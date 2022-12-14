def parse_int(string):
    table = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4,
    "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9,
    "ten" : 10, "eleven" : 11, "twelve" : 12, "thirteen" : 13, "fourteen" : 14,
    "fifteen" : 15, "sixteen" : 16, "seventeen" : 17, "eighteen" : 18, 
    "nineteen" : 19, "twenty" : 20, "thirty" : 30, "forty" : 40, 
    "fifty" : 50, "sixty" : 60, "seventy"  : 70, "eighty" : 80, "ninety" : 90}

    multipliers = {"hundred" : 100, "hundreds" : 100,
    "thousands" : 1000, "thousand" : 1000, "million" : 1000000}

    numbers = string.replace('-', ' ').split()

    term = 0
    for i in range(len(numbers)):
        if numbers[i] in table.keys(): 
            term += table[numbers[i]]
        if numbers[i] in  multipliers.keys(): 
            term += multipliers[numbers[i]] * (term % multipliers[numbers[i]]) - (term % multipliers[numbers[i]]);
    return term

print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"))