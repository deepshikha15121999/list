# QUESTION NO 2

# a= [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# sum=''
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)

# QUESTION NO 4

l= [6,1,3,5,6,3,1]
s=[]
i=0
p=1
while i<len(l):
    if l[i] not in s:
        s.append(l[i])
        p=p*l[i]
    i=i+1
print(s)
print(p)


