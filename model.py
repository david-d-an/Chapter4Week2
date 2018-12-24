import numpy as np
import h5py
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pylab


def mainfunc():
    plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
    plt.rcParams['image.interpolation'] = 'nearest'
    plt.rcParams['image.cmap'] = 'gray'

    np.random.seed(1)
 
