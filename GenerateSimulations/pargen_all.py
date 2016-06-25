#=======================================================================================
# Generate ManyBh and Twopunch parameter files for given configuration of blackholes
# Generate shell script to execute all the simulations
# Prabath Peiris
#=======================================================================================
import numpy as np
import scipy as sp
import string 
import shutil as sh
import os 
import sys

if(len(sys.argv)==2):
    datafile=sys.argv[1]
else:
    print 'Please enter the data file'
    sys.exit()

#cases=['near','mid','far']
cases=['near']


griddata_far={'type':'Byrange',
	  'domain':'full',
	  'dxyz':0.003125,
	  'xmin':4.9375,
	  'ymin':4.9375,
	  'zmin':4.9375,
	  'xmax':5.0625,
	  'ymax':5.0625,
	  'zmax':5.0625,
	  'global_nx':41,
	  'global_ny':41,
	  'global_nz':41,
 	  'out1D_xline_y':5.0,
	  'out1D_xline_z':5.0,
	  'out1D_yline_x':5.0,
	  'out1D_yline_z':5.0,
	  'out1D_zline_x':5.0,
	  'out1D_zline_y':5.0,
	  }

 
griddata_mid={'type':'Byrange',
	  'domain':'full',
	  'dxyz':0.003125, 
	  'xmin':-2.0, 
	  'ymin':-0.0125, 
	  'zmin':-0.0125, 
	  'xmax':2.0,
	  'ymax':0.0125, 
	  'zmax':0.0125, 
	  'global_nx':1281,
	  'global_ny':9,
	  'global_nz':9,
 	  'out1D_xline_y':0.0,
	  'out1D_xline_z':0.0,
	  'out1D_yline_x':0.0,
	  'out1D_yline_z':0.0,
	  'out1D_zline_x':0.0,
	  'out1D_zline_y':0.0,
	  }

griddata_near={'type':'Byrange',
	  'domain':'full',
	  'dxyz':0.003125, 
	  'xmin':2.9375, 
	  'ymin':0.4375,
	  'zmin':0.4375,
	  'xmax':3.0625, 
	  'ymax':0.5625,
	  'zmax':0.5625,
	  'global_nx':41,
	  'global_ny':41,
	  'global_nz':41,
	  'out1D_xline_y':0.5,
	  'out1D_xline_z':0.5,
	  'out1D_yline_x':3.0,
	  'out1D_yline_z':0.5,
	  'out1D_zline_x':3.0,
	  'out1D_zline_y':0.5,
	  }

pathcwd=os.getcwd() 
#print pathcwd
#parfilepath='/Users/prabath/Documents/bbhcode/parfiles/'
#dataFile=parfilepath+'data.txt'
#dataFile=pathcwd+'/data.txt'
dataFile=pathcwd+'/'+datafile

if(os.path.exists(dataFile)):
    print '============================================================='
else:
    print 'data file does not exists'
    print 'Abort!'
    sys.exit()



parfile=open(dataFile,"r")
linedata=parfile.readlines()

dxyz_near=''
xmin_near=''
xmax_near=''

dxyz_mid=''
xmin_mid=''
xmax_mid=''

dxyz_far=''
xmin_far=''
xmax_far=''
twopunch_resArr=''
precis=1.0e-9
nz=10
puncpower=2

