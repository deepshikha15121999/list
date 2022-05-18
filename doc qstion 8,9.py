# QUESTION NO 8
c=[2,4,5,4,4,2,4,2]
i=0
while i<len(c):
    b=c.count(c[i])
    if b>1:
        pass
    i=i+1
print(b)

# QUERSTION NO 9

FIND MAXIMUM NUMBER

a=[1,11,5,9,10,43,9]
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
print('first maximum is :-',max)

FIND SECOND MAXIMUM NUMBER

a=[87,23, 95,100,9,10,43,9]
i=0
max=0
sm=0
while i<len(a):
    if a[i]>max:
        sm=max
        max=a[i]
    elif a[i]>sm:
        sm=a[i]
    i=i+1
print('second maximum is :-',sm)

FIND THIRD MAXIMUM NUMBER

a=[3,7,4,97,23,78,48]
i=0
max=0
sm=0
tm=0
while i<len(a):
    if a[i]>max:
        tm=sm
        sm=max
        max=a[i]
    elif a[i]>sm:
        tm=sm
        sm=a[i]
    elif a[i]>tm:
        tm=a[i]
    i=i+1
print('third maximum is :-',tm)



