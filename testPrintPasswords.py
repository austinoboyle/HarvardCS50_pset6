from crypt import crypt
import sys

def strFromArray(arr):
    word = ""
    for char in arr:
        word += char
    return word

MAXLENGTH = 4

currentPas = ['A']
currentIndex = 0
currentInt = ord(currentPas[currentIndex])
while (len(currentPas) <= MAXLENGTH):

    while (currentInt < 123):
        currentPas[currentIndex] = chr(currentInt)
        currentInt += 1
    
    while (currentIndex >= 1 and ord(currentPas[currentIndex]) >= 122):
        currentPas[currentIndex] = 'A'
        currentIndex -= 1
    
    if (currentIndex == 0 and ord(currentPas[0]) >= 122):
        currentPas.append('A')
        currentPas[0] = 'A'
    
    else:
        currentInt = ord(currentPas[currentIndex])
        currentInt += 1
        currentPas[currentIndex] = chr(currentInt)
        
    currentIndex = len(currentPas) - 1

print("Password Not Alphabetic and 4 or fewer characters!")
        