for line in linedata:
    if(line[:4]=='nzpt'):
	resArray=line[5:].split(',')
    elif(line[:3]=='nbh'):
	nbh=line[4:]
    elif(line[:5]=='rsurf'):
    	rsurf=line[6:]
    elif(line[:3]=='mbh'):
    	mbh=line[4:].split(',')
    elif(line[:3]=='sbh'):
    	sbh=line[4:].split(',')
    elif(line[:3]=='pbh'):
    	pbh=line[4:].split(',')
    elif(line[:3]=='xbh'):
	xbh=line[4:].split(',')
    elif(line[:4]=='name'):
	simname=line[5:]
    elif(line[:12]=='twopunch_res'):
    	twopunch_resArr=line[13:].split(',')
    elif(line[:7]=='exename'):
    	exename=line[8:]
    elif(line[:9]=='dxyz_near'):
	dxyz_near=line[10:]
    elif(line[:9]=='xmax_near'):
	xmax_near=line[10:]
    elif(line[:9]=='xmin_near'):
	xmin_near=line[10:]
    elif(line[:8]=='dxyz_mid'):
	dxyz_mid=line[9:]
    elif(line[:8]=='xmax_mid'):
	xmax_mid=line[9:]
    elif(line[:8]=='xmin_mid'):
	xmin_mid=line[9:]      
    elif(line[:8]=='dxyz_far'):
	dxyz_far=line[9:]
    elif(line[:8]=='xmax_far'):
	xmax_far=line[9:]
    elif(line[:8]=='xmin_far'):
	xmin_far=line[9:]    
    elif(line[:6]=='precis'):
 	precis=line[7:]
    elif(line[:2]=='nz'):
	nz=line[3:]
    elif(line[:9]=='puncpower'):
    	puncpower=line[10:]    

simname=simname.strip()
exename=exename.strip()
#print simname
#print len(simname)

resArray[len(resArray)-1]= resArray[len(resArray)-1].rstrip() #removing the line brake '\n' character from the last entry
mbh[len(mbh)-1]= mbh[len(mbh)-1].rstrip() #removing the line brake '\n' character from the last entry
sbh[len(sbh)-1]= sbh[len(sbh)-1].rstrip() #removing the line brake '\n' character from the last entry
pbh[len(pbh)-1]= pbh[len(pbh)-1].rstrip() #removing the line brake '\n' character from the last entry
xbh[len(xbh)-1]= xbh[len(xbh)-1].rstrip() #removing the line brake '\n' character from the last entry
if(twopunch_resArr!=''):
    twopunch_resArr[len(twopunch_resArr)-1]= twopunch_resArr[len(twopunch_resArr)-1].rstrip() #removing the line brake '\n' character from the last entry

#make the directory for parfiles
#os.mkdir(simname)
if os.path.exists(simname):
    print 'Directory ' + simname + ' exists!'
    print 'Parameter files did not created'
    print 'Abort!'
    print '============================================================='
    sys.exit()
else:
    os.makedirs(simname)
    os.makedirs(simname+'/plots/')

runscriptName=pathcwd+'/'+simname+'/run_'+simname+'.sh'  
runScript=open(runscriptName,'w')
runScript.write("#!/bin/sh\n")
runScript.write("export SIM_PATH=`pwd`\n")
runScript.write("cd $SIM_PATH\n")
runScript.write("echo \"Simulation "+simname+"\" > SimulationStatus.out \n")
runScript.write("echo \"Simulation start at \" `date -u` >> SimulationStatus.out\n")
runScript.write("\n\n")
runScript.write("echo \"Simulations start\"\n")        
#Plotting Script========================================== 
plotScriptName=pathcwd+'/paroriginal/plot.py'  
sh.copy(plotScriptName,simname+'/plots/')
newPlotScriptName=pathcwd+'/'+simname+'/plots/plot.py'
#print newPlotScriptName                           
PlotScript=open(newPlotScriptName,'a+')  
#==========================================================

twopunDirlist=''
manybhDirlist=''


