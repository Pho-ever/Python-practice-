user = int(input('Please pick a number \n'))
x = [y for y in range(2,user)if user % y == 0]
if len(y) == 0:
    print('You picked a prime number')
else:  
    print('You picked a non-prime number')
# if Prime(user):
#     print('The number you picked is a prime number')
# else:
#     print('The number you picked is not a prime number')