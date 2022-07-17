# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 11:41:09 2014

@author: Damien Iceta
"""

from numpy import *

def tri_insertion(T):
    for i, v in enumerate(T):
        j = i
        #print u'i',i,'j',j,'v',v,'T=',T
        while 0 < j and v < T[j-1]:
                T[j] = T[j-1]
                j = j-1
                #print u'i',i,'j',j,'v',v,'T=',T
        T[j] = v
    return T
  

def echange(T, i, j):
	T[i], T[j] = T[j], T[i]
 
 
def partition(T, g, d):
    #print "pivot T[g]=",T[g]    
    assert g < d
    v = T[g]	
    m = g
    for i in range(g+1, d):	
        if T[i] < v:
                m = m+1
                echange(T, i, m)		
    if m!= g:
        echange(T, g, m)
    
    return m
 
 
def tri_rapide_rec(T, g, d):
    if g>=d-1: return
    m = partition(T, g, d)
    #print "partition T=",T,"m",m,"g",g,"d",d    
    tri_rapide_rec(T, g, m)
    #print "tri gauche T=",T,"m",m  
    tri_rapide_rec(T,m+1, d) 
    #print "tri droit T=",T,"m",m 
    

def tri_rapide(T): 
        tri_rapide_rec(T, 0, len(T))
        return T
 
 
def fusion(T1, T2, g, m, d):
    i, j = g, m
    #print T2
    for k in range(g, d):
        if i < m and (j == d or T1[i] <= T1[j]):
            T2[k] = T1[i]
            i = i+1
        else:
			T2[k] = T1[j]
			j = j+1
   
def tri_fusion(T):
    tmp = T[:]
    def tri_fusion_rec(g, d):
        if g >= d-1: return
        m = (g+d)//2
        tri_fusion_rec(g, m)
        tri_fusion_rec(m, d)
        tmp[g:d] = T[g:d]
        fusion(tmp, T, g, m, d)        
    tri_fusion_rec(0, len(T)) 
    return T

import time

L1=[]
L2=[]
L3=[]
N=[10,50,70,100,200,300,400,500,600,700,800,1000]
 
for n in N :
    
    T=np.random.rand(n)*10000
    #T=[15,14,11,8,17,7]

    for i in range(len(T)):
        T[i]=int(T[i])

    #print T 
    debut =time.time() 
    sol=tri_rapide(T)
    fin=time.time() 
    L1.append((fin-debut)*1000)
    
    T=np.random.rand(n)*10000
    #T=[15,14,11,8,17,7]

    for i in range(len(T)):
        T[i]=int(T[i])


    debut =time.time() 
    sol2=tri_insertion(T)
    fin=time.time() 
    L2.append((fin-debut)*1000)
    
    T=np.random.rand(n)*10000
    #T=[15,14,11,8,17,7]

    for i in range(len(T)):
        T[i]=int(T[i])


    debut =time.time()
    sol3=tri_fusion(T)
    fin=time.time() 
    L3.append((fin-debut)*1000)

    #print 'Temps', fin-debut
    #print sol
    
print 'fin'


p1=plt.semilogx(N,L1,'r--',marker='o')
#p2=plt.semilogx(N,L2,'b--',marker='v')
p3=plt.semilogx(N,L3,'g--',marker='x')
plt.title("Comparaison en temps des algorithmes de tri")  
plt.ylabel('Temps de Tri en ms')
plt.xlabel('Taille du tableau')
plt.show()

    
    