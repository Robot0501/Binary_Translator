# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:01:21 2024

@author: RobotNinja
"""

ASCII = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """

dictionary = []


b = 0

for a in ASCII:
    dictionary.append(ASCII[b])
    b+=1

#print(dictionary)
    
word = input("Enter word: ")

pos = 0
bina = 1
remainder = 0

Binary = ' '

for a in word:
    
    for b in dictionary:
        
        if a == '0':
            Binary = "00000000"
        
        elif a == b:
            
            for c in range(1,9):
                remainder = pos%2
                #print(str(remainder) + '       ' + str(pos) + "       " + str(bina))
                
                if bina==1:
                    bina+=1
                else:
                    bina = 2**c
                
                pos = int(pos/2)
                if remainder==1:
                    Binary = Binary + '1'
                elif remainder==0:
                    Binary = Binary + '0'
            break
        else:
            pos+=1
    Binary = Binary + ' '
          
    pos = 0

print(word + " in binary is " + Binary)
                
            
        
