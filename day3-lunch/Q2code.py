#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

FPKMvalue = []
for num in df["FPKM"]:
    if num != 0:
        FPKMvalue.append(num)
#print FPKMvalue

logFPKMvalue = np.log(FPKMvalue)

plt.figure()
plt.hist(logFPKMvalue)
plt.title("SRR072893 FPKM values")
plt.xlabel("mRNA abundance (log(RPKM))")
plt.ylabel("abundance")
plt.savefig("Q2histogram.png")

