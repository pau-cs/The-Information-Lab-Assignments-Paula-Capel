# -*- coding: utf-8 -*-
"""
Created on Dec 22 2023

@author: Paula Capel Silveiro 

Create and call a python function that : 
- stores a random integer A between 1 and 9
- stores a random integer B between 1 and 9
- multiplies A and B together as C
- Prints A and C for every result until C = 4
- If C = 4 , print ‘Success!’ and the results for A and B
- Store your code on a GitHub account and share it with the email-address given in the SQL test, including your CV

"""

import numpy as np 

def functiongetC():
    C=0
    while C!=4:
        A=np.random.randint(1,10) #Store a random integer A between 1 and 9
        B=np.random.randint(1,10) #Store a random integer B between 1 and 9
        C=A*B # Multiply A and B together as C
        print("A:"+str(A)+" and C:"+str(C)) #Prints A and C for every result until C = 4
    print("Success! A:"+str(A)+ " and B:"+str(B)) #If C = 4 , print ‘Success!’ and the results for A and B

functiongetC()    
