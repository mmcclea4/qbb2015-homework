#!/usr/bin/env python

"""
Using Blast alignments - print the sequence name, ratio of identities, and ratio of gaps
"""

import sys
import matplotlib.pyplot as plt

# argv = subset_refMrna_aligned.txt

scoreS = []
expectS = []

for line in open(sys.argv[1]):
    if line.startswith( " Score =" ):
        score = float(line.split()[2])
        scoreS.append(score)
        expect = float(line.split()[7])
        expectS.append(expect)

#print expectS, scoreS

plt.figure()
plt.hist(scoreS, bins=[0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600])
#plt.hist(scoreS)
plt.title("Alignment scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("Q2scorehist.png")

plt.figure()
#plt.hist(scoreS, bins=[0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600])
plt.hist(expectS)
plt.title("Alignment E-values")
plt.xlabel("E-value")
plt.ylabel("Frequency")
plt.savefig("Q2evaluehist.png")

plt.figure()
plt.scatter(scoreS, expectS)
plt.title("Alignment E-values and Scores")
plt.xlabel("Scores")
plt.ylabel("E-value")
plt.savefig("Q2scatter.png")

