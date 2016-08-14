import numpy as np
import scipy as sp
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import os, sys
from matplotlib.ticker import AutoMinorLocator

pd.set_option('display.precision', 30)
axisArr=['d','x','y','z']
# caseArr=['near','mid','far']
caseArr=['near','mid', 'far']
hamiltonian_colnames = ['it','tl','rl','c','ml','ix','iy','iz','time','x','y','z','data']
l2Norm_colnames = ['iteration', 'time', 'data']

axislist = ['d', 'x', 'y', 'z']
BASEPATH = os.path.dirname(os.path.realpath(__file__))

manybhDirArr=['manybhnear_1bh_p0.75_dx0.003125_near_convergencee_4x5x9','manybhnear_1bh_p0.75_dx0.003125_near_convergencee_8x9x13','manybhnear_1bh_p0.75_dx0.003125_near_convergencee_12x13x17','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_4x5x9','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_8x9x13','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_12x13x17','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_4x5x9','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_8x9x13','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_12x13x17']


# manybhDirArr=['manybhnear_1bh_p0.75_dx0.003125_near_convergencee_4x5x9','manybhnear_1bh_p0.75_dx0.003125_near_convergencee_8x9x13','manybhnear_1bh_p0.75_dx0.003125_near_convergencee_12x13x17','manybhnear_1bh_p0.75_dx0.003125_near_convergencee_16x17x25','manybhnear_1bh_p0.75_dx0.003125_near_convergencee_24x25x33','manybhnear_1bh_p0.75_dx0.003125_near_convergencee_32x33x41','manybhnear_1bh_p0.75_dx0.003125_near_convergencee_40x41x49','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_4x5x9','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_8x9x13','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_12x13x17','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_16x17x25','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_24x25x33','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_32x33x41','manybhmid_1bh_p0.75_dx0.003125_near_convergencee_40x41x49','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_4x5x9','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_8x9x13','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_12x13x17','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_16x17x25','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_24x25x33','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_32x33x41','manybhfar_1bh_p0.75_dx0.003125_near_convergencee_40x41x49']



twopunDirArr=[]


simname='1bh_p0.75_dx0.003125_near_convergencee'



twopunDirArr=[]


simname='1bh_p0.1_dx0.003125_near_convergence'



twopunDirArr=[]

simdir = {'manybh': manybhDirArr, 'twopun': twopunDirArr}

plotFormat = '.png'
# plotFormat = '.eps'


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

far_d_label_loc_manybh = loc['best']
far_x_label_loc_manybh = loc['best']
far_y_label_loc_manybh = loc['best']
far_z_label_loc_manybh = loc['best']

mid_d_label_loc_manybh = loc['best']
mid_x_label_loc_manybh = loc['best']
mid_y_label_loc_manybh = loc['best']
mid_z_label_loc_manybh = loc['best']

near_d_label_loc_manybh = loc['best']
near_x_label_loc_manybh = loc['best']
near_y_label_loc_manybh = loc['best']
near_z_label_loc_manybh = loc['best']

far_d_label_loc_twopun = loc['best']
far_x_label_loc_twopun = loc['best']
far_y_label_loc_twopun = loc['best']
far_z_label_loc_twopun = loc['best']

mid_d_label_loc_twopun = loc['best']
mid_x_label_loc_twopun = loc['best']
mid_y_label_loc_twopun = loc['best']
mid_z_label_loc_twopun = loc['best']

near_d_label_loc_twopun = loc['best']
near_x_label_loc_twopun = loc['best']
near_y_label_loc_twopun = loc['best']
near_z_label_loc_twopun = loc['best']

def buildL2NormPlots(datadf, method):
    print('Build L2 Norm')
    ai = {'x': 0, 'y': 1, 'z': 2}
    for gname, gdata in datadf.groupby('zone'):
        l2data = pd.DataFrame()
        if gname not in caseArr:
            continue
        fig = plt.figure()
        l2p = fig.add_subplot(111)
        l2p.grid(True)
        for irow in gdata.index:
            if not gdata.loc[irow]['l2'].empty:
                if gname == gdata.loc[irow]['zone']:
                    l2dataPoint = {'x_label': gdata.loc[irow]['res'], 'y_value': np.log10(np.abs(gdata.loc[irow]['l2']['data'][0]))}
                    l2data = l2data.append(l2dataPoint, ignore_index=True)

        if not l2data.empty:
            l2p.plot(range(len(l2data['x_label'])), l2data['y_value'], 'bo--')
            l2p.set_xticks(range(len(l2data['x_label'])))
            l2p.set_xticklabels(l2data['x_label'], rotation=45, size='small')
            l2p.set_xlabel('Resolutions')
            l2p.set_ylabel('log(L2 Norm)')
            fig.savefig((gname + '/' + method + '_' + gname + '_l2' + plotFormat), bbox_inches= 'tight')
        plt.close('all')


