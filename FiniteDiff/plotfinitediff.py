import numpy as np
import csv
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
from collections import OrderedDict

datafiles = {
    1: { 'file': 'out0.00078125.csv', 'skip': 6, 'label': '0.00078125'},
    2: { 'file': 'out0.0015625.csv', 'skip': 4, 'label': '0.0015625'},
    3: { 'file': 'out0.003125.csv', 'skip': 2, 'label': '0.003125'},
    4: { 'file': 'out0.00625.csv', 'skip': 1, 'label': '0.00625'},
    5: { 'file': 'out0.0125.csv', 'skip': 1, 'label': '0.0125'},
    # 'p6': { 'file': 'out0.000390625.csv', 'skip': 30, 'label': '0.000390625'}

}




fig = plt.figure()
splot = fig.add_subplot(111)
splot.grid(True)

for key in datafiles:
    df = pd.read_csv(datafiles[key]['file'], sep='\t')
    splot.plot(df.x[::datafiles[key]['skip']], np.log10(np.abs(df.fvalue[::datafiles[key]['skip']])), label=datafiles[key]['label'])

splot.plot([3], [-15], 'bo')
splot.set_xlabel('X')
splot.set_ylabel('log(H)')
handles, labels = splot.get_legend_handles_labels()
splot.legend(handles[::-1], labels[::-1], title='dx', loc=0, ncol=1, prop={'size': 8})


fig.savefig('finitediff.eps')
fig.savefig('finitediff.png')
