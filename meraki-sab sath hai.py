elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
even1=0
odd=0
odd1=0
while i<len(elements):
    if elements[i]%2==0:
        even=even+1
        even1=even1+elements[i]
    else:
        odd=odd+1
        odd1=odd1+elements[i]
    i=i+1

print('count of odd numbers ….',odd)
print('count of even numbers ….',even)
print('count of all the numbers ….',len(elements))
print('sum of odd numbers ….',odd1)
print('sum of even numbers ….',even1)
print('sum of all the numbers ….',sum(elements))
print('average of odd numbers ….',odd1/len(elements))
print('average of even numbers ….',even1/len(elements))
print('average of all the numbers ka ….',sum(elements)/len(elements))

