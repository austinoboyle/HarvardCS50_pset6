import cs50

print ("number: ", end = '')
cardNumber = cs50.get_int()
currentNumber = cardNumber
sumDigits = 0
index = 0

while (currentNumber > 0):
    currentDigit = currentNumber % 10
    
    if index % 2 == 0:
        sumDigits += currentDigit
    else:
        currentDigit *= 2
        sumDigits += (currentDigit + currentDigit // 10) % 10
    
    if (currentNumber >= 10 and currentNumber < 100):
        firstTwoDigits = currentNumber
        firstDigit = currentNumber // 10
        
    index += 1
    currentNumber //= 10

validSum = sumDigits % 10 == 0

if (validSum):
    if firstTwoDigits in range(51,56):
        print("MASTERCARD")
    elif firstTwoDigits == 34 or firstTwoDigits == 37:
        print("AMEX")
    elif firstDigit == 4:
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")