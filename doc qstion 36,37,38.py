# QUESTION NO 36
# a=['1', '2', '3', '4', '5', '6', '7', '8','9','7','5']
# i=1
# s=[]
# while i<len(a):
#     b=a[i-1]+a[i]
#     s.append(b)
#     i=i+2
# print(s)

# QUESTION NO 37
a=[1, 2, 3, 4, 5, 6]
s=[]
i=0
while i<len(a)-1:
    p=[] 
    p.append(a[i]),p.append(a[i+1])
    s.append(p)
    i=i+1
print(s)
    

QUESTION NO 38
b='https://www.w3resource.com/python.edu-exercises.tv/list/'
a=['.com', '.edu', '.tv']
i=0
count=0
while i<len(a):
    if a[i] in b:
        count=count+1
    i=i+1
if count==len(a):
    print('true')
else:
    print('false')



