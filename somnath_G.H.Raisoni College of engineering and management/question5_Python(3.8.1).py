#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 18:06:19 2021

@author: samac
"""

def pos(n,a,b):
    res = n - max(a + 1, n - b) + 1;
    print(res)
    
    
    
def main():
    n,a,b=map(int,input().split())
    pos(n,a,b)
    
main()
