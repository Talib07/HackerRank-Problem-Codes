import numpy as np


nm=int(input())
mat=np.zeros((nm,nm),dtype=np.int)
#knights
count=int(input())
knight=[]
n=0
while(n<count):
    c=[int(x) for x in input().split()]
    knight.append(c)
    mat[c[0]][c[1]]=1
    n+=1 
for c in knight:
    sx=[-2,-2,2,2,-1,-1,1,1]
    sy=[1,-1,-1,1,2,-2,-2,2]
    for s in range(len(sx)):
        x=c[0]+ sx[s]
        y=c[1]+ sy[s]
        if x<nm and x>=0 and y<nm and y>=0:
            mat[x][y]=2
#rooks
count=int(input())
rooks=[]
n=0
while(n<count):
    c=[int(x) for x in input().split()]
    rooks.append(c)
    mat[c[0]][c[1]]=1
    n+=1 
for c in rooks:
    sx=[0,0,-1,1]
    sy=[1,-1,0,0]
    
    for s in range(len(sx)):
        x=c[0]
        y=c[1]
        while( x < nm and x>=0 and y<nm and y>=0):
            if(mat[x][y]==2):
                 break
            mat[x][y]=1    
            x=x+sx[s]
            y=y+sy[s]




#bishop
count=int(input())
bishop=[]
n=0
while(n<count):
    c=[int(x) for x in input().split()]
    bishop.append(c)
    mat[c[0]][c[1]]=1
    n+=1 

for c in bishop:
    sx=[1,1,-1,-1]
    sy=[1,-1,1,-1]
    
    for s in range(len(sx)):
        x=c[0]
        y=c[1]
        while( x < nm and x>=0 and y<nm and y>=0):
             if(mat[x][y]==2):
                  break
             mat[x][y]=1    
             x=x+sx[s]
             y =y+sy[s]




#queen
count=int(input())
queen=[]
n=0
while(n<count):
    c=[int(x) for x in input().split()]
    queen.append(c)
    mat[c[0]][c[1]]=1
    n+=1 
for c in queen:
    sx=[1,1,-1,-1,0,0,-1,1]
    sy=[1,-1,1,-1,1,-1,0,0]

    
    for s in range(len(sx)):
        x=c[0]
        y=c[1]
        while( x < nm and x>=0 and y<nm and y>=0):
            if(mat[x][y]==2):
                 break
            mat[x][y]=1    
            x=x+sx[s]
            y=y+sy[s]
#print(mat)
count=0
for i in mat:
    for j in i:
        if j==0:
            count+=1
print(count)
    



