import numpy as np
import csv
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import AutoMinorLocator
pd.options.display.float_format = '{:.10g}'.format


datafiles = {
    1: { 'file': 'out0.000390625.csv', 'skip': 1, 'label': '0.000390625'},
    2: { 'file': 'out0.00078125.csv', 'skip': 1, 'label': '0.00078125'}, # 6
    3: { 'file': 'out0.0015625.csv', 'skip': 1, 'label': '0.0015625'}, # 4
    4: { 'file': 'out0.003125.csv', 'skip': 1, 'label': '0.003125'}, # 2
    5: { 'file': 'out0.00625.csv', 'skip': 1, 'label': '0.00625'},
    6: { 'file': 'out0.0125.csv', 'skip': 1, 'label': '0.0125'},
    7: { 'file': 'out0.025.csv', 'skip': 1, 'label': '0.025'},
    8: { 'file': 'out0.05.csv', 'skip': 1, 'label': '0.05'},
    # 9: { 'file': 'out0.1.csv', 'skip': 1, 'label': '0.1'},
    # 10: { 'file': 'out0.2.csv', 'skip': 1, 'label': '0.2'},
    # 11: { 'file': 'out0.4.csv', 'skip': 1, 'label': '0.4'}
}

fig = plt.figure()
splot = fig.add_subplot(111)
splot.grid(True)

splot.xaxis.set_minor_locator(AutoMinorLocator(4))
splot.yaxis.set_minor_locator(AutoMinorLocator(4))

plt.tick_params(which='both', width=1)
plt.tick_params(which='minor', length=2)
plt.tick_params(axis ='both', which='major', length=4, labelsize =12)


for key in datafiles:
    df = pd.read_csv(datafiles[key]['file'], sep='\t')
    splot.plot(df.x[::datafiles[key]['skip']], np.log10(np.abs(df.fvalue[::datafiles[key]['skip']])), label=datafiles[key]['label'])

# splot.plot([3], [-15], 'bo')
splot.set_xlabel('X')
splot.set_ylabel('log(H)')
handles, labels = splot.get_legend_handles_labels()
splot.legend(handles[::-1], labels[::-1], title='$\Delta x$', loc=0, ncol=1, prop={'size': 8})


fig.savefig('finitediff_0.5_away_fromBH.eps', bbox_inches= 'tight')
fig.savefig('finitediff.png', bbox_inches= 'tight')

# plt.close('all')



#############
dfl2 = pd.DataFrame()
for key in datafiles:
    df = pd.read_csv(datafiles[key]['file'], sep='\t', dtype=float)
    # df['x'] = df['x'].astype(float)
    # df = df[(df.x < 2.5) | (df.x > 3.5)]
    l2d = {'dx': datafiles[key]['label'], 'l2': np.linalg.norm(df['fvalue'])}
    dfl2 = dfl2.append(l2d, ignore_index=True)


figl2 = plt.figure()
l2sub = figl2.add_subplot(111)
l2sub.grid(True)

l2sub.xaxis.set_minor_locator(AutoMinorLocator(4))
l2sub.yaxis.set_minor_locator(AutoMinorLocator(4))

plt.tick_params(which='both', width=1)
plt.tick_params(which='minor', length=2)
plt.tick_params(axis ='both', which='major', length=4, labelsize =12)


dfl2 = dfl2.sort_values(by=['dx'], ascending=False)


l2sub.plot(range(len(dfl2['dx'])), np.log10(np.abs(dfl2['l2'])), 'bo--')
# l2sub.plot(range(len(dfl2['dx'])), dfl2['l2'], 'bo--')
l2sub.set_xticks(range(len(dfl2['dx'])))
l2sub.set_xticklabels(dfl2['dx'], rotation=60)


l2sub.set_xlabel('Grid Spacing ($\Delta x$)')
l2sub.set_ylabel('log($\mathscr{L}^{2}$ - Norm of H)')

# plt.tight_layout()
figl2.savefig('l2norms.png', bbox_inches= 'tight')
figl2.savefig('l2norms_0.5_away_fromBH.eps', bbox_inches= 'tight')

plt.close('all')



