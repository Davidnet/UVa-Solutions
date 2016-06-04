import sys
counter_closed_tick = False
s = ""
i = 0
for line in sys.stdin:
    while "\"" in line:
        if i % 2 == 0:
            line = line.replace("\"", "``",1)
        elif i % 2 == 1:
            line = line.replace("\"", "\'\'",1)
        i += 1
    s += line
print(s)    
