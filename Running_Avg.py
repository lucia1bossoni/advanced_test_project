def Run_Avg(data=[0], NumAvg=10):
    """Function which smooths noisy data.
    
    This function applies a running average to smooth noisy data. The number of point taken into account for the averaging
    given by 'NumAvg'. To prevent loss of data at the beginning and the end of the data array, the range of the point taken
    in the average is adjusted, so the smoothening is less efficient at the end points.
    
    Parameters:
    -----------
    data: list with the noisy data
    NumAvg: number of points on either side of the central point used to calculate the average.
    """
    
    smoothdata = []
    
    for x in range(len(data)):
        if x - NumAvg < 0:
            x_min = 0
        else:
            x_min = x - NumAvg
        
        if x + NumAvg > len(data):
            x_max = len(data)
        else:
            x_max = x + NumAvg
        
        smoothdata.append( sum(data[x_min:x_max]) / (x_max - x_min) )
    
    return smoothdata