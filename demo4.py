num = int(input('Please pick a number '))
z = []
y = num + 1
y = int(y)
for x in range(1, y):
    if num % x == 0:
        z.append(x)
print(z)
