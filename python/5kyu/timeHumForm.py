def make_readable(seconds):
    seconds = str(seconds // 3600) + " " + str(seconds % 3600 // 60) + " " + str(seconds % 3600 % 60)
    return ":".join([time if len(time) > 1 else "0" + time for time in seconds.split(" ")])

print(make_readable(60))