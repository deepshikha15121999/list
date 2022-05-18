# QUESTION NO 12
# a=int(input('enter a no:-'))

c='70304'
x=''
i=1
for a in c:
    if a=="0":
        pass
    else:
        d=int(a)
        b=len(c)-i
        x=x+str(d*(10**b))+'+'
    i=i+1
print(x[:-1])

# a=int(input('enter any no:-'))
# if a%10==0:

# QUESTION NO 14
#     FIND THE MAXIMIM LENGTH OF LIST
    
# l=[[0], [1, 3], [13, 15, 17],[5, 7], [9, 11]]
# i=0
# max=0
# while i<len(l):
#     if len(l[i])>max:
#         max=len(l[i])
#     i=i+1
# print(max,l[i-1])
#     #   FIND THE MINIMUM LENGTH OF LIST
