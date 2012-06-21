# section Lab03_2a
count=0
for i in range(1,7):
    for j in range(1,7):
        if i==1:
            print j, 
            print '\n',
            break
        if i==2:
            print j,
            count+=1
            if count==i:
                print '\n',
                break
        if i==3:
            print j,
            count+=1
            if count==(i+2):
                print '\n',
                break   

        if i==4:
            print j,
            count+=1
            if count==(i+5):
                print '\n',
                break

        if i==5:
            print j,
            count+=1
            if count==(i+9):
                print '\n',
                break 

        if i==6:
            print j,
            count+=1
            if count==(i+14):
                print '\n',
                break


print '\n\n # section Lab03_2b'


for i in range(7,1, -1):
    count=0
    for j in range(1,7):
        if i==7:
            print j,
            count+=1
            if count==(i-1):
                print '\n',
                break
        if i==6:
            print j,
            count+=1
            if count==(i-1):
                print '\n',
                break
        if i==5:
            print j,
            count+=1
            if count==(i-1):
                print '\n',
                break
        if i==4:
            print j,
            count+=1
            if count==(i-1):
                print '\n',
                break
        if i==3:
            print j,
            count+=1
            if count==(i-1):
                print '\n',
                break
        if i==2:
            print j,
            count+=1
            if count==(i-1):
                print '\n',
                break


print '\n\n# section Lab03_2c '

for i in range(1,7, 1):
    count=0
    for j in range(6,0,-1):
        if i==1:
            print ' ',
            count+=1
            if count==(6):
                print j,'\n',
                break
       
        if i==2:
            if count==5:
                print j,'\n',
                break
            else:
                print ' ',
            count+=1
            if count==5: 
                print j,

        if i==3:
            if count==4 :
                print j,
            if count==5:
                print j,'\n',
                break            
            elif count!=4 and count!=5:
                print ' ',

            count+=1
          
            if count==4: 
                print j,

        if i==4:
            if count==3 :
                print j,
            if count==4:
                print j,
                
            if count==5:
                print j,'\n',
                break    
            elif count!=3 and count!=4:
                print ' ',

            count+=1
          
            if count==3: 
                print j,


        if i==5:
            if count==2 :
                print j,
            if count==3:
                print j,
                
            if count==4:
                print j,
                
            if count==5:
                print j,'\n',
                break            
            elif count!=2 and count!=3 and count!=4:
                print ' ',

            count+=1
          
            if count==2: 
                print j,


        if i==6:
            if count==1 :
                print j,
            if count==2:
                print j,
                
            if count==3:
                print j,
            if count==4:
                print j,
            if count==5:
                print j,'\n',
                break            
            if count==0:
                print ' ',

            count+=1
          
            if count==1: 
                print j,
            
                
        


 


print '\n\n# section Lab03_2d '

for i in range(6,0, -1):
    count=0
    for j in range(1,7):
       
        if i==6:
            if count==1 :
                print j,
            if count==2:
                print j,
                
            if count==3:
                print j,
            if count==4:
                print j,
            if count==5:
                print j,'\n',
                break            
            if count==0:
                print ' ',

            count+=1
          
            if count==1: 
                print j,

        
      
        if i==5:
            if count==4:
                print j,'\n',
                break
            if count!=2 or count!=3 or count!=4 or count!=1:
                print ' ',
            count+=1
            if count==4: 
                print j-1,
            if count==3: 
                print j-1,
            if count==2: 
                print j-1,

        if i==4:
            if count==4 :
                print j,
            if count==5:
                print j,'\n',
                break            
            elif count!=4 and count!=5:
                print ' ',

            count+=1
          
            if count==4: 
                print j,

        if i==3:
            if count==3 :
                print j,
            if count==4:
                print j,
                
            if count==5:
                print j,'\n',
                break    
            elif count!=3 and count!=4:
                print ' ',

            count+=1
          
            if count==3: 
                print j,


        


        
            
        
    
