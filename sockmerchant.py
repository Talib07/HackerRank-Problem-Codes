# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:14:45 2019

@author: Talib
"""

def climbingLeaderboard(scores, alice):
    
    ranking_array=[]
    ranking_array.append(1)
    rank=1
    for i in range(1,len(scores)):
        if(scores[i-1]>scores[i]):
            ranking_array.append(rank+1)
            rank+=1
        elif(scores[i]==scores[i-1]):
            ranking_array.append(rank)
    flag=0      
    alice_ranks=[]
    j=len(scores)-1
    for i in alice:
        while(i>scores[j]):
            j-=1
            if(j<0):
                flag=1
                alice_ranks.append(1)
                j=0
                break
        if(i==scores[j]):
            #print(i,scores[j])
            alice_ranks.append(ranking_array[j])
        else:
            if(flag):
                flag=0
                continue
            print(i,scores[j],ranking_array[j]+1)
            alice_ranks.append(ranking_array[j]+1)
        
        '''if(i<scores[-1]):
            alice_ranks.append(rank+1)
            #print("1")
        elif(i==scores[-1]):
            alice_ranks.append(rank)
            #print("2")
        elif(i>=scores[0]):
            alice_ranks.append(1)
            #print("3")
        elif(i in scores):
            score_index = scores.index(i)
            obtained_rank = ranking_array[score_index]
            alice_ranks.append(obtained_rank)
        else:
            #print("4")
            score_index=0
            for k in range(len(scores)-1,score_index,-1):
                if(i>scores[k] and i<scores[k-1]):
                    #print("in between")
                    score_index = k-1
                    obtained_rank = ranking_array[score_index]+1
                    alice_ranks.append(obtained_rank)'''
        
               
    return alice_ranks
                
def main():
    alice=[50, 65, 77, 90 ,102]
    scores= [100, 90, 90, 80, 75, 60]

    ranks=climbingLeaderboard(scores, alice)  
    print(ranks)
main()
                    
        
    
     
    
    


