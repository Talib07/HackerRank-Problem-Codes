l = list(input().split())
val={}
for i in range(10):
     val[str(i)]=i
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=10
for i in s:
     val[i]=x
     x+=1
l=['1Z','A','L0','17']
mini=-1
for i in range(len(l)):
     num=l[i]
     m=val[num[0]]
     for el in num:
          m=max(val[el],m)
     base=m+1
     print("base = " + str(base))

     numlist=[val[x] for x in num ]
     numlist.reverse()
     print(numlist)
     p=0
     s=0
     for n in numlist:
          s+= n*(base**p)
          p+=1
     print("Decimal Value = " + str(s))
     if mini==-1:
          mini=s
     mini=min(mini,s)
print(mini,end='')
     




