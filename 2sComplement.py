# This program reads input of an 8 bit binary number and returns the two's complement of it.
# By Aman Atnafou, for CMSC207

validInput = False
string1 = ""
twoComplement = ""
finalOutput = ""
zeroString = ""

while not validInput:
    num = input("Please enter a 8 bit or smaller binary number: ")
    if len(num) > 8:  # Checks if input is longer than 8 bits
        print("Binary number cannot be larger than 8 bits. Please try again.")
    else:
        validInput = True  # To end the loop

for i in range(len(num)):  # Goes through every bit in the binary number supplied and reverses the value
    if num[i] == '1':
        string1 += '0'
    else:
        string1 += '1'


twoComplement = bin( int(string1, 2) + 1) # Adds 1 to the binary number and gets the new binary value

# This block formats the output by adding the preceding 0's that get thrown out by the bin() function after
# creating a new string without the "0b" prefix and adding it to the previous string
for j in range(2, len(twoComplement)):
    finalOutput += twoComplement[j]
if len(finalOutput) != len(num):  #if output string is not the same length as the input string
    difference = len(num) - len(finalOutput)
    for k in range(0, difference):
        zeroString += '0'
    finalOutput = zeroString + finalOutput


print("The two's complement is", finalOutput)