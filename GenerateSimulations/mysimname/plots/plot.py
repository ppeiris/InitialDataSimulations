#!/usr/bin/env python 

import numpy as np
import scipy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

axisArr=['d','x','y','z']
caseArr=['near','mid','far']
index=0
#========================================================================================================================================
#Following 3 lines will be replaced by another python script according to the simulation parameters, Please do not change them manually
manybhDirArr=['/manybhnear_mysimname_12x13x17','/manybhnear_mysimname_16x17x25','/manybhnear_mysimname_24x25x33','/manybhnear_mysimname_32x33x41','/manybhmid_mysimname_12x13x17','/manybhmid_mysimname_16x17x25','/manybhmid_mysimname_24x25x33','/manybhmid_mysimname_32x33x41','/manybhfar_mysimname_12x13x17','/manybhfar_mysimname_16x17x25','/manybhfar_mysimname_24x25x33','/manybhfar_mysimname_32x33x41']


twopunDirArr=['/twopunnear_mysimname_50','/twopunmid_mysimname_50','/twopunfar_mysimname_50']


simname='mysimname'



# Legend locations 
legend_ncol=3
legend_fontsize=9  
loc={'best':0,
    'upper_right':1,
    'upper_left':2,
    'lower_left':3,
    'lower_right':4,
    'right':5,
    'center_left':6,
    'center_right':7,
    'lower_center':8,
    'upper_center':9,
    'center':10
    }


#Trim the edge of the data
Trim_Points=2

far_d_label_loc_manybh=loc['best']
far_x_label_loc_manybh=loc['best']
far_y_label_loc_manybh=loc['best']
far_z_label_loc_manybh=loc['best']

mid_d_label_loc_manybh=loc['best']
mid_x_label_loc_manybh=loc['best']
mid_y_label_loc_manybh=loc['best']
mid_z_label_loc_manybh=loc['best']

near_d_label_loc_manybh=loc['best']
near_x_label_loc_manybh=loc['best']
near_y_label_loc_manybh=loc['best']
near_z_label_loc_manybh=loc['best']    

far_d_label_loc_twopun=loc['best']
far_x_label_loc_twopun=loc['best']
far_y_label_loc_twopun=loc['best']
far_z_label_loc_twopun=loc['best']

mid_d_label_loc_twopun=loc['best']
mid_x_label_loc_twopun=loc['best']
mid_y_label_loc_twopun=loc['best']
mid_z_label_loc_twopun=loc['best']

near_d_label_loc_twopun=loc['best']
near_x_label_loc_twopun=loc['best']
near_y_label_loc_twopun=loc['best']
near_z_label_loc_twopun=loc['best']    
 

#========================================================================================================================================

