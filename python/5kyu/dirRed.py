def dirReduc(arr):
      output = []
      str = "".join(arr)
      while True:
            while True:
                  if "NORTHSOUTH" in str: str = str.replace("NORTHSOUTH", "")
                  else : break
            while True:
                  if "SOUTHNORTH" in str: str = str.replace("SOUTHNORTH", "")
                  else : break
            while True:
                  if "EASTWEST" in str: str = str.replace("EASTWEST", "")
                  else : break
            while True:
                  if "WESTEAST" in str: str = str.replace("WESTEAST", "")
                  else : break
            if all(dir not in str for dir in ("NORTHSOUTH","EASTWEST","WESTEAST","SOUTHNORTH")):
                  print(str)
                  break

      for i in range(1, len(str) - 1):
            if str[i-1] in "WE" and str[i] not in "S":
                  output.append(str[i-1:i+3])
            if str[i-1] in "SN" and str[i] in "O":
                  output.append(str[i-1:i+4])
      return output

print(dirReduc(['NORTH', 'EAST', 'NORTH', 'EAST', 'WEST', 'WEST', 'EAST', 'EAST', 'WEST', 'SOUTH']))