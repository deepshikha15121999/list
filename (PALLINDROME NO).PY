a=input('enter string only:-')
i=0
c=''
while i<len(a):
    b=a[-(i+1)]
    c=c+str(b)
    i=i+1
if c==a:
    print('pallindrome')
else:
    print('not pallindrome')