num = input('Please pick a number ') 
num = int(num)
if num % 2 == 0 and num % 4 == 0:
    print('The number you picked is an even number and a multiple of four')
elif num % 2 == 0:
    print('You picked an even number')
else:
    print('You picked an odd number')