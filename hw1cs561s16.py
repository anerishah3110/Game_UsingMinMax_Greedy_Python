# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 18:48:22 2016

@author: Aneri
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*
#import sys
from copy import deepcopy
#file=open(sys.argv[2])
file=open("C:\Users\Aneri\.spyder2\input5.txt")
data=file.readlines()
#print data
data[12]=data[12]+"\n"

temp_file=open("traverse_log.txt","w+")


def find_adjacent(i,j,adj):
    if(i-1>=0 and i-1<5):
        if(position[i-1][j]=='*'):
         l=[]
         l.append(i-1)
         l.append(j)
         if l not in adj:
            adj.append(l)
    if(i+1>=0 and i+1<5):
        if(position[i+1][j]=='*'):
         l=[]
         l.append(i+1)
         l.append(j)
         if l not in adj:
            adj.append(l)
    if(j-1>=0 and j-1<5):
        if(position[i][j-1]=='*'):
         l=[]
         l.append(i)
         l.append(j-1)
         if l not in adj:
            adj.append(l)
    if(j+1>=0 and j+1<5):
        if(position[i][j+1]=='*'):
         l=[]
         l.append(i)
         l.append(j+1)
         if l not in adj:
            adj.append(l)
    return adj 
    
def Eval(p):
    sumx=0
    sumo=0
    total=0
   
    for i in xrange(5):
        for j in xrange(5):
            if position[i][j]=='X':
                sumx=sumx+int(grid[i][j])
            elif position[i][j]=='O':
                sumo=sumo+int(grid[i][j])
#    print sumo
#    print sumx
    if(p=='X'):
        total=sumx-sumo
    elif(p=='O'):
        total=sumo-sumx
        
    return total
    
   

def sneak(i,j):
    sum = int(grid[i][j])+Eval(player[0])
    
    global S_max
    global S_i
    global S_j
    if sum > S_max:
         S_max = sum
         S_i=i
         S_j=j
         
         
def traverse(i,j):
    y=''
    if (j==0):
        y='A'
    elif (j==1):
        y='B'
    elif (j==2):
        y='C'
    elif (j==3):
        y='D'
    elif (j==4):
        y='E'
    return y+str(i+1)


def minmax_Eval(p,play):
    sumx=0
    sumo=0
    total=0
   
    for i in xrange(5):
        for j in xrange(5):
            if p[i][j]=='X':
                sumx=sumx+int(grid[i][j])
            elif p[i][j]=='O':
                sumo=sumo+int(grid[i][j])
    
#    print sumo
#    print sumx
    if(play=='X'):
        total=sumx-sumo
    elif(play=='O'):
        total=sumo-sumx
    #temp_file.write("temp: %s"%total)    
    return total   
         
def minmax_sneak(p,point,play):
    i=point[0]
    j=point[1]
    
    sum = minmax_Eval(p,play[0])
    #temp_file.write("i: %s"%i)
    #temp_file.write(" j: %s"%j)
    #a=traverse(i,j)
    #temp_file.write("\n%s "%a)
    #temp_file.write(" sneak sum: %s\n"%-sum)
    return sum
    
flag1=0
       
def minmax_raid(p,point,play):
    i=point[0]
    j=point[1]
    #temp_file.write(" play: %s"%play)
    #print i,j
    
    s=0
    a=0
    global flag1
    
    if play=='X':
        #temp_file.write("yo man\n")
        if(i-1>=0 and i-1<5):
            if p[i-1][j]=='O':
                a=1
                if flag1==0:
                    s=minmax_Eval(p,play[0])
                    flag1=1
                elif flag1==1:
                    s=s
                    
        if(i+1>=0 and i+1<5):
            if p[i+1][j]=='O':
                a=1
                if flag1==0:
                    s=minmax_Eval(p,play[0])
                    flag1=1
                elif flag1==1:
                    s=s
                    
        if(j-1>=0 and j-1<5):
            if p[i][j-1]=='O':
                a=1
                if flag1==0:
                    s=minmax_Eval(p,play[0])
                    flag1=1
                elif flag1==1:
                    s=s
                    
        if(j+1>=0 and j+1<5):
            if p[i][j+1]=='O':
                a=1
                if flag1==0:
                    s=minmax_Eval(p,play[0])
                    flag1=1
                elif flag1==1:
                    s=s
        
            
    elif play=='O':
        if(i-1>=0 and i-1<5):
            if p[i-1][j]=='X':
                a=1
                if flag1==0:
                    s=minmax_Eval(p,play[0])
                    flag1=1
                elif flag1==1:
                    s=s
                    
        if(i+1>=0 and i+1<5):
            if p[i+1][j]=='X':
                a=1
                if flag1==0:
                    s=minmax_Eval(p,play[0])
                    flag1=1
                elif flag1==1:
                    s=s
                    
        if(j-1>=0 and j-1<5):
            if p[i][j-1]=='X':
                a=1
                if flag1==0:
                    s=minmax_Eval(p,play[0])
                    flag1=1
                elif flag1==1:
                    s=s
                    
        if(j+1>=0 and j+1<5):
            if p[i][j+1]=='X':
                a=1
                if flag1==0:
                    s=minmax_Eval(p,play[0])
                    flag1=1
                elif flag1==1:
                    s=s
                    
    if a==0:
        #temp_file.write("yo aneri\n")
        s = minmax_Eval(p,play[0])
        #temp_file.write("s: %s"%s)
    flag1=0
    #temp_file.write("i: %s"%i)
    #temp_file.write(" j: %s"%j)
    #a=traverse(i,j)
    #temp_file.write("\n%s "%a)
    #temp_file.write(" raid sum: %s\n"%-s)
    return s
    
         
