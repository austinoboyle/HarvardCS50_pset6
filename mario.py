import cs50

height = -1
while ((height > 23) or (height <= 0)):
    print("Height: ", end = '')
    height = cs50.get_int()

for i in range(height):
    spaces = (height - i-1) * " "
    hashes = (i + 1) * "#"
    print (spaces + hashes + " " + hashes + spaces)