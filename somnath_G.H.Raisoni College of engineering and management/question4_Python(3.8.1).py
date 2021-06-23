
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:53:16 2021

@author: samac
"""
            
    
    
    
    
    
    
def main():
    n=int(input())
    res=1
    s=list(map(int,input().split()))
    
    q=int(input())
        
    for i in range(q):
        st=s
        l,r=map(int,input().split())
        li=s.index(l)
        ri=s.index(r)
        
        a=st.pop(li-1)
        b=st.pop(ri-1)
        r=1
        for f in(st):
            r+=a^f * b^f
            print(r)
        res+=r*(a^b)
    print(res)
    
main()
