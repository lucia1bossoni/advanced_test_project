"""This module makes fake data of a gaussian with some random noise.
Specify the start,stop and number of points of the independent variable, as wel as the mean and variance of the gaussian 
"""



#simulates a gaussian with random noise

def fake_gauss(np.linspace(start=-10, stop=10, num=100),mu=1,sig=1):
    x=np.linspace(start=-10, stop=10, num=100)
    fake_data=np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


    fake_data_n=fake_data+0.2*np.random.randn(len(x))  #add noise to data



    #plot data
    plt.plot(x,fake_data_n)

#np.show()