def buildGroupPlotsGroup(datadf, method):
    print('Building Group Plots In One')
    ai = {'x': 0, 'y': 1, 'z': 2}

    print('Building Group Subplots')
    for axis in axislist:
        splotcount = 321
        zone_name = 1
        fig1 = plt.figure(1)
        for zname, zdata in datadf.groupby('zone'):
            subplot = fig1.add_subplot(splotcount)
            subplot.grid(True)

            subplot.xaxis.set_minor_locator(AutoMinorLocator(4))
            subplot.yaxis.set_minor_locator(AutoMinorLocator(4))

            plt.tick_params(which='both', width=1)
            plt.tick_params(which='minor', length=2)
            plt.tick_params(axis ='both', which='major', length=4, labelsize =8)

            l2data = pd.DataFrame()
            for irow in zdata.index:
                if axis in ['d']:
                    axisVal = datadf.loc[irow][axis]['ml'].str.split(' ').apply(lambda x: x[0])
                    dataVal = np.log10(np.abs(datadf.loc[irow][axis]['ix']))
                else:
                    axisVal = datadf.loc[irow][axis]['ix'].str.split(' ').apply(lambda x: x[ai[axis]])
                    dataVal = np.log10(np.abs(datadf.loc[irow][axis]['iy']))
                subplot.plot(axisVal, dataVal, label=datadf.loc[irow]['res'])
                subplot.set_title('Zone - ' + str(zone_name) + '(a)', fontsize =10)
                subplot.set_xlabel('$'+axis+'$', fontsize =10)
                subplot.set_ylabel('$log(H)$', fontsize =10)
                # subplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 5})
                subplot.legend(bbox_to_anchor=(1.01, 1.0), loc=2, borderaxespad=0., prop={'size': 5})
                # subplot.legend(loc=loc['best'], ncol=legend_ncol, prop={'size': 5})
                if not datadf.loc[irow]['l2'].empty:
                    l2dataPoint = {'x_label': zdata.loc[irow]['res'], 'y_value': np.log10(np.abs(zdata.loc[irow]['l2']['data'][0]))}
                    l2data = l2data.append(l2dataPoint, ignore_index=True)
            splotcount +=1
            subplot = fig1.add_subplot(splotcount)
            subplot.grid(True)

            subplot.xaxis.set_minor_locator(AutoMinorLocator(4))
            subplot.yaxis.set_minor_locator(AutoMinorLocator(4))

            plt.tick_params(which='both', width=1)
            plt.tick_params(which='minor', length=0)
            plt.tick_params(axis ='both', which='major', length=4, labelsize =8)

            subplot.plot(range(len(l2data['x_label'])), l2data['y_value'], 'ko--')
            subplot.set_xticks(range(len(l2data['x_label'])))
            subplot.set_xticklabels(l2data['x_label'], size='xx-small')
            subplot.set_title('Zone - ' + str(zone_name) + '(b)', fontsize =10)
            subplot.set_xlabel('$Collocations$', fontsize =10)
            subplot.set_ylabel('$log(l_{2})$', fontsize =10)
            zone_name += 1
            # plt.set_xticks(range(len(l2data['x_label'])))
            # pltt.set_xticklabels(l2data['x_label'], rotation=45, size='small')
            splotcount +=1
            fig1.tight_layout()
            fig1.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

        # plt.savefig('gplots_' + axis +'_.png')
            plt.savefig('group/' + 'group_' + axis + plotFormat)
        plt.close('all')


def buildGroupPlots(datadf, method):
    print('Building Group Plots ...')
    ai = {'x': 0, 'y': 1, 'z': 2}
    for gname, gdata in datadf.groupby('zone'):
        if gname not in caseArr:
            continue
        for axis in axislist:
            fig = plt.figure()
            figl2 = plt.figure()
            l2p = figl2.add_subplot(111)
            l2p.grid(True)

            ad = fig.add_subplot(111)
            ad.grid(True)

            ad.xaxis.set_minor_locator(AutoMinorLocator(4))
            ad.yaxis.set_minor_locator(AutoMinorLocator(4))

            plt.tick_params(which='both', width=1)
            plt.tick_params(which='minor', length=2)
            plt.tick_params(axis ='both', which='major', length=4, labelsize =12)

            for irow in gdata.index:
                try:
                    if axis in ['d']:
                        axisVal = datadf.loc[irow][axis]['ml'].str.split(' ').apply(lambda x: x[0])
                        dataVal = np.log10(np.abs(datadf.loc[irow][axis]['ix']))
                    else:
                        axisVal = datadf.loc[irow][axis]['ix'].str.split(' ').apply(lambda x: x[ai[axis]])
                        dataVal = np.log10(np.abs(datadf.loc[irow][axis]['iy']))
                    ad.plot(axisVal, dataVal, label=datadf.loc[irow]['res'])
                    # add L2
                    if not datadf.loc[irow]['l2'].empty:
                        l2p.plot(axisVal, [np.log10(np.abs(datadf.loc[irow]['l2']['data'][0]))] * len(axisVal), label=datadf.loc[irow]['res'])
                        # ad.plot(axisVal, [np.log10(np.abs(datadf.loc[irow]['l2']['data'][0]))] * len(axisVal), label=datadf.loc[irow]['res'])

                except Exception, e:
                    print(str(e))
                    continue
            ad.legend(loc=loc['best'], ncol=legend_ncol, prop={'size': legend_fontsize})
            ad.set_xlabel(axis)
            ad.set_ylabel('log(H)')
            fig.savefig((gname + '/' + method + '_' + gname + '_' + axis + '_all_resolution' + plotFormat), bbox_inches= 'tight')

            l2p.legend(loc=loc['best'], ncol=legend_ncol, prop={'size': legend_fontsize})
            l2p.set_xlabel(axis)
            l2p.set_ylabel('log(L2 Norm)')
            ymin, ymax = l2p.get_ylim()
            l2p.set_ylim([ymin - (ymax - ymin)/2, ymax + (ymax - ymin)/2])

            figl2.savefig((gname + '/' + method + '_' + gname + '_' + axis + '_all_resolution_L2' + plotFormat), bbox_inches= 'tight')
            plt.close('all')

        # print(gdata)

