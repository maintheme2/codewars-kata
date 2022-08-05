def rgb(r, g, b):
    rgbList = [r, g, b]
    for i in range(len(rgbList)):
        if 255 < rgbList[i]: rgbList[i] = 255
        elif 0 > rgbList[i]: rgbList[i] = 0
    temp = [str(hex(int(rgb)))[2::] if 
    len(str(hex(int(rgb)))[2::]) >= 2 else "0" + str(hex(int(rgb)))[2::]
    for rgb in rgbList]
    hexstr = "".join(temp)
    return hexstr.upper()

print(rgb(-20, 275, 125))