for case in caseArr:
    #Loop through all the manybh simulations directories
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
	if(manybhDir[6:manybhDir.find('_')]==case):

            if(case=='near'):
                d_label_loc=near_d_label_loc_manybh
                x_label_loc=near_x_label_loc_manybh
                y_label_loc=near_y_label_loc_manybh
                z_label_loc=near_z_label_loc_manybh
            elif(case=='mid'):
                d_label_loc=mid_d_label_loc_manybh
                x_label_loc=mid_x_label_loc_manybh
                y_label_loc=mid_y_label_loc_manybh
                z_label_loc=mid_z_label_loc_manybh
            elif(case=='far'):
                d_label_loc=far_d_label_loc_manybh
                x_label_loc=far_x_label_loc_manybh
                y_label_loc=far_y_label_loc_manybh
                z_label_loc=far_z_label_loc_manybh
                
	    dataFiled='../'+manybhDir+'/admconstraints::hamiltonian.d.asc'
	    dataFilex='../'+manybhDir+'/admconstraints::hamiltonian.x.asc'
	    dataFiley='../'+manybhDir+'/admconstraints::hamiltonian.y.asc'
	    dataFilez='../'+manybhDir+'/admconstraints::hamiltonian.z.asc'

	    datad=np.loadtxt(dataFiled)
	    datax=np.loadtxt(dataFilex)
	    datay=np.loadtxt(dataFiley)
	    dataz=np.loadtxt(dataFilez)
            # make the legends ( labels ) : Lorene resolutions
            plot_label=manybhDir[manybhDir.rfind('_')+1:len(manybhDir)]
            #Plot the axis d
            i=0
            daxis=[]
	    ddata=[]
	    while (datad[i][0]==index):
                if(i>(Trim_Points-1)):
		    daxis.append(datad[i][9])
		    ddata.append(datad[i][12])
                i=i+1
		if(i>=len(datad)-Trim_Points):
		    break
	    ad.plot(daxis,np.log10(np.abs(ddata)),label=plot_label)
            ad.legend(loc=d_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})
            #Plot the axis x
            i=0
            xaxis=[]
	    xdata=[]
	    while (datax[i][0]==index):
                if(i>(Trim_Points-1)):
		    xaxis.append(datax[i][9])
		    xdata.append(datax[i][12])
                i=i+1 
		if(i>=len(datax)-Trim_Points):
		    break
	    ax.plot(xaxis,np.log10(np.abs(xdata)),label=plot_label)
            ax.legend(loc=x_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize}) 
	    #Plot the y axis
	    i=0
            yaxis=[]
	    ydata=[]
	    while (datay[i][0]==index):
                if(i>(Trim_Points-1)):
		    yaxis.append(datay[i][10])
		    ydata.append(datay[i][12])
                i=i+1                        
		if(i>=len(datay)-Trim_Points):
		    break
	    ay.plot(yaxis,np.log10(np.abs(ydata)),label=plot_label)
            ay.legend(loc=y_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})   

	   #Plot the z axis
            i=0
            zaxis=[]
	    zdata=[]
	    while (dataz[i][0]==index):
                if(i>(Trim_Points-1)):
		    zaxis.append(dataz[i][11])
		    zdata.append(dataz[i][12])
                i=i+1                        
		if(i>=len(dataz)-Trim_Points):
		    break
	    az.plot(zaxis,np.log10(np.abs(zdata)),label=plot_label)
            az.legend(loc=z_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize}) 
  


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

            if(case=='near'):
                d_label_loc=near_d_label_loc_twopun
                x_label_loc=near_x_label_loc_twopun
                y_label_loc=near_y_label_loc_twopun
                z_label_loc=near_z_label_loc_twopun
            elif(case=='mid'):
                d_label_loc=mid_d_label_loc_twopun
                x_label_loc=mid_x_label_loc_twopun
                y_label_loc=mid_y_label_loc_twopun
                z_label_loc=mid_z_label_loc_twopun
            elif(case=='far'):
                d_label_loc=far_d_label_loc_twopun
                x_label_loc=far_x_label_loc_twopun
                y_label_loc=far_y_label_loc_twopun
                z_label_loc=far_z_label_loc_twopun  


 	    tdataFiled='../'+twopunDir+'/admconstraints::hamiltonian.d.asc'
	    tdataFilex='../'+twopunDir+'/admconstraints::hamiltonian.x.asc'
	    tdataFiley='../'+twopunDir+'/admconstraints::hamiltonian.y.asc'
	    tdataFilez='../'+twopunDir+'/admconstraints::hamiltonian.z.asc'

	    tdatad=np.loadtxt(tdataFiled)
	    tdatax=np.loadtxt(tdataFilex)
	    tdatay=np.loadtxt(tdataFiley)
	    tdataz=np.loadtxt(tdataFilez)
            # make the legends ( labels ) : Lorene resolutions
            plot_label=twopunDir[twopunDir.rfind('_')+1:len(twopunDir)]  
            #Plot the axis d
            i=0
            tdaxis=[]
	    tddata=[]
	    while (tdatad[i][0]==index):
                if(i>(Trim_Points-1)):
		    tdaxis.append(tdatad[i][9])
		    tddata.append(tdatad[i][12])
                i=i+1
		if(i>=len(tdatad)-Trim_Points):
		    break
	    tad.plot(tdaxis,np.log10(np.abs(tddata)),label=plot_label)
            tad.legend(loc=d_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})
            #Plot the axis x
            i=0
            txaxis=[]
	    txdata=[]
	    while (tdatax[i][0]==index):
                if(i>(Trim_Points-1)):
		    txaxis.append(tdatax[i][9])
		    txdata.append(tdatax[i][12])
                i=i+1 
		if(i>=len(tdatax)-Trim_Points):
		    break
	    tax.plot(txaxis,np.log10(np.abs(txdata)),label=plot_label)
            tax.legend(loc=x_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})
	    #Plot the y axis
	    i=0
            tyaxis=[]
	    tydata=[]
	    while (tdatay[i][0]==index):
                if(i>(Trim_Points-1)):
		    tyaxis.append(tdatay[i][10])
		    tydata.append(tdatay[i][12])
                i=i+1                        
		if(i>=len(tdatay)-Trim_Points):
		    break
	    tay.plot(tyaxis,np.log10(np.abs(tydata)),label=plot_label)
            tay.legend(loc=y_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})

	   #Plot the z axis
            i=0
            tzaxis=[]
	    tzdata=[]
	    while (tdataz[i][0]==index):
                if(i>(Trim_Points-1)):
		    tzaxis.append(tdataz[i][11])
		    tzdata.append(tdataz[i][12])
                i=i+1                        
		if(i>=len(tdataz)-Trim_Points):
		    break
	    taz.plot(tzaxis,np.log10(np.abs(tzdata)),label=plot_label) 
            taz.legend(loc=z_label_loc,ncol=legend_ncol, prop={'size':legend_fontsize})
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
