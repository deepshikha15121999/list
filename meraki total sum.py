number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=1
s=[]
while i<len(n):
    j=i
    while j<len(n):
        if n[i-1]+n[j]==number:
            s.append ([n[i-1],n[j]])
        j=j+1
    i=i+1
print(s)

# s=[]
# print(s.append([n[1],n[2]])
# print(s)

    

