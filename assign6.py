#ques 1
def area(num):
    area=float(4*3.14*r*r)
    return area
r=int(input("Enter radius\n"))
n=area(r)
print(n)

#ques 2
def perfect(num):
    l=0
    for i in range(1,num):
        if(num%i==0):
            l=l+i
    if(l==num):
        return l
    else:
        return 0
for i in range(1,1000):
    h=perfect(i)
    if(h!=0):
        print(h)

#ques 3
def table(n):
    for i in range(1,11):
        print(n,'X',i,'=',n*i)
n=int(input("Enter digit\n"))
table(n)

#ques 4
def power(b,e):
    if(e==1):
        return(b)
    if(e!=1):
        return(b*power(b,e-1))
b=int(input("Enter base: "))
e=int(input("Enter exponential value: "))
print("Result:",power(b,e))