flag=0
       
def raid(i,j,p):
    #print i,j
    s=0
    a=0
    global flag
    
    if p=='X':
        if(i-1>=0 and i-1<5):
            if position[i-1][j]=='O':
                a=1
                if flag==0:
                    s=Eval(p)+2*int(grid[i-1][j])+s+int(grid[i][j])
                    flag=1
                elif flag==1:
                    s=s+2*int(grid[i-1][j])
                    
        if(i+1>=0 and i+1<5):
            if position[i+1][j]=='O':
                a=1
                if flag==0:
                    s=Eval(p)+2*int(grid[i+1][j])+s+int(grid[i][j])
                    flag=1
                elif flag==1:
                    s=s+2*int(grid[i+1][j])
                    
        if(j-1>=0 and j-1<5):
            if position[i][j-1]=='O':
                a=1
                if flag==0:
                    s=Eval(p)+2*int(grid[i][j-1])+s+int(grid[i][j])
                    flag=1
                elif flag==1:
                    s=s+2*int(grid[i][j-1])
                    
        if(j+1>=0 and j+1<5):
            if position[i][j+1]=='O':
                a=1
                if flag==0:
                    s=Eval(p)+2*int(grid[i][j+1])+s+int(grid[i][j])
                    flag=1
                elif flag==1:
                    s=s+2*int(grid[i][j+1])
        
            
    elif p=='O':
        if(i-1>=0 and i-1<5):
            if position[i-1][j]=='X':
                a=1
                if flag==0:
                    s=Eval(p)+2*int(grid[i-1][j])+s+int(grid[i][j])
                    flag=1
                elif flag==1:
                    s=s+2*int(grid[i-1][j])
                    
        if(i+1>=0 and i+1<5):
            if position[i+1][j]=='X':
                a=1
                if flag==0:
                    s=Eval(p)+2*int(grid[i+1][j])+s+int(grid[i][j])
                    flag=1
                elif flag==1:
                    s=s+2*int(grid[i+1][j])
                    
        if(j-1>=0 and j-1<5):
            if position[i][j-1]=='X':
                a=1
                if flag==0:
                    s=Eval(p)+2*int(grid[i][j-1])+s+int(grid[i][j])
                    flag=1
                elif flag==1:
                    s=s+2*int(grid[i][j-1])
                    
        if(j+1>=0 and j+1<5):
            if position[i][j+1]=='X':
                a=1
                if flag==0:
                    s=Eval(p)+2*int(grid[i][j+1])+s+int(grid[i][j])
                    flag=1
                elif flag==1:
                    s=s+2*int(grid[i][j+1])
                    
    if a==0:
        s = Eval(p)+int(grid[i][j])
        
    
    global R_max
    global R_i
    global R_j
   # print s
    if s > R_max:
         R_max = s
         R_i=i
         R_j=j
    flag=0
    
