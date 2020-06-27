p = []
with open(prime.txt) as p:
    line = p.readline()
    while line:
        p.append(int(line))
        line = p.readline()

h = []
with open(happy.text) as h: 
    line = h.readline()
    while line:
        h.append(int(line))
        line = h.readline()

over_lap = []
value for value in h:
    if value in p:
        over_lap.append(value)

print(over_lap)