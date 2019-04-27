def check_productID(isbn):
    remainingDigits = isbn[3:]    
    #print(remainingDigits)        
    assert len(remainingDigits) == 9
    sum = 0
    for i in range(len(remainingDigits)):
        number = int(remainingDigits[i])
        value = i + 1
        sum += value * number
    print(sum)
    result = sum % 11
    #print(result)
    #print(value)
    if result == 10:
        print(str(remainingDigits)+'X')
    else:
        print(str(remainingDigits)+str(result))

isbn = input("ISBN :  ")

check_productID(isbn)
