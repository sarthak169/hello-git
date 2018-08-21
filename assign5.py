#ques 1
n=int(input("Enter the year\n"))
if(n%4==0):
    if(n%100==0):
        if(n%400==0):
            print("\n Leap year")
        else:
            print("Not a leap year")

#Ques 2
l=float(input("Enter length\n"))
b=float(input("Enter breadth\n"))
if(l==b):
    print("It is a square")
else:
    print("It is a rectangle")

#ques 3
a=int(input("Enter age of person 1\n"))
b=int(input("Enter age of person 2\n"))
c=int(input("Enter age of person 3\n"))
print("Oldest person is ",max(a,b,c)," years old\nYoungest person is ",min(a,b,c)," Years old")

#Ques 4
a=int(input("Enter age\n"))
s=input("Enter M if Male and F if female\n")
m=input("Enter Y if married and N if not married\n")
if(s=='F' or s=='f'):
    print("She will work only in urban areas\n")
elif(s=='M'or s=='m' and (a>19 and a<41)):
    print("He may work anywhere")
elif(s=='M' or s=='m' and (a>39 and a<61)):
    print("He will work in urban areas only")
else:
    print("Error")

#ques 5
cost=100
q=int(input("Enter quantity\n"))
p=float(q*cost)
if(q>1000):
    j=float(0.1*p)
    val=float(p-j)
    print("Cost after discount is ",val)
else:
    print("Sorry no discount amount is ",p)
#ques 6
for i in range(0,10):
    n=int(input("Enter integer ",i,"\n"))
    print(n)
#ques 7
while(True):
    print("This is a infinite loop")

#ques  8
n=int(input("How many elements do you want to enter\n"))
l=[]
for i in range(0,n):
    h=int(input("Enter element\n"))
    l.append(h)
l2=[]
for i in l:
    h=i*i
    l2.append(h)
print(l2)

#ques 9
st=[]
fl=[]
iy=[]
l=[4,5,6,7,8,'a','b','c','d',5.00,6.00,8.098]
for i in l:
    if(type(i) is str):
        st.append(i)
    elif(type(i) is float ):
        fl.append(i)
    elif(type(i) is int):
        iy.append(i)
print("List of integer type is ",iy)
print("List of float type is ",fl)
print("List of string type is",st)
#ques 10
l=[]
for i in range(1,101):
    count=0
    for j in range(2, int(i/2)) :
        if(i%j==0):
            count+=1
    if(count==0):
        l.append(i)
print(l)

#ques 11
q='*'
for i in range(1,5):
    print(i*q)
#ques 12
l=[]
n=int(input("how may elements in list?\n"))
for i in range(0,n):
    h=input("Enter element")
    l.append(h)
h=input("Which element you want\n")
l.remove(h)
print(l)
