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
caseArr=['near','mid','far']
hamiltonian_colnames = ['it','tl','rl','c','ml','ix','iy','iz','time','x','y','z','data']
l2Norm_colnames = ['iteration', 'time', 'data']

axislist = ['d', 'x', 'y', 'z']
BASEPATH = os.path.dirname(os.path.realpath(__file__))

manybhDirArr=['manybhnear_1bh_p0.1_dx0.003125_near_convergence_4x5x9','manybhnear_1bh_p0.1_dx0.003125_near_convergence_12x13x17','manybhnear_1bh_p0.1_dx0.003125_near_convergence_16x17x25','manybhnear_1bh_p0.1_dx0.003125_near_convergence_24x25x33','manybhnear_1bh_p0.1_dx0.003125_near_convergence_32x33x41','manybhnear_1bh_p0.1_dx0.003125_near_convergence_40x41x49']


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

    l2data = pd.DataFrame()
    for gname, gdata in datadf.groupby('zone'):
        fig = plt.figure()
        l2p = fig.add_subplot(111)
        l2p.grid(True)
        for irow in gdata.index:
            if not datadf.loc[irow]['l2'].empty:
                l2dataPoint = {'x_label': datadf.loc[irow]['res'], 'y_value': np.log10(np.abs(datadf.loc[irow]['l2']['data'][0]))}
                l2data = l2data.append(l2dataPoint, ignore_index=True)

        if not l2data.empty:
            l2p.plot(range(len(l2data['x_label'])), l2data['y_value'], 'bo--')
            l2p.set_xticks(range(len(l2data['x_label'])))
            l2p.set_xticklabels(l2data['x_label'], rotation=45, size='small')
            l2p.set_xlabel('Resolutions')
            l2p.set_ylabel('log(L2 Norm)')
            fig.savefig((gname + '/' + method + '_' + gname + '_l2' + plotFormat), bbox_inches= 'tight')
        plt.close('all')


def buildGroupPlots(datadf, method):
    print('Building Group Plots ...')
    ai = {'x': 0, 'y': 1, 'z': 2}
    for gname, gdata in datadf.groupby('zone'):
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

    buildSinglePlosts(simdatadf)
    buildGroupPlots(simdatadf, method)
    buildL2NormPlots(simdatadf, method)
    # build individual plots
    del simdatadf




buildPlots('manybh')
buildPlots('twopun')


# need to fix the y axis limits


exit()



