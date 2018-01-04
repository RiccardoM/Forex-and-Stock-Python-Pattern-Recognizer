import numpy as np
import matplotlib.dates as mdates

from settings import *

date, bid, ask = np.loadtxt(file_name, unpack=True, delimiter=',',
                            converters={0: mdates.bytespdate2num('%Y%m%d%H%M%S')})
data_length = int(bid.shape[0])

# Creates an array with the average values between the bid and the ask
all_data = ((bid + ask) / 2)

accuracy_array = []
