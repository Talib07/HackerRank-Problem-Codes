import numpy as np


nm=int(input())
mat=np.zeros((nm,nm),dtype=np.int)
#mat=[[0]*nm]*nm
#print(mat)

coordinate=[]

#knights rooks bishop queen

count=int(input())
co=[]
n=0
while(n<count):
    c=[int(x) for x in input().split()]
    co.append(c)
    n+=1 
for c in co:
    sx=[-2,-2,2,2,-1,-1,1,1]
    sy=[1,-1,-1,1,2,-2,-2,2]
    for s in range(len(sx)):
        x=c[0]+ sx[s]
        y=c[1]+ sy[s]
        if x<nm and x>=0 and y<nm and y>=0:
            mat[x][y]=1
print(mat)
    



#rooks
count=int(input())
co=[]
n=0
while(n<count):
    c=[int(x) for x in input().split()]
    co.append(c)
    n+=1 
#rooks
for c in co:
    x=c[0]
    y=c[1]
    mat[:,y]=1
    mat[x,:]=1

print(mat)





#bishop
count=int(input())
co=[]
n=0
while(n<count):
    c=[int(x) for x in input().split()]
    co.append(c)
    n+=1 
for c in co:
    sx=[1,1,-1,-1]
    sy=[1,-1,1,-1]
    
    for s in range(len(sx)):
        x=c[0]
        y=c[1]
        while( x < nm and x>=0 and y<nm and y>=0):
            mat[x][y]=1    
            x=x+sx[s]
            y=y+sy[s]
#####################3
for c in co:
    mat[c[0],c[1]]=2
# #####################33           
print(mat)
#bishop





#Queen
count=int(input())
co=[]
n=0
while(n<count):
    c=[int(x) for x in input().split()]
    co.append(c)
    n+=1
for c in co:
    sx=[1,1,-1,-1]
    sy=[1,-1,1,-1]
    
    for s in range(len(sx)):
        x=c[0]
        y=c[1]
        while( x < nm and x>=0 and y<nm and y>=0):
            mat[x][y]=1    
            x=x+sx[s]
            y=y+sy[s]
    mat[:,c[1]]=1
    mat[c[0],:]=1

#print(mat)
count=0
for i in mat:
    for j in i:
        if j==0:
            count+=1
print(count)