def update_adj(i,j,p):
    if p=='X':
        if(i-1>=0 and i-1<5):
            if position[i-1][j]=='O':
                position[i-1][j]='X'
                    
        if(i+1>=0 and i+1<5):
            if position[i+1][j]=='O':
                position[i+1][j]='X'
               
        if(j-1>=0 and j-1<5):
            if position[i][j-1]=='O':
                 position[i][j-1]='X'
                    
        if(j+1>=0 and j+1<5):
            if position[i][j+1]=='O':
                position[i][j+1]='X'
                
                
    elif p=='O':
        if(i-1>=0 and i-1<5):
            if position[i-1][j]=='X':
                position[i-1][j]='O'
                    
        if(i+1>=0 and i+1<5):
            if position[i+1][j]=='X':
                position[i+1][j]='O'
                    
        if(j-1>=0 and j-1<5):
            if position[i][j-1]=='X':
                position[i][j-1]='O'
                    
        if(j+1>=0 and j+1<5):
            if position[i][j+1]=='X':
                position[i][j+1]='O'
                
                
                
def raidupdate_adj(i,j,player,p_clone):
    if player=='X':
        if(i-1>=0 and i-1<5):
            if p_clone[i-1][j]=='O':
                p_clone[i-1][j]='X'
                    
        if(i+1>=0 and i+1<5):
            if p_clone[i+1][j]=='O':
                p_clone[i+1][j]='X'
               
        if(j-1>=0 and j-1<5):
            if p_clone[i][j-1]=='O':
                 p_clone[i][j-1]='X'
                    
        if(j+1>=0 and j+1<5):
            if p_clone[i][j+1]=='O':
                p_clone[i][j+1]='X'
                
                
    elif player=='O':
        if(i-1>=0 and i-1<5):
            if p_clone[i-1][j]=='X':
                p_clone[i-1][j]='O'
                    
        if(i+1>=0 and i+1<5):
            if p_clone[i+1][j]=='X':
                p_clone[i+1][j]='O'
                    
        if(j-1>=0 and j-1<5):
            if p_clone[i][j-1]=='X':
                p_clone[i][j-1]='O'
                    
        if(j+1>=0 and j+1<5):
            if p_clone[i][j+1]=='X':
                p_clone[i][j+1]='O'

                
               
                
def avail(position):
    available=[] 
    for i in xrange(5):
        
        for j in xrange(5):
            if (position[i][j]!='X' and position[i][j]!='O' ):
                l=[]
                
                l.append(i)
                l.append(j)
                available.append(l)
                
    return available
    
def next_sneak(a,player,p):
    p_clone=p[:]
    [i,j]=a
        
    
    p_clone[i][j]=player[0]
    return p_clone
    
    
def next_raid(a,player,p):
       p_clone=deepcopy(p)
       
       [i,j]=a
       raidupdate_adj(i,j,player[0],p_clone)    

       p_clone[i][j]=player[0]
#       for o in xrange(5):
#        for p in xrange(5):
#          item=p_clone[o][p]
#        #print item,
#    #print     
#          temp_file.write("%s" % item)
#        temp_file.write("\n")
       return p_clone
    
    
def op_player(player):
    if(player[0]=='X'):
        return 'O'
    else:
        return 'X'  
        
        
def op_adj(player,p):
   
   op_adj = []  
   for i in xrange(5):
      for j in xrange(5):
       
       if p[i][j] == player[0]:
           op_adj= find_adjacent(i,j,op_adj)
   return op_adj




best_move=[]  
  
def minmax(position,grid,player):
    posible_moves=[]
    depth=1
    posible_moves=avail(position)
    
    score=float('inf')
    best_move=posible_moves[0]
    best_score=float('-inf')
    print best_score
    print best_move
    if(best_score == float('-inf')):
        k ="-Infinity"
    temp_file.write("Node,Depth,Value\n")
    temp_file.write("root")
    temp_file.write(",0")
    temp_file.write(",%s \n"%k)
    adj1=op_adj(player,position)
    
    for i in xrange(len(posible_moves)):
##           [e,r]=posible_moves[i] 
#            y1=traverse(e,r)
#            temp_file.write("%s" % y1)
#            temp_file.write(",%s" % depth)
#            temp_file.write(",Infinity\n")
        p=deepcopy(position)
        if(posible_moves[i]  not in adj1): 
            print "posible\n"
            print posible_moves[i],i
            #temp_file.write("posible")
            #temp_file.write("player: %s \n" % player)
            #temp_file.write("%s " % posible_moves[i])
            #temp_file.write("%s \n" % i)
        
            s=next_sneak(posible_moves[i],player,p)
            sc=min_play(s,posible_moves[i],"sneak",player,depth)
        
        else :
            #temp_file.write("posible ")
            #temp_file.write("%s " % posible_moves[i])
            #temp_file.write("%s \n" % i)
            r=next_raid(posible_moves[i],player,p)
            sc=min_play(r,posible_moves[i],"raid",player,depth)
        
        if sc[0] > best_score:
            best_move=posible_moves[i]
            best_score=sc[0]
        if(int(cutoff[0])==1):
            [e,r]=posible_moves[i] 
            y1=traverse(e,r)
            temp_file.write("%s" % y1)
            temp_file.write(",%s" % depth)
            temp_file.write(",%s\n"%sc[0])
        temp_file.write("root")
        temp_file.write(",0")
        temp_file.write(",%s\n"%best_score)
        score=float('inf')
    #temp_file.write("minmax best score: ")
    #temp_file.write("%s\n" % best_score)
    return best_move
            
    
        
