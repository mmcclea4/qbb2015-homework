#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")

repdata = pd.read_csv("~/qbb2015/rawdata/replicates.csv")

Sxlf = []
for sample in metadata[metadata["sex"] == "female"]["sample"]:
    dff = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roif = dff["t_name"].str.contains("FBtr0331261")
    Sxlf.append(dff[roif]["FPKM"].values)

Sxlm =[]    
for sample in metadata[metadata["sex"] == "male"]["sample"]:
    dfm = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roim = dfm["t_name"].str.contains("FBtr0331261")
    Sxlm.append(dfm[roim]["FPKM"].values)
    
Repf = []
for sample in repdata[repdata["sex"] == "female"]["sample"]:
    dfrf = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roirf = dfrf["t_name"].str.contains("FBtr0331261")
    Repf.append(dfrf[roirf]["FPKM"].values)
    
Repm = []
for sample in repdata[repdata["sex"] == "male"]["sample"]:
    dfrm = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roirm = dfrm["t_name"].str.contains("FBtr0331261")
    Repm.append(dfrm[roirm]["FPKM"].values)
    
plt.figure()
plt.plot(Sxlf, "r")
plt.plot(Sxlm, "b")
plt.plot((4, 5, 6, 7), Repf, "ro")
plt.plot((4, 5, 6, 7), Repm, "bo")
plt.title("Sxl")
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.xticks( range(8), ('10', '11', '12', '13', '14A', '14B', '14C', '14D'))
plt.legend(["Female", "Male", "Stage 14 Female", "Stage 14 Male"], ("upper left"))
    # not to be confused with .figlegend
plt.savefig("Q1timecourse.png")
    