for case in caseArr:
    print('Start building plots for %s zone ' % (case))
    # ManyBH plots ==================================================================================
    figd=plt.figure()
    ad = figd.add_subplot(111)
    ad.grid(True)

    figx=plt.figure()
    ax = figx.add_subplot(111)
    ax.grid(True)

    figy=plt.figure()
    ay = figy.add_subplot(111)
    ay.grid(True)

    figz=plt.figure()
    az = figz.add_subplot(111)
    az.grid(True)

    print('ManyBH:')
    for manybhDir in manybhDirArr:
        print('resolution: %s' % (manybhDir))
       #Create all the file Names
       # print(manybhDir[6:manybhDir.find('_')])
        if(manybhDir[6:manybhDir.find('_')]==case):

            if(case == 'near'):
                d_label_loc = near_d_label_loc_manybh
                x_label_loc = near_x_label_loc_manybh
                y_label_loc = near_y_label_loc_manybh
                z_label_loc = near_z_label_loc_manybh
            elif(case == 'mid'):
                d_label_loc = mid_d_label_loc_manybh
                x_label_loc = mid_x_label_loc_manybh
                y_label_loc = mid_y_label_loc_manybh
                z_label_loc = mid_z_label_loc_manybh
            elif(case == 'far'):
                d_label_loc = far_d_label_loc_manybh
                x_label_loc = far_x_label_loc_manybh
                y_label_loc = far_y_label_loc_manybh
                z_label_loc = far_z_label_loc_manybh

            dataFiled = '../'+manybhDir+'/admconstraints-hamiltonian.d.asc'
            dataFilex = '../'+manybhDir+'/admconstraints-hamiltonian.x.asc'
            dataFiley = '../'+manybhDir+'/admconstraints-hamiltonian.y.asc'
            dataFilez = '../'+manybhDir+'/admconstraints-hamiltonian.z.asc'
            dataFileL2 = '../'+manybhDir+'/admconstraints-hamiltonian.norm2.asc'

            datad = pd.read_table(dataFiled, sep='\t', comment='#', names=hamiltonian_colnames)
            datax = pd.read_table(dataFilex, sep='\t', comment='#', names=hamiltonian_colnames)
            datay = pd.read_table(dataFiley, sep='\t', comment='#', names=hamiltonian_colnames)
            dataz = pd.read_table(dataFilez, sep='\t', comment='#', names=hamiltonian_colnames)
            datal2 = pd.read_table(dataFileL2, sep='\t', comment='#', names=l2Norm_colnames)

            datad = datad[datad.it == 0]
            datax = datax[datax.it == 0]
            datay = datay[datay.it == 0]
            dataz = dataz[dataz.it == 0]

            # make the legends ( labels ) : Lorene resolutions
            plot_label=manybhDir[manybhDir.rfind('_')+1:len(manybhDir)]

            print('============================')
            print(datal2)
            sys.exit()

            #Plot the axis d
            if not datad.empty:
                datad['axis'] =  datad['ml'].str.split(' ').apply(lambda x: x[0])
                ad.plot(list(datad['axis']),list(np.log10(np.abs(datad['ix']))),label=plot_label)
                ad.legend(loc=d_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})
            else:
                print("Data set %s is empty" %(dataFiled))

            # Plot the axis x
            if not datax.empty:
                datax['axis'] = datax['ix'].str.split(' ').apply(lambda x: x[0])
                ax.plot(datax['axis'], np.log10(np.abs(datax['iy'])), label=plot_label)
                ax.legend(loc=x_label_loc, ncol=legend_ncol, prop={'size': legend_fontsize})
            else:
                print("Data set %s is empty" %(dataFilex))

            #Plot the y axis
            if not datay.empty:

                datay['axis'] = datay['ix'].str.split(' ').apply(lambda x: x[1])
                ay.plot(datay['axis'], np.log10(np.abs(datay['iy'])), label=plot_label)
                ay.legend(loc=y_label_loc, ncol=legend_ncol, prop={'size': legend_fontsize})
            else:
                print("Data set %s is empty" %(dataFiley))

            #Plot the z axis
            if not dataz.empty:
                dataz['axis'] = dataz['ix'].str.split(' ').apply(lambda x: x[2])
                az.plot(dataz['axis'], np.log10(np.abs(dataz['iy'])), label=plot_label)
                az.legend(loc=y_label_loc, ncol=legend_ncol, prop={'size': legend_fontsize})
            else:
                print("Data set %s is empty" %(dataFilez))

    # Twopunc plots ==================================================================================

    tfigd=plt.figure()
    tad = tfigd.add_subplot(111)
    tad.grid(True)

    tfigx=plt.figure()
    tax = tfigx.add_subplot(111)
    tax.grid(True)

    tfigy=plt.figure()
    tay = tfigy.add_subplot(111)
    tay.grid(True)

    tfigz=plt.figure()
    taz = tfigz.add_subplot(111)
    taz.grid(True)

    #Loop through twopun simulation files
    for twopunDir in twopunDirArr:
        if(twopunDir[6:twopunDir.find('_')]==case):
            if(case == 'near'):
                d_label_loc = near_d_label_loc_twopun
                x_label_loc = near_x_label_loc_twopun
                y_label_loc = near_y_label_loc_twopun
                z_label_loc = near_z_label_loc_twopun
            elif(case == 'mid'):
                d_label_loc = mid_d_label_loc_twopun
                x_label_loc = mid_x_label_loc_twopun
                y_label_loc = mid_y_label_loc_twopun
                z_label_loc = mid_z_label_loc_twopun
            elif(case == 'far'):
                d_label_loc = far_d_label_loc_twopun
                x_label_loc = far_x_label_loc_twopun
                y_label_loc = far_y_label_loc_twopun
                z_label_loc = far_z_label_loc_twopun


        tdataFiled='../'+twopunDir+'/admconstraints-hamiltonian.d.asc'
        tdataFilex='../'+twopunDir+'/admconstraints-hamiltonian.x.asc'
        tdataFiley='../'+twopunDir+'/admconstraints-hamiltonian.y.asc'
        tdataFilez='../'+twopunDir+'/admconstraints-hamiltonian.z.asc'

        tdatad = pd.read_table(tdataFiled, sep='\t', comment='#', names=hamiltonian_colnames)
        tdatax = pd.read_table(tdataFilex, sep='\t', comment='#', names=hamiltonian_colnames)
        tdatay = pd.read_table(tdataFiley, sep='\t', comment='#', names=hamiltonian_colnames)
        tdataz = pd.read_table(tdataFilez, sep='\t', comment='#', names=hamiltonian_colnames)

        tdatad = tdatad[tdatad.it == 0]
        tdatax = tdatax[tdatax.it == 0]
        tdatay = tdatay[tdatay.it == 0]
        tdataz = tdataz[tdataz.it == 0]

        # make the legends ( labels ) : Lorene resolutions
        plot_label=twopunDir[twopunDir.rfind('_')+1:len(twopunDir)]
        #Plot the axis d
        if not tdatad.empty:
            tdatad['axis'] = tdatad['ml'].str.split(' ').apply(lambda x: x[0])
            tad.plot(tdatad['axis'],np.log10(np.abs(tdatad['ix'])),label=plot_label)
            tad.legend(loc=d_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})

        #Plot the axis x
        if not tdatax.empty:
            tdatax['axis'] = tdatax['ix'].str.split(' ').apply(lambda x: x[0])
            tax.plot(tdatax['axis'],np.log10(np.abs(tdatax['iy'])),label=plot_label)
            tax.legend(loc=d_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})

        # Plot the y axis
        if not tdatay.empty:
            tdatay['axis'] = tdatay['ix'].str.split(' ').apply(lambda x: x[1])
            tay.plot(tdatay['axis'],np.log10(np.abs(tdatay['iy'])),label=plot_label)
            tay.legend(loc=d_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})

        # Plot the z axis
        if not tdataz.empty:
            tdataz['axis'] = tdataz['ix'].str.split(' ').apply(lambda x: x[2])
            tay.plot(tdataz['axis'],np.log10(np.abs(tdataz['iy'])),label=plot_label)
            tay.legend(loc=d_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})

    #Fix the ylimits for d-plots

    ylimarray_m=ad.get_ylim()
    ylimarray_t=tad.get_ylim()

    ymin=ylimarray_t[0]
    ymax=ylimarray_t[1]
    if(ylimarray_m[0]<ylimarray_t[0]):
        ymin=ylimarray_m[0]
    if(ylimarray_m[1]>ylimarray_t[1]):
        ymax=ylimarray_m[1]

    ad.set_ylim(ymin,ymax)
    tad.set_ylim(ymin,ymax)


    #Fix the ylimits for x-plots
    ylimarray_m=ax.get_ylim()
    ylimarray_t=tax.get_ylim()

    ymin=ylimarray_t[0]
    ymax=ylimarray_t[1]
    if(ylimarray_m[0]<ylimarray_t[0]):
        ymin=ylimarray_m[0]
    if(ylimarray_m[1]>ylimarray_t[1]):
        ymax=ylimarray_m[1]

    ax.set_ylim(ymin,ymax)
    tax.set_ylim(ymin,ymax)

    #Fix the ylimits for y-plots
    ylimarray_m=ay.get_ylim()
    ylimarray_t=tay.get_ylim()

    ymin=ylimarray_t[0]
    ymax=ylimarray_t[1]
    if(ylimarray_m[0]<ylimarray_t[0]):
        ymin=ylimarray_m[0]
    if(ylimarray_m[1]>ylimarray_t[1]):
        ymax=ylimarray_m[1]

    ay.set_ylim(ymin,ymax)
    tay.set_ylim(ymin,ymax)

    #Fix the ylimits for z-plots
    ylimarray_m=az.get_ylim()
    ylimarray_t=taz.get_ylim()

    ymin=ylimarray_t[0]
    ymax=ylimarray_t[1]
    if(ylimarray_m[0]<ylimarray_t[0]):
        ymin=ylimarray_m[0]
    if(ylimarray_m[1]>ylimarray_t[1]):
        ymax=ylimarray_m[1]

    az.set_ylim(ymin,ymax)
    taz.set_ylim(ymin,ymax)

    ad.set_xlabel('d')
    ad.set_ylabel('log(H)')

    ax.set_xlabel('x')
    ax.set_ylabel('log(H)')

    ay.set_xlabel('y')
    ay.set_ylabel('log(H)')

    az.set_xlabel('z')
    az.set_ylabel('log(H)')

    tad.set_xlabel('d')
    tad.set_ylabel('log(H)')

    tax.set_xlabel('x')
    tax.set_ylabel('log(H)')

    tay.set_xlabel('y')
    tay.set_ylabel('log(H)')

    taz.set_xlabel('z')
    taz.set_ylabel('log(H)')

    figd.savefig((case + '_d_manybh_' + simname + plotFormat), bbox_inches= 'tight')
    figx.savefig((case + '_x_manybh_' + simname + plotFormat), bbox_inches= 'tight')
    figy.savefig((case + '_y_manybh_' + simname + plotFormat), bbox_inches= 'tight')
    figz.savefig((case + '_z_manybh_' + simname + plotFormat), bbox_inches= 'tight')

    tfigd.savefig((case + '_d_twopun_' + simname + plotFormat), bbox_inches= 'tight')
    tfigx.savefig((case + '_x_twopun_' + simname + plotFormat), bbox_inches= 'tight')
    tfigy.savefig((case + '_y_twopun_' + simname + plotFormat), bbox_inches= 'tight')
    tfigz.savefig((case + '_z_twopun_' + simname + plotFormat), bbox_inches= 'tight')

    plt.close('all')
