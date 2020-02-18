x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
f=float(input())

if x1==x2:
     print('{number:.{digits}f}'.format(number=x1, digits=6))
else:
          
     m=(y2-y1)/(x2-x1)
     m=m*f
     c=y1-m*x1
     n=-1*(c/m)
     print('{number:.{digits}f}'.format(number=n, digits=6))          
