p=[[8,3,4],
   [1,5,9],
   [6,7,2]]
i=0
a,b,c,d,e,f,g,h=0,0,0,0,0,0,0,0
while i<len(p):
    a=a+p[i][0]
    b=b+p[i][1]
    c=c+p[i][2]
    d=d+p[0][i]
    e=e+p[1][i]
    f=f+p[2][i]
    g=g+p[i][i]
    h=h+p[i][2-i]
    i=i+1
if a==b==c==d==e==f==g==h==15:
    print('magic square')
else:
    print('not magic square')
    