def min_play(p,point,s,play,depth):
    min_depth=depth
    if (min_depth==int(cutoff[0])):
        if(s=="sneak"):
             return [minmax_sneak(p,point,play),-1,-2]
        else:
             return [minmax_raid(p,point,play),-1,2]
        
    min_depth=min_depth+1
    min_moves=[]
    min_moves=avail(p)
    best_score=float('inf')
    op=op_player(play)
    op_adj1=op_adj(op,p)
   
    
#    for jj in xrange(len(op_adj1)):
#        item=op_adj1[jj]
#        #print item,
#    #print     
#        temp_file.write(" %s" % item)
#        temp_file.write("\n")    
#    

    if(best_score==float('inf')):
         q1='Infinity'

    [e,r]=point
    y1=traverse(e,r)
    temp_file.write("%s" % y1)
    temp_file.write(",%s" % depth)
    temp_file.write(",%s\n"%q1)
    
    
    for i in xrange(len(min_moves)):
        #print min_depth
        p2=deepcopy(p)
        if(min_moves[i]  not in op_adj1):
           # print "posible"
            min_s=next_sneak(min_moves[i],op,p2)
            print "min moves s",i
            print min_moves[i] 
            #temp_file.write("min moves s ")
            #temp_file.write("%s " % i)
            #temp_file.write("%s \n" % min_moves[i])
            #print "min s"
            #print min_s
            sc=max_play(min_s,min_moves[i],"sneak",play,min_depth)
            if(sc[1]!=sc[2]):
                [q,w]=min_moves[i]
                e=traverse(q,w)
                temp_file.write("%s" % e)
                temp_file.write(",%s" % min_depth)
                #temp_file.write(" ,score s:")
                temp_file.write(",%s\n" % sc[0])
    
        else:
            min_r=next_raid(min_moves[i],op,p2)
            print "min moves r",i           
            print min_moves[i]
            #temp_file.write("min moves r ")
            #temp_file.write("%s " % i)
            #temp_file.write("%s \n" % min_moves[i])
            #print "min r"
            #print min_r
            sc=max_play(min_r,min_moves[i],"raid",play,min_depth)
            if(sc[1]!=sc[2]):
                [q,w]=min_moves[i]
                e=traverse(q,w)
                temp_file.write("%s" % e)
                temp_file.write(",%s" % min_depth)
                #temp_file.write("  ,score r:")
                temp_file.write(",%s\n" % sc[0])
        if sc[0]<best_score:
            best_move=min_moves[i]
            best_score=sc[0]
            
        
        e1=traverse(point[0],point[1])
        #temp_file.write("min_play best score:")
        temp_file.write("%s" % e1)
        temp_file.write(",%s" % str(int(min_depth)-1))
        temp_file.write(",%s\n" % best_score) 
            #temp_file.write("point: ")
            #temp_file.write(" [%s" % point[0] )
            #temp_file.write(" %s]\n" % point[1] )
        l1=[]
        l1.append(best_score)
        l1.append(i)
        l1.append(len(min_moves)-1)
    return l1
    
def max_play(p,point,s,play,depth):
     
     max_depth=depth
     if (max_depth==int(cutoff[0])):
         if(s=="sneak"):
             return [minmax_sneak(p,point,play),-1,-2]
         else:
             return [minmax_raid(p,point,play),-1,-2]
         
     max_depth=max_depth+1
     max_moves=[]
     max_moves=avail(p)
     best_score=float('-inf')
     #op=op_player(play)
     adj1=op_adj(player,p)
    #print "adjcent"
    #print adj
     if(best_score==float('-inf')):
         q1='-Infinity'
     
     [e,r]=point
     y1=traverse(e,r)
     temp_file.write("%s" % y1)
     temp_file.write(",%s" % depth)
     temp_file.write(",%s\n"%q1)     
     
     for i in xrange(len(max_moves)):
        #print max_depth
        p1=deepcopy(p)
        if(max_moves[i]  not in adj1):
           # print "posible"
            s=next_sneak(max_moves[i],player,p1)
