### Imports ###
import math
import numpy as np
import scipy.special as special
from scipy.integrate import quad, dblquad
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import codecs

### Define & Create Variables ###
pList = np.linspace(-3, 3, num=50) # generate 50 values for p for comparison
mList = range(3,10,2) # test every other value of m until 9 (M = 4)
normcdfList = norm.cdf(pList) # generate 50 values for the p with std. normal cdf for comparison

numInt = plt.figure() # start figure...

### Do Double Numeric Integration to Estimate values for the CDF of P ###
for eachParam in mList: # do it for all M values of m
	cdfList = [] # create empty list to store estimated CDF values
	m = eachParam # shorter notation
	# estimate the constant
	const = special.gamma(m-1) * 2**(3*(1-m/2)) / (special.gamma(m/2) * special.gamma((m-1)/2) * special.gamma((m-1)/2) )
	for eachPoint in pList: # estimate F_P(p) for all 50 data points (-3 to 3)
		cdf = dblquad(lambda t, p: const * 1/abs(t) * (p/t)**(m-1) * np.exp(-0.5*(p/t)**2) * (1-t**2)**((m-3)/2), -np.inf, eachPoint, lambda p: 0, lambda p: 1)
		cdf = cdf[0] # extract approximation and toss error term
		cdfList.append(cdf) # append approximation to list for comparison
	plotLabel = r'CDF of $P \,$ with $m=$' + str(m) # raw string for LaTeX
	plt.plot(pList, cdfList, label=plotLabel) # plot approx. cdf

### Finish Plot ###
plt.plot(pList, normcdfList, label=r'CDF of Std. Normal RV') # raw string for LaTeX
plt.title('CDFs Approximated Using Numeric Integration')
plt.legend(loc='lower right')
os.chdir('../Figures/') # navigate to "Figures" folder
plt.savefig('13.pdf') # store figure as pdf
plt.close(numInt)

### Create LaTeX Table with Comparison for m = 9 ###
diffList = abs(cdfList - normcdfList) # list of absolute values of differences
comparisonDF = pd.DataFrame({'Input Value' : pList, 'Num. Integration' : cdfList, 'Normal CDF' : norm.cdf(pList), 'Absolute Difference' : diffList})
comparisonDF = comparisonDF[['Input Value', 'Num. Integration', 'Normal CDF', 'Absolute Difference']]
comparisonDF.drop(range(1,48,2), axis=0, inplace = True) # drop every other row (readability)
# export table to a .tex file that is loaded by my LaTeX document...reproducibility FTW
table = comparisonDF.to_latex(index = False)
writeFile = codecs.open('NumericIntegration.tex','w', 'utf-8')
writeFile.write(table)
writeFile.close()