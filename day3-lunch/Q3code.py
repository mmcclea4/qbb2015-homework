#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

FPKMvalue = []
for num in df["FPKM"]:
    if num != 0:
        FPKMvalue.append(num)
#print FPKMvalue - it works!

#the data set - need the log because the numbers are hard to work with
logFPKMvalue = np.log(FPKMvalue)

#generates a density class from the data
FPKMdensity = gaussian_kde(logFPKMvalue)

#set covariance_factor
#chose lambda : .25 because thats what my example did online and I can't find a great explanation of what this is
    #FPKMdensity.covariance_factor = lambda : .25
    #FPKMdensity._compute_covariance()
#Didn't end up needing to set the covariance - some online tutorials used it and some didn't

#generates a range of x values - not sure how to choose these best
#x = np.arange(0., 8, .1)
x = np.arange(-8, 10, .1)
    #Chose these based on the histogram values from Q2
    
plt.figure()
plt.plot(x, FPKMdensity(x))
plt.title("SRR072893 FPKM values density plot")
plt.xlabel("mRNA abundance (log(RPKM))")
plt.ylabel("abundance")
plt.savefig("Q3out.png")



