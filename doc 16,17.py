# QUESTION NO 16
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i=1
# s=[]
# while i<len(a):
#     b=a[i]-a[i-1]
#     s.append(b)
#     i=i+1
# print(s)


# QUESTION NO 17

a=[2,4,6,9,13,8,15,7]
i=0
sum=0
while i<len(a):
    b=i+2
    if b<=len(a):
        if a[-(i+2)]>=9:
            sum=0
            p=0
            c=a[-(i+2)]
            w=str(a[-(i+2)])
            while p<len(w):
                
                d=c%10
                c=c//10
                sum=sum+d
                p=p+1
            a[-(i+2)]=sum
        else:
            a[-(i+2)]=a[-(i+2)]*2
    # a.insert(-(i+2),b)
    i=i+2
print(a)

