# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:54:13 2019

@author: Owner
"""

# 最大有効数字６桁
def gal2L(gal):
    return 3.78541 * gal

def L2gal(L):
    return L/3.78541
# 最大有効数字５桁
def oz2g(oz):
    return oz/0.035274

def g2oz(g):
    return g*0.035274

def calcHBU(batch_size, hops):
    w_alpha = sum([hop.alpha*hop.oz for hop in hops])
    HBU = w_alpha/batch_size
    return HBU

class Hop():
    def __init__(self, name, alpha, g):
        self.name = name
        self.alpha = alpha
        self.oz = g2oz(g)
        
cascade = Hop("Cascade", 6.2, 40)
nugget  = Hop("Nugget", 15.1, 20)

hops = [cascade, nugget]
batch_size = L2gal(11) # gal

print(calcHBU(batch_size, hops))