# y, d, h, m and s

def format_duration(seconds):
    delta = {"years" : seconds // (3600 * 24 * 365), "days" : seconds % (3600 * 24 * 365) // (3600 * 24), "hours" : seconds % (3600 * 24 * 365) % (3600 * 24) // 3600, "minutes" : seconds % (3600 * 24 * 365) % (3600 * 24) % 3600 // 60,
    "seconds" : seconds % (3600 * 24 * 365) % (3600 * 24) % 3600 % 60 }

    result = ''
    for item in delta:
        if delta[item] != 0:
            if delta[item] == 1:
                result += str(delta[item]) + ' '
                item = item[:-1]
                result += item + ', '
            else: result += str(delta[item]) + ' ' + item + ', '

    result = list(result)

    if len(result) > 0: result[-1] = ''
    elif len(result) == 0: return "now"

    comma_counter = 0
    for i in range(len(result)-1, -1, -1):
        if result[i] == ',':
            comma_counter += 1
            if comma_counter == 2:
                result[i] = ' '
                result[i+1] = "and "
                break
            else: result[i] = ''
    result = "".join(result)
    return result

print(format_duration(0))