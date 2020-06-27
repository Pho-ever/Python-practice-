def maxi(a,b,c):
    maxi3 = 0 
    if a > b:
        if a > c:
            maxi3 = c
        else:
            maxi3 = a
    else: 
        if b > c:
            maxi3 = b 
        else: 
            maxi3 = c
    return maxi3

