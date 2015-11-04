"""This module makes moke data of a gaussian with some random noise"""

import numpy.random as npr
from scipy.optimize import leastsq
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

def fake_gauss(x,mu,sig)
#make fake data with gaussian
#mu = mean
#sig= std deviation

    fake_data=np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


    fake_data_n=fake_data+0.2*npr.randn(len(x))  #add noise to data



    #plot data
    plt.plot(x,fake_data_n)

#np.show()