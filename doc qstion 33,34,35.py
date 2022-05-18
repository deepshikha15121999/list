# QUESTION NO 33

# a=  [15, 81, 11, 234]
# i=0
# s=[]
# while i<len(a):
#     d=str(a[i])
#     c=int(d)
#     j=0
#     sum=0
#     while j<len(d):
#         b=c%10
#         c=c//10
#         sum=sum+b
#         j=j+1
#     s.append(sum)
#     i=i+1
# print(s)

# QUESTION NO 34

# a= [34.67, 12, -94.89, 'Python', 0, 'C#']
# i=0
# s=[]
# while i<len(a):
#     if type(a[i])==int:
#         s.append(a[i])
#     i=i+1
# print(s)
        

# QUESTION NO 35

# a=[1234, 122, 1984, 19372, 100]
a=['abc', 'abc', 'ab', 'a']
i=0
s=[]
while i<len(a):
    b=str(a[i])
    s.append(b)
    i=i+1
print(s)
j=0
c=s[0][0]
count=0
while j<len(s):
    if c==s[j][0]:
        count=count+1
    j=j+1
if count==len(s):
    print('true')
else:
    print('false')

