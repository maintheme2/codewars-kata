# y, d, h, m and s
import humanize
import datetime as dt

def format_duration(seconds):
    delta = dt.timedelta(seconds=seconds)  
  
    return humanize.time.precisedelta(delta)
    
print(format_duration(123456789))