# SUM OF EVEN AND ODD NUMBER
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# even=0
# odd=0
# while i<len(elements):
#     if elements[i]%2==0:
#         even=even+elements[i]
#     else:
#         odd=odd+elements[i]
#     i=i+1
# print('SUM-'even)
# print('SUM-'odd)

# AVERAGE OF EVEN AND ODD

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        even=even+elements[i]
    else:
        odd=odd+elements[i]
    i=i+1
print(even/len(elements))
print(odd/len(elements))
