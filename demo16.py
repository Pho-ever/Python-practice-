import random 

a = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*()?'
passlen = 8
p = "".join(random.sample(a,passlen))
print(p)