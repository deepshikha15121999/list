# question no 45

# a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# i=0
# s=[]
# while i <len(a)-3:
#     s.append(a[i])
#     i=i+1
# print(s)

# QUESTION NO  46   

# a=['0', '1', '2', '3', '4']
# b=['red', 'green', 'black', 'blue', 'white']
# c=['100', '200', '300', '400', '500']
# i=0
# s=[]
# while i<len(a):
#     d=a[i]+b[i]+c[i]
#     s.append(d)
#     i=i+1
# print(s)

# QUESTION NO 47

a=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
s=[]
while i <len(a):
    j=0
    p=[]
    while j<len(a[i]):
        d=a[i][j]
        p.append(d)
        j=j+1
    i=i+1
    s.append(p)
print(s)