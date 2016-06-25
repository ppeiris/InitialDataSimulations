#!/usr/bin/env python 

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

axisArr=['d','x','y','z']
caseArr=['near','mid','far']
index=0
#========================================================================================================================================
#Following 3 lines will be replaced by another python script according to the simulation parameters, Please do not change them manually
manybhDirArr=['manybhnear_2bh_noS_PinY_DifRes_4_12x13x17','manybhnear_2bh_noS_PinY_DifRes_4_16x17x25','manybhnear_2bh_noS_PinY_DifRes_4_24x25x33','manybhnear_2bh_noS_PinY_DifRes_4_32x33x41','manybhmid_2bh_noS_PinY_DifRes_4_12x13x17','manybhmid_2bh_noS_PinY_DifRes_4_16x17x25','manybhmid_2bh_noS_PinY_DifRes_4_24x25x33','manybhmid_2bh_noS_PinY_DifRes_4_32x33x41','manybhfar_2bh_noS_PinY_DifRes_4_12x13x17','manybhfar_2bh_noS_PinY_DifRes_4_16x17x25','manybhfar_2bh_noS_PinY_DifRes_4_24x25x33','manybhfar_2bh_noS_PinY_DifRes_4_32x33x41']


twopunDirArr=['twopunnear_2bh_noS_PinY_DifRes_4_20','twopunnear_2bh_noS_PinY_DifRes_4_30','twopunnear_2bh_noS_PinY_DifRes_4_40','twopunmid_2bh_noS_PinY_DifRes_4_20','twopunmid_2bh_noS_PinY_DifRes_4_30','twopunmid_2bh_noS_PinY_DifRes_4_40','twopunfar_2bh_noS_PinY_DifRes_4_20','twopunfar_2bh_noS_PinY_DifRes_4_30','twopunfar_2bh_noS_PinY_DifRes_4_40']


simname='2bh_noS_PinY_DifRes_4'


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
	    dataFiled='../'+manybhDir+'/admconstraints::hamiltonian.d.asc'
	    dataFilex='../'+manybhDir+'/admconstraints::hamiltonian.x.asc'
	    dataFiley='../'+manybhDir+'/admconstraints::hamiltonian.y.asc'
	    dataFilez='../'+manybhDir+'/admconstraints::hamiltonian.z.asc'

	    datad=np.loadtxt(dataFiled)
	    datax=np.loadtxt(dataFilex)
	    datay=np.loadtxt(dataFiley)
	    dataz=np.loadtxt(dataFilez)
            #Plot the axis d
            i=0
            daxis=[]
	    ddata=[]
	    while (datad[i][0]==index):
		daxis.append(datad[i][9])
		ddata.append(datad[i][12])
                i=i+1
		if(i>=len(datad)):
		    break
	    ad.plot(daxis,np.log10(np.abs(ddata)))

            #Plot the axis x
            i=0
            xaxis=[]
	    xdata=[]
	    while (datax[i][0]==index):
		xaxis.append(datax[i][9])
		xdata.append(datax[i][12])
                i=i+1 
		if(i>=len(datax)):
		    break
	    ax.plot(xaxis,np.log10(np.abs(xdata)))

	    #Plot the y axis
	    i=0
            yaxis=[]
	    ydata=[]
	    while (datay[i][0]==index):
		yaxis.append(datay[i][10])
		ydata.append(datay[i][12])
                i=i+1                        
		if(i>=len(datay)):
		    break
	    ay.plot(yaxis,np.log10(np.abs(ydata)))


	   #Plot the z axis
            i=0
            zaxis=[]
	    zdata=[]
	    while (dataz[i][0]==index):
		zaxis.append(dataz[i][11])
		zdata.append(dataz[i][12])
                i=i+1                        
		if(i>=len(dataz)):
		    break
	    az.plot(zaxis,np.log10(np.abs(zdata)))
            
    figd.savefig((case+'_d_manybh_'+simname+'.png'),bbox_inches='tight')
    figx.savefig((case+'_x_manybh_'+simname+'.png'),bbox_inches='tight')
    figy.savefig((case+'_y_manybh_'+simname+'.png'),bbox_inches='tight')
    figz.savefig((case+'_z_manybh_'+simname+'.png'),bbox_inches='tight')


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
 	    tdataFiled='../'+twopunDir+'/admconstraints::hamiltonian.d.asc'
	    tdataFilex='../'+twopunDir+'/admconstraints::hamiltonian.x.asc'
	    tdataFiley='../'+twopunDir+'/admconstraints::hamiltonian.y.asc'
	    tdataFilez='../'+twopunDir+'/admconstraints::hamiltonian.z.asc'

	    tdatad=np.loadtxt(tdataFiled)
	    tdatax=np.loadtxt(tdataFilex)
	    tdatay=np.loadtxt(tdataFiley)
	    tdataz=np.loadtxt(tdataFilez)

            #Plot the axis d
            i=0
            tdaxis=[]
	    tddata=[]
	    while (tdatad[i][0]==index):
		tdaxis.append(tdatad[i][9])
		tddata.append(tdatad[i][12])
                i=i+1
		if(i>=len(tdatad)):
		    break
	    tad.plot(tdaxis,np.log10(np.abs(tddata)))

            #Plot the axis x
            i=0
            txaxis=[]
	    txdata=[]
	    while (tdatax[i][0]==index):
		txaxis.append(tdatax[i][9])
		txdata.append(tdatax[i][12])
                i=i+1 
		if(i>=len(tdatax)):
		    break
	    tax.plot(txaxis,np.log10(np.abs(txdata)))

	    #Plot the y axis
	    i=0
            tyaxis=[]
	    tydata=[]
	    while (tdatay[i][0]==index):
		tyaxis.append(tdatay[i][10])
		tydata.append(tdatay[i][12])
                i=i+1                        
		if(i>=len(tdatay)):
		    break
	    tay.plot(tyaxis,np.log10(np.abs(tydata)))


	   #Plot the z axis
            i=0
            tzaxis=[]
	    tzdata=[]
	    while (tdataz[i][0]==index):
		tzaxis.append(tdataz[i][11])
		tzdata.append(tdataz[i][12])
                i=i+1                        
		if(i>=len(tdataz)):
		    break
	    taz.plot(tzaxis,np.log10(np.abs(tzdata))) 

    tfigd.savefig((case+'_d_twopun_'+simname+'.png'),bbox_inches='tight')
    tfigx.savefig((case+'_x_twopun_'+simname+'.png'),bbox_inches='tight')
    tfigy.savefig((case+'_y_twopun_'+simname+'.png'),bbox_inches='tight')
    tfigz.savefig((case+'_z_twopun_'+simname+'.png'),bbox_inches='tight')        
