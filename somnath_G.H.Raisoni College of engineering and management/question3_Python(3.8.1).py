#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:30:54 2021

@author: samac
"""

t=int(input())
res=0
for i in range(t):
    r,c=map(int,input().split())
    res+=r*c
    
print(res)
