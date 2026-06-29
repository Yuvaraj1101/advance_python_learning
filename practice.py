#filter even numbers
a=[21,43,34,12,4,45,]
b=list(filter(lambda x:x%2==0,a))
print(b)

#square of a numbers using lambda
a=[12,44,323,34,5,]

b=list(map(lambda x:x**2,a))
print(b)

#sum of list using reduce
from functools import reduce
a=[1,2,3,4,5]

b=reduce(lambda x,y:x+y,a)
print(b)

students = [
("Raj",80),
("Kumar",95),
("Arun",70)
]
b=sorted(students,key=lambda x:x[1],reverse=True)
print(b)