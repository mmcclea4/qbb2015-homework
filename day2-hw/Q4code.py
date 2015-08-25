#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df = pd.read_table(annotation)

df2 = df[df.FPKM !=0]
    #Removes rows where the value in column FPKM = 0

df3 = df2.sort("FPKM", ascending = True)
    #Sorts the data file to ascending valued of FPKM, in order to divide into thirds

df3bot = df3[0:3183] 
df3mid = df3[3183:6366]
df3top = df3[6366:9649]

plt.figure()
plt.boxplot([df3bot["FPKM"],df3mid["FPKM"],df3top["FPKM"]])
plt.savefig("Q4.png")
        
        
        
        