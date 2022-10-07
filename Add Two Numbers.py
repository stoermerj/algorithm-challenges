"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
https://leetcode.com/problems/add-two-numbers/

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807."""

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

try:
    def reverseList(list): #reverse the list
        list.reverse()
        return list
    
    def combineList(list): #combine the list to one int
        stringType = [str(x) for x in list]
        stringType = ''.join(stringType)
        stringType = int(stringType)
        return stringType

    def addNumbers(): #execute the functions and add the numbers
        answerOne = reverseList(l1)
        answerOne = combineList(l1)
        answerTwo = reverseList(l2)
        answerTwo = combineList(l2)
        return answerOne + answerTwo
        print(answerOne + answerTwo)

    def reverseInt():
        answerCombined = addNumbers() #execute addnumbers function
        answerCombined = str(answerCombined) #change to string for iteration
        answerCombined = [int(x) for x in answerCombined] #list function with change to int
        answerCombined.reverse() #reverse the list
        print(answerCombined)

except:
    print("error")

reverseInt()