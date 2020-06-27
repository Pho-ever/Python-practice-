# def backwards(name):
#     name = input("Please input some words")
#     if type(name) is str 
#     reverse 
name1 = input('Please input some words \n')
def reverse(name1):
    names = name1.split()
    if len(names) <= 1:
        return print(name1)
    else:
        new_split = ' '.join([word for word in names[::-1]])
        return print(new_split) 
reverse(name1)

