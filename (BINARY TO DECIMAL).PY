a=[1, 0, 0, 1, 1, 0, 1, 1]
i=0
sum=0
while i<len(a):
    b=a[-(i+1)]
    sum=sum+b*(2**i)
    i=i+1
print(sum)