for case in cases:
    #Read the par file
    ParFileName=pathcwd+'/paroriginal/manybh'+case+'.par'
    twopParFileName=pathcwd+'/paroriginal/twopunc'+case+'.par' 
    oParfile=open(ParFileName,'r')
    otwopParfile=open(twopParFileName,'r')

    if(case=='near'):
	gtype=griddata_near['type']
        gdomain=griddata_near['domain']
	if(dxyz_near!=''):
	    gdxyz=dxyz_near
	else:    
	    gdxyz=griddata_near['dxyz']
	    
	if(xmin_near!=''):
	    gxmin=xmin_near
	else:
	    gxmin=griddata_near['xmin']

	if(xmax_near!=''):
	    gxmax=xmax_near
	else:
	    gxmax=griddata_near['xmax']

        gymin=griddata_near['ymin']
        gzmin=griddata_near['zmin']
	gymax=griddata_near['ymax']
	gzmax=griddata_near['zmax']
	gnx=griddata_near['global_nx']
	gny=griddata_near['global_ny']
	gnz=griddata_near['global_nz']
	dxy=griddata_near['out1D_xline_y'] 
	dxz=griddata_near['out1D_xline_z'] 
	dyx=griddata_near['out1D_yline_x'] 
	dyz=griddata_near['out1D_yline_z'] 
	dzx=griddata_near['out1D_zline_x'] 
	dzy=griddata_near['out1D_zline_y'] 
    elif(case=='mid'):
 	gtype=griddata_mid['type']
	gdomain=griddata_mid['domain']
  	
	if(dxyz_mid!=''):
	    gdxyz=dxyz_mid
	else:    
	    gdxyz=griddata_mid['dxyz']
	    
	if(xmin_mid!=''):
	    gxmin=xmin_mid
	else:
	    gxmin=griddata_mid['xmin']

	if(xmax_mid!=''):
	    gxmax=xmax_mid
	else:
	    gxmax=griddata_mid['xmax']
         
	gymin=griddata_mid['ymin']
	gzmin=griddata_mid['zmin']
	gymax=griddata_mid['ymax']
	gzmax=griddata_mid['zmax']
	gnx=griddata_mid['global_nx']
	gny=griddata_mid['global_ny']
	gnz=griddata_mid['global_nz']
 	dxy=griddata_mid['out1D_xline_y'] 
	dxz=griddata_mid['out1D_xline_z'] 
	dyx=griddata_mid['out1D_yline_x'] 
	dyz=griddata_mid['out1D_yline_z'] 
	dzx=griddata_mid['out1D_zline_x'] 
	dzy=griddata_mid['out1D_zline_y'] 
    elif(case=='far'):
        gtype=griddata_far['type']
	gdomain=griddata_far['domain']
 	
	if(dxyz_far!=''):
	    gdxyz=dxyz_far
	else:    
	    gdxyz=griddata_far['dxyz']
	    
	if(xmin_far!=''):
	    gxmin=xmin_far
	else:
	    gxmin=griddata_far['xmin']

	if(xmax_far!=''):
	    gxmax=xmax_far
	else:
	    gxmax=griddata_far['xmax']
         
	gymin=griddata_far['ymin']
	gzmin=griddata_far['zmin']
	gymax=griddata_far['ymax']
	gzmax=griddata_far['zmax']
	gnx=griddata_far['global_nx']
	gny=griddata_far['global_ny']
	gnz=griddata_far['global_nz']
 	dxy=griddata_far['out1D_xline_y'] 
	dxz=griddata_far['out1D_xline_z'] 
	dyx=griddata_far['out1D_yline_x'] 
	dyz=griddata_far['out1D_yline_z'] 
	dzx=griddata_far['out1D_zline_x'] 
	dzy=griddata_far['out1D_zline_y']      


    #twopunch simulations 
    if(twopunch_resArr!=''): 
    	runScript.write("# Twopunch "+case+" simulations\n")
    	runScript.write("# ==========================\n")
    	for tres in twopunch_resArr:
	    newtwoParFileName=pathcwd+'/'+simname+'/twopun'+case+'_'+simname+'_'+tres+'.par'  
	    inputFileName='/twopun'+case+'_'+simname+'_'+tres+'.par'  
	    simulationDir='twopun'+case+'_'+simname+'_'+tres
	    outputFileName='/twopun'+case+'_'+simname+'_'+tres+'.out'  
            sh.copy(twopParFileName,newtwoParFileName)
	    twoeditFile=open(newtwoParFileName,'a+')
            #Plot Script==============
            #plotScriptName
	    if(twopunDirlist):
		twopunDirlist+=',\''+simulationDir+'\''
	    else:
	        twopunDirlist+='\''+simulationDir+'\''

	    #=========================

            #print inputFileName
	    runScript.write("START=$(date +%s)\n")
	    runScript.write("echo \"Simulation twopun"+case+"_"+simname+"_"+tres+" start at \"`date -u` >> SimulationStatus.out\n")
	    runScript.write("echo \"Still working on ...\" >> SimulationStatus.out\n")
            runScript.write("nohup ./"+exename+" $SIM_PATH"+inputFileName+" > $SIM_PATH"+outputFileName+"\n")
	    runScript.write("END=$(date +%s)\n")
	    runScript.write("echo \"Simulation twopun"+case+"_"+simname+"_"+tres+" end at \"`date -u` >> SimulationStatus.out\n")
	    runScript.write("echo \"Simulation took\" $(($END-$START)) \"seconds\" >> SimulationStatus.out\n")
            runScript.write("\n")
	

	    #fill the grid info
	    twoeditFile.write('\n')
            twoeditFile.write("#--------------------------------------------------------------------------------------- \n")
	    twoeditFile.write("# Grid Parameters:\n")
            twoeditFile.write("#--------------------------------------------------------------------------------------- \n")
	
	    twoeditFile.write('\n')

	    twoeditFile.write('grid::type = \"%s\"\n' % gtype)
	    twoeditFile.write('grid::domain =\"%s\"\n' % gdomain)
	    twoeditFile.write('grid::dxyz =%s\n' % gdxyz)
	    twoeditFile.write('grid::xmin =%s\n' % gxmin)
	    twoeditFile.write('grid::ymin =%s\n' % gymin)
	    twoeditFile.write('grid::zmin =%s\n' % gzmin)
	    twoeditFile.write('grid::xmax =%s\n' % gxmax)
	    twoeditFile.write('grid::ymax =%s\n' % gymax)
	    twoeditFile.write('grid::zmax =%s\n' % gzmax)
	    twoeditFile.write('driver::global_nx   =%s\n' % gnx)
	    twoeditFile.write('driver::global_ny   =%s\n' % gny)
	    twoeditFile.write('driver::global_nz   =%s\n' % gnz)
            
	    twoeditFile.write('\n')
            
	    twoeditFile.write('IOASCII::out1D_xline_y = %s\n' %  dxy)
	    twoeditFile.write('IOASCII::out1D_xline_z = %s\n' %  dxz)
	    twoeditFile.write('\n')
	    twoeditFile.write('IOASCII::out1D_yline_x = %s\n' %  dyx)
	    twoeditFile.write('IOASCII::out1D_yline_z = %s\n' %  dyz)
	    twoeditFile.write('\n')
	    twoeditFile.write('IOASCII::out1D_zline_x = %s\n' %  dzx)
	    twoeditFile.write('IOASCII::out1D_zline_y = %s\n' %  dzy)
            
	    twoeditFile.write('\n')
            
            twoeditFile.write("#--------------------------------------------------------------------------------------- \n")
	    twoeditFile.write("# ManyBH Parameters:\n")
            twoeditFile.write("#--------------------------------------------------------------------------------------- \n")
             
	    twoeditFile.write("twopunctures :: verbose=\"yes\"\n")
	    twoeditFile.write("twopunctures :: grid_setup_method = \"evaluation\"\n")
	    twoeditFile.write("twopunctures :: npoints_A = %s\n" % tres)
	    twoeditFile.write("twopunctures :: npoints_B = %s\n" % tres)
	    twoeditFile.write("twopunctures :: npoints_phi = %s\n" % tres)
            
	    if (int(nbh) == 2):
	        twoeditFile.write("twopunctures :: par_m_plus = %s\n" % mbh[0])
	        twoeditFile.write("twopunctures :: par_m_minus = %s\n" % mbh[1])
	    elif(int(nbh)==1):
	        twoeditFile.write("twopunctures :: par_m_plus = %s\n" % mbh[0])
		

	    #xbhval1=xbh[0].split['x']
            xbhval=xbh[0].split('x')
	    twoeditFile.write("twopunctures :: par_b = %s\n"% xbhval[0])
            
            for i in range(0,int(nbh)):
	        pbhval=pbh[i].split('x')
	        sbhval=sbh[i].split('x')
	        if(i==0):
		    twoeditFile.write('\n')
	    	    twoeditFile.write("twopunctures :: par_P_plus[0] = %s\n" % pbhval[0])
	            twoeditFile.write("twopunctures :: par_P_plus[1] = %s\n" % pbhval[1])
	            twoeditFile.write("twopunctures :: par_P_plus[2] = %s\n" % pbhval[2])
	        elif(i==1):
	    	    twoeditFile.write('\n')
	    	    twoeditFile.write("twopunctures :: par_P_minus[0] = %s\n" % pbhval[0])
	            twoeditFile.write("twopunctures :: par_P_minus[1] = %s\n" % pbhval[1])
	            twoeditFile.write("twopunctures :: par_P_minus[2] = %s\n" % pbhval[2])
	        if(i==0):
	    	    twoeditFile.write('\n')
	    	    twoeditFile.write("twopunctures :: par_S_plus[0] = %s\n" % sbhval[0])
	    	    twoeditFile.write("twopunctures :: par_S_plus[1] = %s\n" % sbhval[1])
	    	    twoeditFile.write("twopunctures :: par_S_plus[2] = %s\n" % sbhval[2])
	        elif(i==1):
	    	    twoeditFile.write('\n')
	    	    twoeditFile.write("twopunctures :: par_S_minus[0] = %s\n" % sbhval[0])
	    	    twoeditFile.write("twopunctures :: par_S_minus[1] = %s\n" % sbhval[1])
	    	    twoeditFile.write("twopunctures :: par_S_minus[2] = %s\n" % sbhval[2])
            
    #ManyBH simulations    
    #Loop through resArray
    runScript.write("# ManyBH "+case+" simulation\n")
    runScript.write("# ==========================\n")
    for res in resArray:
	newParFileName=pathcwd+'/'+simname+'/manybh'+case+'_'+simname+'_'+res+'.par' 
	simulationDir='manybh'+case+'_'+simname+'_'+res
	inputFileName='/manybh'+case+'_'+simname+'_'+res+'.par'  
	outputFileName='/manybh'+case+'_'+simname+'_'+res+'.out'  
	#copy file with the new name
	sh.copy(ParFileName,newParFileName)
        #open the new file
	editFile=open(newParFileName,'a+')

        #Plot Script==============
        #plotScriptName
 	if(manybhDirlist):
	    manybhDirlist+=',\''+simulationDir+'\''
	else:
	    manybhDirlist+='\''+simulationDir+'\'' 

	#=========================     


	runScript.write("START=$(date +%s)\n") 
        runScript.write("echo \"Simulation ManyBH"+case+"_"+simname+"_"+res+" start at \"`date -u` >> SimulationStatus.out\n")
        runScript.write("echo \"Still working on ...\" >> SimulationStatus.out\n")
        runScript.write("nohup ./"+exename+" $SIM_PATH"+inputFileName+" > $SIM_PATH"+outputFileName+"\n")
        runScript.write("END=$(date +%s)\n")
        runScript.write("echo \"Simulation ManyBH"+case+"_"+simname+"_"+res+" end at \"`date -u` >> SimulationStatus.out\n")
        runScript.write("echo \"Simulation took\" $($END-$START) \"seconds\" >> SimulationStatus.out\n")
        runScript.write("\n") 


        #---Grid Parameters-------------------------------
        editFile.write("#--------------------------------------------------------------------------------------- \n")
	editFile.write("# Grid Parameters:\n")
        editFile.write("#--------------------------------------------------------------------------------------- \n")
	
	editFile.write('\n')

	editFile.write('grid::type = \"%s\"\n' % gtype)
	editFile.write('grid::domain =\"%s\"\n' % gdomain)
	editFile.write('grid::dxyz =%s\n' % gdxyz)
	editFile.write('grid::xmin =%s\n' % gxmin)
	editFile.write('grid::ymin =%s\n' % gymin)
	editFile.write('grid::zmin =%s\n' % gzmin)
	editFile.write('grid::xmax =%s\n' % gxmax)
	editFile.write('grid::ymax =%s\n' % gymax)
	editFile.write('grid::zmax =%s\n' % gzmax)
	editFile.write('driver::global_nx   =%s\n' % gnx)
	editFile.write('driver::global_ny   =%s\n' % gny)
	editFile.write('driver::global_nz   =%s\n' % gnz)

	editFile.write('\n')

	editFile.write('IOASCII::out1D_xline_y = %s\n' %  dxy)
	editFile.write('IOASCII::out1D_xline_z = %s\n' %  dxz)
	editFile.write('\n')
	editFile.write('IOASCII::out1D_yline_x = %s\n' %  dyx)
	editFile.write('IOASCII::out1D_yline_z = %s\n' %  dyz)
	editFile.write('\n')
	editFile.write('IOASCII::out1D_zline_x = %s\n' %  dzx)
	editFile.write('IOASCII::out1D_zline_y = %s\n' %  dzy)
 
	

	editFile.write('\n')
        #---ManyBH Parameters-------------------------------
        editFile.write("#--------------------------------------------------------------------------------------- \n")
	editFile.write("# ManyBH Parameters:\n")
        editFile.write("#--------------------------------------------------------------------------------------- \n")

	editFile.write("ManyBH :: rsurf=%s" % rsurf)
	editFile.write("\n")

        nzpt=res.split('x')
	editFile.write("ManyBH :: nz=%s\n" % nz)
	editFile.write("ManyBH :: np=%s\n" % nzpt[0])
	editFile.write("ManyBH :: nt=%s\n" % nzpt[1])
	editFile.write("ManyBH :: nr=%s\n" % nzpt[2])
	editFile.write("ManyBH :: precis=%s\n" % precis)
	editFile.write("ManyBH :: ite_max = 500\n")
	editFile.write("ManyBH :: relax = 0.5\n")
	editFile.write("\n")   
	editFile.write("ManyBH :: puncpower = %s\n" % puncpower)   
	editFile.write("\n")   
 	editFile.write("ManyBH :: nbh=%s" % nbh)
	for i in range(0,int(nbh)):
	    editFile.write("\n")
	    editFile.write("ManyBH :: mbh[%s]=%s\n" % (i, mbh[i]))
            
	    sbhval=sbh[i].split('x')
	    editFile.write("ManyBH :: sbh[%s]=%s\n" % ((i*3), sbhval[0]))
	    editFile.write("ManyBH :: sbh[%s]=%s\n" % ((i*3)+1, sbhval[1]))
	    editFile.write("ManyBH :: sbh[%s]=%s\n" % ((i*3)+2, sbhval[2]))

	    pbhval=pbh[i].split('x')
	    editFile.write("ManyBH :: pbh[%s]=%s\n" % ((i*3), pbhval[0]))
	    editFile.write("ManyBH :: pbh[%s]=%s\n" % ((i*3)+1, pbhval[1]))
	    editFile.write("ManyBH :: pbh[%s]=%s\n" % ((i*3)+2, pbhval[2]))
            
            xbhval=xbh[i].split('x')
	    editFile.write("ManyBH :: xbh[%s]=%s\n" % ((i*3), xbhval[0]))
	    editFile.write("ManyBH :: xbh[%s]=%s\n" % ((i*3)+1, xbhval[1]))
	    editFile.write("ManyBH :: xbh[%s]=%s\n" % ((i*3)+2, xbhval[2]))

runScript.write("echo \"Done!\" >> SimulationStatus.out")
editFile.close()
if(twopunch_resArr!=''):
    twoeditFile.close()
runScript.close()

twopunDirlist='twopunDirArr=['+twopunDirlist+']'  
manybhDirlist='manybhDirArr=['+manybhDirlist+']'  


#my_text = my_text.replace('Hello', 'Goodbye')

#PlotScript=PlotScript.replace('manybhDirArr',manybhDirlist)

#PlotScript.write(twopunDirlist+'\n')
#PlotScript.write(manybhDirlist+'\n')

PlotScript.close()


#PlotScript=open(newPlotScriptName,'a+')  
f=open(plotScriptName,'r+')
w=open(simname+'/plots/plot.py','w+')
for line in f:
        line=line.replace('[==manybhDirArr==]',manybhDirlist+'\n\n') 
        line=line.replace('[==twopunDirArr==]',twopunDirlist+'\n\n') 
        line=line.replace('[==simname==]','simname=\''+simname+'\'\n\n') 
        w.write(line)

print 'Par files are created in ' + simname + ' directory'
print 'Done.'
print '============================================================='
