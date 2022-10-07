
"""
https://www.101computing.net/ip-addresses-ipv4-ipv6-mac-addresses-urls/

Python Task #1
Write a python program to generate and output:
    A random IPv4 address, An IP address (IPv4) consists of 4 Bytes: 4 numbers between 0 and 255 separated by dots. E.G.: 166.123.213.35
    A random IPv6 address, IPv6 addresses consist of 16 Bytes (=128 bits). They are expressed in hexadecimal using 8 blocks of 2 Bytes (4 hexadecimal digits) 
    separated by colons e.g.: 9714:B755:F5F0:CD59:2140:30ED:F7E2:0140
    A random MAC address. A MAC address consists of 6 Bytes of Data, expressed in hexadecimal, separated using colons. e.g. EB:DC:7A:36:0A:A2
"""


import random

def randomByteGenerator(places=4, startChar= 2, charac=4, address="IPv4"):
    returnValue = []
    if address == "IPv6" or address == "MAC":
        returnValue.append(":")
    if address == "IPv4":
        returnValue.append(".")
    
    while 0 < places:
        #random Number between 2 and b
        numberOfBytes = random.sample(range(startChar,charac),1)
        if address =="IPv6" or "MAC":
            numbersAndAlphabet = [chr(i).upper() for i in range(48, 123) if i < 58 or i > 96]
            randomList = random.sample(numbersAndAlphabet, charac)
            #print(randomList)

        if address =="IPv4":
        #random Number between 0 and 10 for two to b times
            randomList = random.sample(range(0,10), numberOfBytes[0])

            #if i = 10, then remove it for only two numbers
            for i in randomList:
                if i > 9:
                    randomList.remove(i)

        #makes string out of list
        combinedList = ''.join(str(e) for e in randomList)

        returnValue.append(combinedList)
        places= places-1
    return returnValue


finalOutputList = randomByteGenerator(6,1,2,"MAC")
#finalOutputList = randomByteGenerator(6,1,2,"MAC")
#finalOutputList = randomByteGenerator(8,2,4,"IPv6")
#finalOutputList = randomByteGenerator(4,2,4,"IPv4")

separator = finalOutputList.pop(0)
finalOutputString = separator.join(str(e) for e in finalOutputList)
print(finalOutputString)
