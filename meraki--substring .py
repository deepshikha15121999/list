mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
a=mainStr.split()
i=0
while i<len(a):
    if a[i]=='over':
        a.remove('over')
    i=i+1
print(a)


