### Imports ###
import os
import numpy as np
from numpy import random as rnd
from scipy.stats import t
from scipy.stats import beta
import seaborn as sns
import matplotlib.pyplot as plt

### Parameters ###
nu = 3 # arbitrary choice
sigma = 2 # arbitrary choice

### Simulate Values ###
draws1 = rnd.standard_t(nu, size = 1.e6) # draw one million Y values
draws2 = t.cdf(draws1, df = nu) # classic PIT (F_Y(Y) is standard uniform)
draws3 = t.cdf(draws1 / sigma, df = nu) # compute one million X values based on Y values
alpha_fit, beta_fit, loc_fit, scale_fit = beta.fit(draws3) # determine best-fitted beta

### Plot KDEs and CDF of Best-Fitted Beta PDF ###
kdeFig = plt.figure() # start figure
sns.set("talk") # set seaborn style to "talk" --> increase font size
# add all KDEs with plot labels in LaTeX (hence the use of raw strings)
sns.kdeplot(draws1, shade = True, clip = (-3, 3), label = r'KDE for $Y \sim t_3$')
sns.kdeplot(draws2, shade = True, clip = (-3, 3), label = r'KDE for $F_Y(Y)$')
sns.kdeplot(draws3, shade = True, clip = (-3, 3), label = r'KDE for $X$ with $\sigma = 2$')
# add pdf for best-fitted beta with plot labels in LaTeX (hence the use of raw strings)
x = np.linspace(-3,3, num = 1000) # create 1000 values between -3 and +3
y = beta.pdf(x, a = alpha_fit, b = beta_fit, loc = loc_fit, scale = scale_fit) # f(x)
plt.plot(x, y, label = r'PDF for Best-Fitted $B(\alpha, \beta)$')
# title & legend
plt.title('Kernel Density Estimation')
plt.legend(loc='upper left')
os.chdir('../Figures/') # navigate to "Figures" folder
plt.savefig('4c.pdf') # store figure as pdf
plt.close(kdeFig)