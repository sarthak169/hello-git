#assignment 3
#ques 1
"""list=[]
n=int(input("How many items do you want ot enter in the list\n"))
for i in range(0,n):
    c=input("Enter Element\n")
    list.append(c)
print(list)
#ques 2
a=['google','apple','facebook','microsoft','tesla']
list.extend(a)
print(list)
#ques 3
x=input("Enter element you want to count")
p=list.count(x)
print("The item",x,"occurs ",p,"Times")
#ques 4
num=[]
n=int(input("How many numbers in list"))
for i in range(0,n):
    h=int(input("Enter number"))
    num.append(h)
num.sort()
print(num)
    #question 5

a=[1,2,3,4,10,50,61]
b= [7,11,35,46,68,456]
c=a+ b
c.sort()
print(c)
#optional ques
stack=['a','b','c','d','e']
print("Stack is: ",stack)
stack.append('f')
print("New stack is: ",stack)
print("Top is: ",stack.pop())
print("Updated stack is: ",stack)
#queue
queue=[1,2,3,4,5]
print("Queue is: ",queue)
queue.append(99)
print("New queue is: ",queue)
queue.pop(0)
print("Updated queue is: ",queue)
#ques 6
even=0
odd=0
for i in c:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("Even Elements are\n",even,"\nodd elements are \n",odd)
#ques 7"""
tup=('hello','i','am','sarthak')
print(tup[::-1])
tup1=(4,6,2,1,2,3,10,24,1424,123)
print("Max element is",max(tup1))
print("Smallest element is ",min(tup1))
#Strings
#ques 1
st="welcome to python"
print(st.upper())
#ques2
st1="1234"
print(st1.isdigit())
#ques 3
str="Hello World"
print(str.replace('World','Sarthak'))
