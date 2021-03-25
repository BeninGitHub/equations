#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:21:00 2021

@author: bnzr
"""


def exp(x:float) ->float:
    var1=100
    e=1.0
           
    for i in range(var1):
        var2=1
        if i==0:
            continue
        for j in range(i):
                  j=j+1
                  var2=var2*j

        var3=x
        for ii in range(i):
            if ii==0:
                continue
            else:
                var3=var3*x
        e=e+(var3/var2)
    return e

 
def Ln(x:float) ->float:
    EP = 0.001
    
    if x<0 :
        x=x*-1
    varY= x-1.0
    exp1 = exp(varY)
    varY1= varY +2*((x-exp1)/(x+exp1))
    Y1 = varY - varY
    if (Y1) < 0:
        Y1= Y1*-1
        
    while (Y1) > EP:
        exp1 = exp(varY)
        varY = varY1
        varY1= varY +2*((x-exp(varY))/(x+exp(varY)))
        Y1 = varY - varY
        if (Y1) < 0:
            Y1= Y1*-1  
    return varY1
    

def XtimesY(x:float,y:float) ->float:
    xy = exp(y*Ln(x))
    if (x<0) :
        return(0)
    elif x==0:
        return(0)
    else:
        return(xy)
    
   
    
def sqrt(x:float,y:float) ->float:
    if (y<0):
        return(0)
    elif y==0:
        return(0)
    else:
        return(exp((1/x)*Ln(y)))



def calculate(x:float) ->float:
    c = exp(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)   
    return c