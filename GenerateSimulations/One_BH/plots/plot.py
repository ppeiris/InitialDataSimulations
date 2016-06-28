import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.precision', 30)
axisArr=['d','x','y','z']
caseArr=['near','mid','far']
hamiltonian_colnames = ['it','tl','rl','c','ml','ix','iy','iz','time','x','y','z','data']

# Following 3 lines will be replaced by another python script according to the simulation parameters, Please do not change them manually

manybhDirArr=['manybhnear_One_BH_12x13x17','manybhnear_One_BH_16x17x25','manybhnear_One_BH_24x25x33','manybhnear_One_BH_32x33x41','manybhmid_One_BH_12x13x17','manybhmid_One_BH_16x17x25','manybhmid_One_BH_24x25x33','manybhmid_One_BH_32x33x41','manybhfar_One_BH_12x13x17','manybhfar_One_BH_16x17x25','manybhfar_One_BH_24x25x33','manybhfar_One_BH_32x33x41']


twopunDirArr=['twopunnear_One_BH_20','twopunnear_One_BH_30','twopunnear_One_BH_40','twopunmid_One_BH_20','twopunmid_One_BH_30','twopunmid_One_BH_40','twopunfar_One_BH_20','twopunfar_One_BH_30','twopunfar_One_BH_40']


simname='One_BH'



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

for case in caseArr:
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

    for manybhDir in manybhDirArr:
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

            datad = pd.read_table(dataFiled, sep='\t', comment='#', names=hamiltonian_colnames)
            datax = pd.read_table(dataFilex, sep='\t', comment='#', names=hamiltonian_colnames)
            datay = pd.read_table(dataFiley, sep='\t', comment='#', names=hamiltonian_colnames)
            dataz = pd.read_table(dataFilez, sep='\t', comment='#', names=hamiltonian_colnames)

            # make the legends ( labels ) : Lorene resolutions
            plot_label=manybhDir[manybhDir.rfind('_')+1:len(manybhDir)]
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

    figd.savefig((case+'_d_manybh_'+simname+'.eps'),bbox_inches='tight')
    figx.savefig((case+'_x_manybh_'+simname+'.eps'),bbox_inches='tight')
    figy.savefig((case+'_y_manybh_'+simname+'.eps'),bbox_inches='tight')
    figz.savefig((case+'_z_manybh_'+simname+'.eps'),bbox_inches='tight')

    tfigd.savefig((case+'_d_twopun_'+simname+'.eps'),bbox_inches='tight')
    tfigx.savefig((case+'_x_twopun_'+simname+'.eps'),bbox_inches='tight')
    tfigy.savefig((case+'_y_twopun_'+simname+'.eps'),bbox_inches='tight')
    tfigz.savefig((case+'_z_twopun_'+simname+'.eps'),bbox_inches='tight')
    plt.close('all')
