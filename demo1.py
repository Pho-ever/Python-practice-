# Create a program that ask the user to enter their name and their age. 
# print out a message addressed to them that tells them the year they will turn 100 
name = print('What is your name please: ')
name = input()
age = print('How old are you?')
age = int(input ())
print('Your name is ' + name + 'and you are ' + str(age) + ' years old')
years = 2120 - age
print('You will be 100 years old in the year ' + str(years))


# Or

name = input('What is your name please: ')
age = int(input('How old are you? '))
print('Your name is ' + name + 'and you are ' + str(age) + ' years old')
years = 2120 - age
print('You will be 100 years old in the year ' + str(years))