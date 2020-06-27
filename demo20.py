def list_numbers(ordered, find):
    for value in ordered:
        if value == find:
            return True
    return False

# if __name__ == "__main__":
s = [3,5,7,9,13,15,17]
print(list_numbers(s,13))
print(list_numbers(s,2))
print(list_numbers(s,7))
print(list_numbers(s,1))

# How to use binary??