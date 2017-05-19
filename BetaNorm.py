# -*- coding: utf-8 -*-
"""
Created on Mon May 15 15:56:05 2017

@author: philip.ball
"""

# Quick and dirty function to validate approximations of the normal curve with a beta distribution.
# Equations thanks to https://www.johndcook.com/blog/normal_approx_to_beta/

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Set your beta parameters, and optionally set a parameter for the normal
# If you don't set the scaling parameter for the normal, it just equates the variances/stdevs
# Note that the beta function only goes between 0 and 1

def normVSbeta(a,b,scale = -100):
    
    x = np.linspace(0,1,1000)
    
    loc = a/(a+b)
    
    if scale == -100:
        scale = np.sqrt(a*b/((a+b)**2*(a+b+1)))
        
    beta = stats.beta.pdf(x,a,b)
    norm = stats.norm.pdf(x,loc,scale)
    
    error = beta - norm
        
    e_max = max(abs(error))
    
    beta_p, = plt.plot(x,beta)
    norm_p, = plt.plot(x,norm)
    plt.title('Normal vs Beta')
    plt.legend([beta_p,beta_p],['Beta','Normal'])
    plt.show()
    plt.gcf().clear()
    plt.title('Error Term')
    plt.plot(x,error)
    plt.show()
    plt.gcf().clear()
    print('The max error is: ' + str(e_max))

# run with centred beta dist
normVSbeta(6,6)

# run with a manual SD
normVSbeta(5,5,1/6)

# run with an unbalanced beta dist
normVSbeta(4,6)