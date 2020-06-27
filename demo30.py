import random
with open('demo_30.txt') as f:
    line = list(f)
print(random.choice(line).strip())