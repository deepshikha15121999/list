# QUESTION NO 42

a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
s=[]
# while i<len(a):
j=3
while j<len(a):
    s.append(a[j])
    j=j+1
k=0
while k<3:
    s.append(a[k])
    k=k+1
print(s)


QUESTION NO 43
O/P=[1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]

a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
i=0
s=[]
while i<len(a):
    s.append(a[i])
    if (i+1)%4==0:
        s.append(20)
    i=i+1
print(s)

a=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
i=0
s=[]
while i<len(a):
    s.append(a[i])
    if (i+1)%3==0:
        s.append('Z')
    i=i+1
print(s)

# QUESTION NO 44
a=[3, 8, 9, 4, 5, 0, 5, 0, 3]
i=0
s=[]
while i<len(a):
    p=a[i]+3
    s.append(p)
    i=i+1
print(s)

