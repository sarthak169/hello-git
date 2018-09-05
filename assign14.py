# # ques 1
# l=[1,2,3,4,5,6,7,8,9,10]
# h=[i*i*i for i in l]
# print(h)
# #ques 2
# def prime(x):
#     c=0
#     for i in range(2,int(x/2)):
#         if(x%i == 0):
#             c+=1
#     if(c==0):
#         return True
#     else:
#         return False
# k=list(filter(prime,l))
# print(k)
#ques 4
# The difference between the two kinds of expressions is that
# the List comprehension is enclosed in square brackets []
# while the Generator expression is enclosed in plain parentheses ().
# Therefore the list comprehension returns a list
# while the generator expression return a generator
# We can access the elements of the list
# but if we try to access the elements of the generator we get a TypeError'''
#ques 5
cel=[39.2, 36.5, 37.3, 37.8]
f=list(map(lambda x: 1.8*x +32,cel))
print(f)
#ques 6
l=[1,2,3,4,5,6]
h=list(map(lambda x: x*x,l))
print(h)
# ques 7
l=[1,2,3,4,5,6,7,8,9,10,11]
def prime(x):
    c=0
    for i in range(2,int(x/2)):
        if(x%i == 0):
            c+=1
    if(c==0):
        return True
    else:
        return False
k=list(filter(prime,l))
print(k)
#ques 8
l=[1,2,3,4,5,11,6]
from functools import *
g=reduce(lambda x,y : x*y,l)
print(g)