#            print "max moves s",i
#            print max_moves[i]
#            temp_file.write("max moves s ")
#            temp_file.write("%s " % i)
#            temp_file.write("%s\n" % max_moves[i])
            sc=min_play(s,max_moves[i],"sneak",player,max_depth)
            if(sc[1]!=sc[2]):
                [q,w]=max_moves[i]
                e=traverse(q,w)
                temp_file.write("%s" % e)
                temp_file.write(",%s" % max_depth)
                #temp_file.write(" ,score s:")
                temp_file.write(",%s\n" % sc[0])
        
    
        else:
            r=next_raid(max_moves[i],player,p1)
#            print "max moves r",i
#            print max_moves[i]
#            temp_file.write("max moves r ")
#            temp_file.write("%s " % i)
#            temp_file.write("%s \n" % max_moves[i])
            sc=min_play(r,max_moves[i],"raid",player,max_depth)
            
            if(sc[1]!=sc[2]):
                [q,w]=max_moves[i]
                e=traverse(q,w)
                temp_file.write("%s" % e)
                temp_file.write(",%s" % max_depth)
                #temp_file.write("  ,score r:")
                temp_file.write(",%s\n" % sc[0])
            
        if sc[0]>best_score:
            best_move=max_moves[i]
            best_score=sc[0]
     #temp_file.write("max_play best score:")
     #temp_file.write("%s\n" % best_score)
        e1=traverse(point[0],point[1])
       #temp_file.write("min_play best score:")
        temp_file.write("%s" % e1)
        temp_file.write(",%s" % str(int(max_depth)-1))
        temp_file.write(",%s\n" % best_score)
        l1=[]
        l1.append(best_score)
        l1.append(i)
        l1.append(len(max_moves)-1)
     return l1
    
          
        
    
    
    
    
    
    
                
                

    
                         
        
    
             
        
       

Type=data[0]
player=data[1]
cutoff=data[2]
print Type
print player
print cutoff
print Type[0]



S_max=float('-inf')
S_i=-1
S_j=-1

R_max=float('-inf')
R_i=-1
R_j=-1


grid=[]

count=3
while(count<8):
    for i in xrange(5):
    

        grid.append(data[count].split())
        count=count+1
#print grid


position=[]
j=0
while(count<13):

    x=data[count]


    position.append([])
    for i in xrange(0,len(x)-1):
        position[j].append(x[i])

    j=j+1
    count=count+1
    
#print position
if (Type[0]=='2'):
        
    move=[]
    print "Hi"
    move=minmax(position,grid,player[0])
    #if(move==[-1,-1]):
        
    print 'final move'
    print move  
    i=move[0]
    j=move[1]
    position[i][j]=player[0]
    update_adj(i,j,player[0])
    print "minmax ans:"
    print position
    #temp_file.write("final move:")
    #temp_file.write("%s" % move)
    f=open("next_state.txt","w+")

    for i in xrange(5):
        for j in xrange(5):
          item=position[i][j]
        #print item,
    #print     
          f.write("%s" % item)
        f.write("\n")    



adj = []
if (Type[0]=='1'):
   print "greedy"
   for i in xrange(5):
      for j in xrange(5):
       
         if position[i][j] == player[0]:
           adj= find_adjacent(i,j,adj)
           
           
           


#print adj

   for i in xrange(5):
        for j in xrange(5):
            if (position[i][j]!='X' and position[i][j]!='O' and [i,j] not in adj):
                #print grid[i][j]
                 sneak(i,j)
               
#
#print S_max
#print S_i
#print S_j
   for i in xrange(len(adj)):
      [a,b]=adj[i]
      raid(a,b,player[0])

    
   print S_max
   print R_max
   print S_i
   print S_j
               

   if(S_max>R_max):
     position[S_i][S_j]=player[0]
   else:
     position[R_i][R_j]=player[0]
     update_adj(R_i,R_j,player[0])
    
    
   print 'ans:'
   print position
   f=open("next_state.txt","w+")

   for i in xrange(5):
      for j in xrange(5):
         item=position[i][j]
        #print item,
    #print     
         f.write("%s" % item)
      f.write("\n")    

    


  
  










    
    
    

    










    
    
    

