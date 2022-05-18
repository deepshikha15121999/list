QUESTION NO 39

a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
j=0
s=[]
while j<len(a[j]):
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i][j]
        i=i+1
    j=j+1
    b=sum/len(a)
    s.append(b)
print(s)

QUESTION NO 40

a=[[1, 2, 4], [2, 4, 4], [1, 2]]
j=0
s=[]
while j<len(a[j]):
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i][j]
        i=i+1
    j=j+1
    b=sum
    s.append(b)
print(s)

# QUESTION NO 41

a=[[0, 1,3], [2, 4,6]]
j=0
sum=0
while j<len(a[0]):
    sum=sum+1
    j=j+1
print(len(a),sum)