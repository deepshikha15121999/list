# QUESTION NO 5
il = [1, 2, 2, 5, 8, 4, 4, 8]
s=[]
i=0
count=0
while i<len(il):
    if il[i] not in s:
        s.append(il[i])
        count=count+1
    i=i+1
print(s)
print('unique values are',count)


QUESTION NO 6

a[i]>b[i], so Alice receives 1 point.
a[i]=b[i], so nobody receives a point.
a[i]<b[i], so Bob receives 1 point

a = [17, 122, 23]
b = [31, 24, 187]
i=0
al=0
bo=0
while i<len(a):
    if a[i]>b[i]:
        al=al+1
    elif a[i]==b[i]:
        pass
    elif a[i]<b[i]:
        bo=bo+1
    i=i+1
print(al,bo)

#  QUESTION NO 7
# SUM OF LIST

a=[1,2,3,4]
i=0
sum=0
while i<len(a):
    sum=sum+a[i]
    i=i+1
print(sum)