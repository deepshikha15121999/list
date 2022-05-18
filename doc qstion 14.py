# FIND THE MAXIMUM LENGTH

a=[[0], [1, 3], [5, 7], [9,12,98,11], [13, 15, 17]]
i=0
b=[]
while i<len(a):
    if len(a[i])>len(b):
        b=a[i]
    i=i+1
print(len(b),b)


# FIND THE MINIMUM LENGTH

a=[[6], [1, 3], [5, 7], [9,12,98,11], [13, 15, 17]]
i=1
b=a[0]
while i<len(a):
    if len(a[i])<len(b):
        b=a[i]
    i=i+1
print(len(b),b)
