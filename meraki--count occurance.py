char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=0
n=0
t=0
x=0
u=0
g=0
l=[]

while i<len(char_list):
    if 'a' in char_list[i]:
        a=a+1
    elif 'n'in char_list[i]:
        n=n+1
    elif 't'in char_list[i]:
        t=t+1
    elif 'x'in char_list[i]:
        x=x+1
    elif 'u'in char_list[i]:
        u=u+1
    elif 'g'in char_list[i]:
        g=g+1

    i=i+1
l.append(['a',a])
l.append(['n',n])
l.append(['t',t])
l.append(['x',x])
l.append(['u',u])
l.append(['g',g])
print(l)
print('a',a,'times')
print('n',n,'times')
print('t',t,'times')
print('x',x,'times')
print('u',u,'times')
print('g',g,'times')
