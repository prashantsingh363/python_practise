'''
Created on Oct 15, 2018

@author: prashant
'''
num = int(input(" Enter a num"))
if (num%2)==0:
    print("Even")
    if(num%4)==0:
        print("number divisible by 4")
    else:
            print("nothing")
    
else:
    print("Odd")