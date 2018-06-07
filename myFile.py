import sys
import random
a = [0,1,2,3,4,5,6,7,8,9]
Bwin = False
Awin = False

totalA = 0
totalB = 0
count = 0
while(len(a)>0):
    if(count == 0):
        b = int(input("Player 1 Turn"))
        if(b in a):
            count+=1
            totalA += b
            a.remove(b)
        else:
            print("Cannot choose this")
        
    else:
        
        count -=1
        c = random.choice(a)
        a.remove(c)
        totalB += c
        print("Computer choosed " , str(c) )
        
        
    if(totalA >= 21):
        Awin = True
    if(totalB >= 21):
        Bwin = True
        
if(Awin and Bwin):        
    totalA = totalA - 21
    totalB = totalB - 21
    if(totalA < totalB):
        print("Player one-- is winner")
        sys.exit('listofitems not long enough')
    else:
        print("Player two-- is winner")
        sys.exit('listofitems not long enough')
elif(Awin):
    print("Player one-- is winner")
else:
    print("Player two-- is winner")
    
