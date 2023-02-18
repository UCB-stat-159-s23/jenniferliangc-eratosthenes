import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def plot_sieve(x, y, log_scale = True):
    if log_scale == True:
        plt.plot(x, y)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")
        plt.xscale("log")
        plt.yscale("log")
    else:    
        plt.plot(x, y)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")
    
