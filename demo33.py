date = {"oluwayomi mofetoluwa" : "01/02/78",
            "dami krane" : "05/12/89",
            "mary jane" : "12/05/99",
            "dwayne johnson" : "11/03/98"
            }

while True:
    print("Welcome to the birthday dictionary \n We have know the birthdays of: ")
    for items in date:
        print(items)
    print("Please enter a name: ")
    item = input()
    item = item.lower()
    if item == "":
        break 
    if item in date:
        print(item + "'s birthday is on the " + date[item])
    else: 
        print("Sorry, we dont have that person's birthday")
