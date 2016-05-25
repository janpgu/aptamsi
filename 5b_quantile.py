### Imports ###
import os
import numpy as np
from numpy import random as rnd
from scipy.stats import t
from scipy.stats import beta
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')

p = np.arange(0, 1, 0.01)
q = (2*p-1) / np.sqrt(2*p*(1-p))

quantPlot = plt.figure() # start figure
plt.plot(p, q, label=r'$F_X^{-1}(p)$')
plt.title('Quantile Function')
plt.legend(loc='upper left')
os.chdir('../Figures/') # navigate to "Figures" folder
plt.savefig('5b.pdf') # store figure as pdf
plt.close(quantPlot)