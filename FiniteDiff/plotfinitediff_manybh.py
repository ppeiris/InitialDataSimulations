import numpy as np
import csv
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import AutoMinorLocator

datafiles = {
    1: { 'file': 'out0.000390625.csv', 'skip': 1, 'label': '0.000390625'},
    2: { 'file': 'out0.00078125.csv', 'skip': 1, 'label': '0.00078125'}, # 6
    3: { 'file': 'out0.0015625.csv', 'skip': 1, 'label': 'Finite Difference, dx = 0.0015625'}, # 4
    4: { 'file': 'out0.003125.csv', 'skip': 1, 'label': '0.003125'}, # 2
    5: { 'file': 'out0.00625.csv', 'skip': 1, 'label': '0.00625'},
    6: { 'file': 'out0.0125.csv', 'skip': 1, 'label': '0.0125'}
}

manybhdata = {
	1: { 'file': 'manybh_ex0.0015625_40x41x49.x.asc', 'skip': 1, 'label': 'ManyBH'}
}

hamiltonian_colnames = ['it','tl','rl','c','ml','ix','iy','iz','time','x','y','z','data']

fig = plt.figure()
splot = fig.add_subplot(111)
splot.grid(True)

splot.xaxis.set_minor_locator(AutoMinorLocator(4))
splot.yaxis.set_minor_locator(AutoMinorLocator(4))

plt.tick_params(which='both', width=1)
plt.tick_params(which='minor', length=2)
plt.tick_params(axis ='both', which='major', length=4, labelsize =12)

key = 3
df = pd.read_csv(datafiles[key]['file'], sep='\t')
splot.plot(df.x[::datafiles[key]['skip']], np.log10(np.abs(df.fvalue[::datafiles[key]['skip']])), label=datafiles[key]['label'])

del df

df = pd.read_table(manybhdata[1]['file'], sep='\t', comment='#', names=hamiltonian_colnames)
df = df[2:-2]
df = df.reset_index()
df = df[df.it == 0]

axisVal = df['ix'].str.split(' ').apply(lambda x: x[0])
dataVal = np.log10(np.abs(df['iy']))
splot.plot(axisVal, dataVal, label='Spectral (ManyBH), $N_{r} = 40$, $N_{\\theta} = 41$, $N_{\\varphi} = 49$')


splot.set_xlabel('X')
splot.set_ylabel('log(H)')
handles, labels = splot.get_legend_handles_labels()
splot.legend(handles[::-1], labels[::-1], loc=0, ncol=1, prop={'size': 8})


fig.savefig('finitediff_manybh.eps')
fig.savefig('finitediff_manybh.png')
