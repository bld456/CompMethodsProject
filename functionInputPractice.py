# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 16:29:54 2017

@author: Jack
"""

def shovel(num):
    
    if num==7:
         treasure = "pot 'o gold"
         
    else:
        treasure = "dead body"
    return treasure
    
num=input("where will you dig? (an int)")
print shovel(num)