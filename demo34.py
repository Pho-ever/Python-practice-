import json 
birthdays = {}

with open ('demo34.json') as f:
    birthdays = json.load(f)

def add_entry():
    name = input('Who do you want to add to the birthday dictionary? \n')
    date = input(f'When was {name} born \n')
    item = birthdays['birth']
    new = {"name": name, "date": date}
    item.append(new)
    with open('demo35.json', 'w') as file:
        json.dumps(birthday, file)
    print(f'{name} was added to the birthday list')
add_entry()


