#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:21:36 2021

@author: samac
"""

def main():
    
    n=int(input())
    
    p=[]
    p=list(map(str,input().split()))
    #print(p)
    
    m=int(input())
    
    for i in range(m):
        cmd=[]
        cmd=list(map(str,input().split(" ")))
        
        if(cmd[0]=="SERVE"):
           p.pop(0) 
        elif(cmd[0]=="FRIEND"):
            if(cmd[2] in p):
                p.insert(p.index(cmd[2]),cmd[1])
           
        elif(cmd[0]=="VIP"):
            p.insert(0,cmd[1])
            
    print(p)
            
            
main()
