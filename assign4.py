#question 1
list=[]
n=int(input("how many elements"))
for i in range(0,n):
    a=input("Enter element\n")
    list.append(a)
#print(list[::-1])
for i in list[::-1]:
    print(i)

#question 2
string=input("Enter string\n")
for i in string:
    if(i.isupper()):
        print(i)

#Ques 3
string1=input("Enter the value\n")
s=string1.split(',')
l=[]
for i in s:
    l.append(int(i))
print(l)


#question    4
str=input("Enter the string\n")
count=0
str1=str[::-1]
if(str==str1):
    print("The string is palindrome")
else:
    print("The string is not palindrome")

#ques 5
import copy as c
l1=[1,2,4,[6,7],9,10]
l2=c.deepcopy(l1)
l1[3][0]=3
print(l1)
print(l2)
# in deep copy the string is just copied to another string and if the changes are made in 1st string then the second string is not affected because it was copied bfore the changes were made
# where as in shallow copy reference object is copied to another string so any changes made in string is directly implemented over the other string.
