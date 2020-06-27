count{}
with open('nameslist.txt')as f:
    line = f.readline()
    while line:
        line = line.split()
        if line in count:
            count[line] += 1
        else: 
            count[line] = 1
        line = f.readline()
print(count)