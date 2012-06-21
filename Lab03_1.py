import math
count=0
for n in range(1, 1000):
    nroot=n**0.5
    if n==2 or n==3:
        print n ,
        count+=1
        continue
    elif n<2:
        print ' '
    prime = True
    for c in range(2,(int(nroot)+1)):
            if n%c==0:
                prime = False
                break

    if prime == True:
        count+=1
        if count==11 or count==21 or count==31 or count==41:
            print n , '\n',
        else :
            print n,
        
    if count==53:
        break
    
        


        
        
        
            
            
    
        



        
    

            
    
        
