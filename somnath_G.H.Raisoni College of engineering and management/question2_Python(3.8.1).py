#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:20:34 2021

@author: samac
"""


def main():
    n=int(input())
    
    g1,g2=[],[]
    count=0
    
    g1=list(map(int,input().split()))
    g2=list(map(int,input().split()))
    
    for i in range(n):
        g1.sort()
        g2.sort()
        
        if(g1[0]<g2[0]):
            x=g1.pop(0)
        else:
            x=g2.pop(0)
            
        count+=x
        
    print(count)
    
main()
