# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:02:02 2022

@author: tonit
"""

def checkIfPrime(numberToCheck):
    for x in range(2,numberToCheck):
        if (numberToCheck%x==0):
            return False
        return True