def buildSinglePlosts(datadf):
    # build individual plots
    print('Building Individual Plots...')
    ai = {'x': 0, 'y': 1, 'z': 2}
    for irow in datadf.index:
        if datadf.loc[irow]['zone'] not in caseArr:
            continue

        for axis in axislist:
            if not datadf.loc[irow][axis].empty:
                try:
                    fig = plt.figure()
                    ad = fig.add_subplot(111)
                    ad.grid(True)

                    if axis in ['d']:
                        axisVal = datadf.loc[irow][axis]['ml'].str.split(' ').apply(lambda x: x[0])
                        dataVal = np.log10(np.abs(datadf.loc[irow][axis]['ix']))
                    else:
                        axisVal = datadf.loc[irow][axis]['ix'].str.split(' ').apply(lambda x: x[ai[axis]])
                        dataVal = np.log10(np.abs(datadf.loc[irow][axis]['iy']))

                    # print(len(axisVal))
                    ad.plot(axisVal, dataVal, label=datadf.loc[irow]['res'])

                    # Plot l2 norm
                    if not datadf.loc[irow]['l2'].empty:
                        ad.plot(axisVal, [np.log10(np.abs(datadf.loc[irow]['l2']['data'][0]))] * len(axisVal), label='test')


                    ad.legend(loc=loc['best'], ncol=legend_ncol, prop={'size': legend_fontsize})

                    ad.set_xlabel(axis)
                    ad.set_ylabel('log(H)')
                    fig.savefig((datadf.loc[irow]['zone'] + '/' + datadf.loc[irow]['dir'] + '_' + axis + plotFormat), bbox_inches= 'tight')
                    plt.close('all')
                    print('Plot %s' % (datadf.loc[irow]['dir'] + '_' + axis + plotFormat))
                except Exception, e:
                    print(str(e))
                    continue
            else:
                print("Data set is empty")


def buildPlots(method):
    if not method in ['manybh', 'twopun']:
        print('Error...')
        return False

    simdatadf = pd.DataFrame(simdir[method], columns=['dir'])
    simdatadf['zone'] = simdatadf.dir.str.split('_').apply(lambda x: x[0][6:len(x[0])])
    simdatadf['res'] = simdatadf.dir.str.split('_').apply(lambda x: x[-1])
    simdatadf['d'] = None
    simdatadf['x'] = None
    simdatadf['y'] = None
    simdatadf['z'] = None
    simdatadf['l2'] = 'l2'

    print('Loading data for %s ...' % (method))
    # Read all the data and store in simdatadf datat frame
    for irow in simdatadf.index:
        datapathl2 = '../' + simdatadf.loc[irow]['dir'] + '/admconstraints-hamiltonian.norm2.asc'
        if os.path.exists(datapathl2):
            dftmp = pd.read_table(datapathl2, sep=' ', comment='#', names=l2Norm_colnames)
        else:
            dftmp = None

        simdatadf.loc[irow]['l2'] = dftmp

        for axis in axislist:
            datapath = '../' + simdatadf.loc[irow]['dir'] + '/admconstraints-hamiltonian.' + axis + '.asc'
            # print(datapath)
            df = pd.read_table(datapath, sep='\t', comment='#', names=hamiltonian_colnames)
            df = df[2:-2]
            df = df.reset_index()
            # print('Data loaded for %s %s: %s ' % (simdatadf.loc[irow]['dir'], axis, datapath))
            simdatadf.loc[irow][axis] = df[df.it == 0]

    for zone in caseArr:
        if not os.path.isdir(os.path.join(BASEPATH, zone)):
            os.makedirs(os.path.join(BASEPATH, zone))

    if not os.path.isdir(os.path.join(BASEPATH, 'group')):
        os.makedirs(os.path.join(BASEPATH, 'group'))

    buildSinglePlosts(simdatadf)
    buildGroupPlots(simdatadf, method)
    buildL2NormPlots(simdatadf, method)
    buildGroupPlotsGroup(simdatadf, method)
    # build individual plots
    del simdatadf




buildPlots('manybh')
buildPlots('twopun')

