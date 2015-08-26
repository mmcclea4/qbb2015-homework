#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfm = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

dff = pd.read_table("~/qbb2015/stringtie/SRR072905/t_data.ctab")

m10FPKMvalue = [] # =R
for num in dfm["FPKM"]:
    m10FPKMvalue.append(num)

f10FPKMvalue = [] # =G
for num in dff["FPKM"]:
    f10FPKMvalue.append(num)
    
# According to wiki M = log2(R/G) = log2(R) - log2(G)
M = np.log2(m10FPKMvalue) - np.log2(f10FPKMvalue)

#According to wiki A = 1/2 log2(RG) = 1/2(log2(R) + log2(G))
A = 0.5 * (np.log2(m10FPKMvalue) + np.log2(f10FPKMvalue))
        
plt.figure()
plt.plot(A, M, "co")
plt.axhline(y=0, color='gray', linestyle='--')
plt.title("Male vs Female Stage 10 FPKM values - MA plot")
plt.xlabel("M")
plt.ylabel("A")
plt.savefig("Q4out.png")