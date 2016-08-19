import numpy as np
import scipy as sp
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import os, sys
from matplotlib.ticker import AutoMinorLocator
from scipy import interpolate
import matplotlib.gridspec as gridspec
import itertools

pd.set_option('display.precision', 30)
axisArr=['d','x','y','z']
# caseArr=['near','mid','far']
caseArr=['near','mid', 'far']
hamiltonian_colnames = ['it','tl','rl','c','ml','ix','iy','iz','time','x','y','z','data']
l2Norm_colnames = ['iteration', 'time', 'data']

axislist = ['d', 'x', 'y', 'z']
BASEPATH = os.path.dirname(os.path.realpath(__file__))

dataFiles = {
    1 : {'file': '../1BH_P0.1_convergence/1bh_p0.1_dx0.003125_convergence/plots/l2data/%s_%s_%s.csv', 'legend': '$P_{x} = 0.1$'},
    2 : {'file': '../1BH_P0.3_convergence/1bh_p0.3_dx0.003125_convergence/plots/l2data/%s_%s_%s.csv', 'legend': '$P_{x} = 0.3$'},
    3 : {'file': '../1BH_P0.5_convergence/1bh_p0.5_dx0.003125_convergence/plots/l2data/%s_%s_%s.csv', 'legend': '$P_{x} = 0.5$'},
    4 : {'file': '../1BH_P0.75_convergence/1bh_p0.75_dx0.003125_near_convergence/plots/l2data/%s_%s_%s.csv', 'legend': '$P_{x} = 0.75$'},
}

plotFormat = '.png'
plotFormat = '.eps'

# Legend locations
legend_ncol = 3
legend_fontsize = 9
loc = {
    'best': 0,
    'upper_right': 1,
    'upper_left': 2,
    'lower_left': 3,
    'lower_right': 4,
    'right': 5,
    'center_left': 6,
    'center_right': 7,
    'lower_center': 8,
    'upper_center': 9,
    'center': 10
}

def getConvergentFactor(df):
    confac = (df.iloc[3]['y_original'] - df.iloc[1]['y_original'])/(df.iloc[1]['y_original'] - df.iloc[0]['y_original'])
    print(confac)

def plotl2s():

    axis = 'x'
    method = 'manybh'
    zone = 'far'

    gfig = plt.figure(figsize=(10, 10))

    setylabel = True

    subplotval = 321
    zi = 0
    for zone in caseArr:
        marker = itertools.cycle(('o', 'D', 's', '^', 'D', '*'))
        zi +=1
        gfsub = gfig.add_subplot(subplotval)
        gfsub.grid(True)
        # gfsub.xaxis.set_minor_locator(AutoMinorLocator(4))
        gfsub.yaxis.set_minor_locator(AutoMinorLocator(4))

        # load all the data
        data = pd.DataFrame()
        maxlen = 0
        iindex = -1
        for key in dataFiles:
            dfilename = dataFiles[key]['file'] % (method, zone, axis)
            print(dfilename)
            tmpdf = pd.read_csv(dfilename, sep='\t')
            tmpdf = tmpdf[0:5]
            tmpval = {'data': tmpdf, 'legend': dataFiles[key]['legend']}
            iindex += 1
            if maxlen < len(tmpval['data']):
                maxindex = iindex
                maxlen = len(tmpval['data'])
            data = data.append(tmpval, ignore_index=True)

        # Plot
        fig = plt.figure()
        l2p = fig.add_subplot(111)
        l2p.grid(True)
        l2p.yaxis.set_minor_locator(AutoMinorLocator(4))
        for index in data.index:
            # getConvergentFactor(data.iloc[index]['data'])
            # print(data.iloc[index]['data'])
            tmpy = list(data.iloc[index]['data']['y_value'])
            if tmpy != maxlen:
                tmpy += [None]*(maxlen - len(tmpy))

            x = np.arange(0, maxlen)
            y = tmpy

            f = interpolate.interp1d(x, y, kind='cubic')
            xnew = np.arange(0, maxlen - 1, 0.1)
            ynew = f(xnew)

            l2p.plot(xnew, ynew, '-', label=data.iloc[index]['legend'])
            l2p.plot(x, y, 'k.')

            # gfsub.plot(xnew, ynew, '-', label=data.iloc[index]['legend'])
            gfsub.plot(x, y, '-', marker=marker.next(), label=data.iloc[index]['legend'])



        # l2p.plot(range(maxlen), tmpy, 'o-', label=data.iloc[index]['legend'])
        l2p.set_xticks(range(maxlen))
        l2p.set_xticklabels(data.iloc[maxindex]['data']['x_label'], rotation=45, size='small')
        l2p.set_xlabel('Boosted BH - %s Zone - ManyBH' %(zone))
        l2p.set_ylabel('log(L2 Norm)')
        l2p.legend(loc=0, ncol=1, prop={'size': 10})

        fig.tight_layout()
        plt.tick_params(which='both', width=1)
        plt.tick_params(which='minor', length=2)
        plt.tick_params(axis ='both', which='major', length=4, labelsize =8)
        fig.savefig('l2s_' + method + '_' + zone + '_' + axis + plotFormat, bbox_inches= 'tight')

        gfsub.set_xticks(range(maxlen))
        gfsub.set_xticklabels(data.iloc[maxindex]['data']['x_label'], rotation=70, size='small')
        gfsub.set_title('Zone - %s (%s)' %(str(zi), zone), fontsize=12)
        if setylabel:

            setylabel = False
            gfsub.legend(bbox_to_anchor=(1.95, -0.75), loc=0, ncol=1, borderaxespad=0., prop={'size': 12})
            # gfsub.legend(loc=0, ncol=1, prop={'size': 8})
        gfsub.set_ylabel('log($l_{2}$ Norm)', fontsize=12)
        subplotval += 1

    gfig.tight_layout()
    # gs1.tight_layout(gfig, rect=[0, 0, 3, 3])
    gfig.savefig('group_l2s_' + method  + '_' + axis + plotFormat, bbox_inches= 'tight')

    plt.close('all')


plotl2s()
print('Done.')
