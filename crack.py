from crypt import crypt
import sys

def strFromArray(arr):
    word = ""
    for char in arr:
        word += char
    return word

if len(sys.argv) != 2:
    print("Usage: python crack.py hash")
    exit(1)

MAXLENGTH = 4

hashVal = sys.argv[1]
salt = hashVal[0:2]
currentPas = ['A']
currentIndex = 0
currentInt = ord(currentPas[currentIndex])
while (len(currentPas) <= MAXLENGTH):

    while (currentInt < 123):
        if (crypt(strFromArray(currentPas), salt) == hashVal):
            print("{}".format(strFromArray(currentPas)))
            exit(0)
        currentPas[currentIndex] = chr(currentInt)
        currentInt += 1
    
    while (currentIndex >= 1 and ord(currentPas[currentIndex]) >= 122):
        currentPas[currentIndex] = 'A'
        currentIndex -= 1
    
    if (currentIndex == 0 and ord(currentPas[0]) >= 122):
        currentPas.append('A')
        currentPas[0] = 'A'
        currentInt = ord('A')
    
    else:
        currentInt = ord(currentPas[currentIndex])
        currentInt += 1
        currentPas[currentIndex] = chr(currentInt)
        currentInt = ord('A')
        
    currentIndex = len(currentPas) - 1

print("Password Not Alphabetic and 4 or fewer characters!")
        

