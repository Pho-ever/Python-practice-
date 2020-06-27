# def fib(nums):
#     total = 0 
#     for num in nums:
#         total += num 
#     return total
# print(fib([1,2,3,4,5,6,7,8])) 

def fib(nums):
    if n == 1:
        f = [1]
    elif n!= 1:
        f = [1,-1]
    while len(f) < n:
        f.append(f[-1] + f[-2])
    return(f)
user = int(input('Please enter a number '))
f = fib(user)
print('sequence is ')
for x in f:
    print(x)