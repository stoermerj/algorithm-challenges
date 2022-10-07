"""Given a string s, find the length of the longest substring without repeating characters.
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

e = "abcdabcabclllo"
d = "ababababababcd"

def substringChar(str):
    try: 
        finalArr = []
        newArr = []
        sArr = [letter for letter in str]

        def appendCopyClear(str): #make a copy of array, clear it and append copied array to final array
            newArrCopy = newArr.copy()
            newArr.clear()
            finalArr.append(newArrCopy)

        for index, value in enumerate(sArr):
            if index+1 == len(str): #avoid error for last item
                if newArr.count(str[index]) == 0: #if not in list
                    newArr.append(str[index])
                    appendCopyClear(str)
                elif newArr.count(str[index]) > 0: #if already in list
                    appendCopyClear(str)
                    newArr.append(str[index]) #take current value with you to push into array
                    appendCopyClear(str)
            elif str[index] != str[index+1] and newArr.count(str[index]) == 0: #if current value not equal next value and not in list
                newArr.append(str[index])
            elif str[index] == str[index+1] or newArr.count(str[index]) > 0: #if current value  equal next value or  in list
                appendCopyClear(str)
                newArr.append(str[index]) #adds value to array
        return finalArr
    except:
        print("EXCEPTION")

returnsubstringChar = substringChar(d) 

def checkForLength(func):     #loop through finalArr for largest array
    lengthtestFunc = [len(y) for y in func]
    print(lengthtestFunc)
    return(max(lengthtestFunc), lengthtestFunc.index(max(lengthtestFunc)), func[lengthtestFunc.index(max(lengthtestFunc))]) #return length, index and array

finalAnswer = checkForLength(returnsubstringChar)
print(finalAnswer)

