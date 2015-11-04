"""This module makes fake data of a gaussian with some random noise.
Specify the start,stop and number of points of the independent variable, as wel as the mean and variance of the gaussian 
"""

import numpy as np
import matplotlib.pyplot as plt


#simulates a gaussian with random noise

def data(start=-10, stop=10, num=100,mu=1,sig=1):
    x=np.linspace(start=-10, stop=10, num=100)
    gaussian=np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


    return x, data=gaussian+0.2*np.random.randn(len(x))  #add noise to data
   