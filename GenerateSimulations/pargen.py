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
#cases=['near']

xmin_near_shift = 0.0625
xmax_near_shift = 0.0625
ymin_near_shift = 0.4375
ymax_near_shift = 0.5625
zmin_near_shift = 0.4375
zmax_near_shift = 0.5625

xmin_mid_shift = 1.0
xmax_mid_shift = 1.0
ymin_mid_shift = 0.0125
ymax_mid_shift = 0.0125
zmin_mid_shift = 0.0125
zmax_mid_shift = 0.0125

xmin_far_shift = 1.9375
xmax_far_shift = 2.0625
ymin_far_shift = 4.9375
ymax_far_shift = 5.0625
zmin_far_shift = 4.9375
zmax_far_shift = 5.0625




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
ymin_near=''
ymax_near=''
zmin_near=''
zmax_near=''

dxyz_mid=''
xmin_mid=''
xmax_mid=''
ymin_mid=''
ymax_mid=''
zmin_mid=''
zmax_mid=''

dxyz_far=''
xmin_far=''
xmax_far=''
ymin_far=''
ymax_far=''
zmin_far=''
zmax_far=''
gridside='plus'




twopunch_resArr=''
precis=1.0e-9
nz=10
puncpower=2
cases=''
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
    print 'xmax_near', xmax_near
    elif(line[:9]=='xmin_near'):
    xmin_near=line[10:]
    print 'xmin_near', xmin_near
    elif(line[:9]=='ymin_near'):
    ymin_near=line[10:]
    elif(line[:9]=='ymax_near'):
    ymax_near=line[10:]
    elif(line[:9]=='zmin_near'):
    zmin_near=line[10:]
    elif(line[:9]=='zmax_near'):
    zmax_near=line[10:]
    elif(line[:8]=='dxyz_mid'):
    dxyz_mid=line[9:]
    elif(line[:8]=='xmax_mid'):
    xmax_mid=line[9:]
    elif(line[:8]=='xmin_mid'):
    xmin_mid=line[9:]
    elif(line[:8]=='ymax_mid'):
    ymax_mid=line[9:]
    elif(line[:8]=='ymin_mid'):
    ymin_mid=line[9:]
    elif(line[:8]=='zmax_mid'):
    zmax_mid=line[9:]
    elif(line[:8]=='zmin_mid'):
    zmin_mid=line[9:]
    elif(line[:8]=='dxyz_far'):
    dxyz_far=line[9:]
    elif(line[:8]=='xmax_far'):
    xmax_far=line[9:]
    elif(line[:8]=='xmin_far'):
    xmin_far=line[9:]
    elif(line[:8]=='ymax_far'):
    ymax_far=line[9:]
    elif(line[:8]=='ymin_far'):
    ymin_far=line[9:]
    elif(line[:8]=='zmax_far'):
    zmax_far=line[9:]
    elif(line[:8]=='zmin_far'):
    zmin_far=line[9:]
    elif(line[:6]=='precis'):
    precis=line[7:]
    elif(line[:2]=='nz'):
    nz=line[3:]
    elif(line[:9]=='puncpower'):
        puncpower=line[10:]
    elif(line[:5]=='cases'):
    cases=line[6:].split(',')
    elif(line[:8]=='gridside'):
        gridside=line[9:]
    elif(line[:14]=='global_nx_near'):
        gnx=line[15:]
    elif(line[:14]=='global_ny_near'):
        gny=line[15:]
    elif(line[:14]=='global_nz_near'):
        gnz=line[15:]


    #elif(line[:5].rstrip()=='ndxyz'):
    #ndxyz=line[6:]
    #    griddata_near['dxyz']=line[6:].rstrip()
    #elif(line[:5].rstrip()=='nxmin'):
    #    griddata_near['xmin']=line[6:].rstrip()
    #elif(line[:5].rstrip()=='nymin'):
    #    griddata_near['ymin']=line[6:].rstrip()
    #elif(line[:5].rstrip()=='nzmin'):
    #    griddata_near['zmin']=line[6:].rstrip()
    #    print 'zmin', line
    #elif(line[:5].rstrip()=='nxmax'):
    #    griddata_near['xmax']=line[6:].rstrip()
    #elif(line[:5].rstrip()=='nymax'):
    #    griddata_near['ymax']=line[6:].rstrip()
    #elif(line[:5].rstrip()=='nzmax'):
    #    griddata_near['zmax']=line[6:].rstrip()
    #    print 'zmax', line

#nxmin=2.9375
#nymin=0.4375
#nzmin=0.4375
#nxmax=3.0625
#nymax=0.5625
#nzmax=0.5625



if(cases==''):
    cases=['near','mid','far']
else:
    cases[len(cases)-1]= cases[len(cases)-1].rstrip() #removing the line brake '\n' character from the last entry

gridside=gridside.strip()
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



# Calculate the near,mid and far regions
# near
# xbhtmp = xbh[0].split('x')
#


for case in cases:
    #Read the par file
    ParFileName=pathcwd+'/paroriginal/manybh'+case+'.par'
    twopParFileName=pathcwd+'/paroriginal/twopunc'+case+'.par'
    oParfile=open(ParFileName,'r')
    otwopParfile=open(twopParFileName,'r')

    if(case=='near'):
    # Calculate near grid zone -------------------------------
    # check for the symetry in x axis
    xbh_plus=xbh[0].split('x')
    xbh_minus=xbh[1].split('x')
    # x - value
    #print 'x: ',xbh_plus[0]
    #print 'y: ',xbh_plus[1]
    #print 'z: ',xbh_plus[2]
        print 'gridside : ', gridside
    if(gridside=='plus'):
        print 'plus side'
        xmin_plus_near=float(xbh_plus[0])-xmin_near_shift
        xmax_plus_near=float(xbh_plus[0])+xmax_near_shift
        ymin_plus_near=float(xbh_plus[1])+ymin_near_shift
        ymax_plus_near=float(xbh_plus[1])+ymax_near_shift
        zmin_plus_near=float(xbh_plus[2])+zmin_near_shift
        zmax_plus_near=float(xbh_plus[2])+zmax_near_shift
    elif(gridside=='minus'):
        print 'Minus side'
        xmin_minus_near=float(xbh_minus[0])-xmin_near_shift
        xmax_minus_near=float(xbh_minus[0])+xmax_near_shift
        ymin_minus_near=float(xbh_minus[1])+ymin_near_shift
        ymax_minus_near=float(xbh_minus[1])+ymax_near_shift
        zmin_minus_near=float(xbh_minus[2])+zmin_near_shift
        zmax_minus_near=float(xbh_minus[2])+zmax_near_shift



        #print 'xmin_plus_near = ',xmin_plus_near
    #print 'xmax_plus_near = ',xmax_plus_near
        #
    #print 'ymin_plus_near = ',ymin_plus_near
    #print 'ymax_plus_near = ',ymax_plus_near
        #
    #print 'zmin_plus_near = ',zmin_plus_near
    #print 'zmax_plus_near = ',zmax_plus_near

    #print '======================================'
    #
    #---------------------------------------------------------

    gtype=griddata_near['type']
        gdomain=griddata_near['domain']
    if(dxyz_near!=''):
        gdxyz=dxyz_near
    else:
        gdxyz=griddata_near['dxyz']

    if(xmin_near!=''):
        gxmin=xmin_near
        print 'getting the xmin from file'
    else:
        gxmin=griddata_near['xmin']
        print 'getting the xmin from array'

    if(xmax_near!=''):
        gxmax=xmax_near
    else:
        gxmax=griddata_near['xmax']


        if(ymin_near!=''):
        gymin=ymin_near
    else:
        gymin=griddata_near['ymin']

    if(ymax_near!=''):
        gymax=ymax_near
    else:
        gymax=griddata_near['ymax']

        if(zmin_near!=''):
        gzmin=zmin_near
    else:
        gzmin=griddata_near['zmin']

    if(zmax_near!=''):
        gzmax=zmax_near
    else:
        gzmax=griddata_near['zmax']


        #gymin=griddata_near['ymin']
        #gzmin=griddata_near['zmin']
    #gymax=griddata_near['ymax']
    #gzmax=griddata_near['zmax']



        #if(gridside=='plus'):
    #    gxmin=xmin_plus_near
    #    gxmax=xmax_plus_near
    #    gymin=ymin_plus_near
        #    gymax=ymax_plus_near
    #    gzmin=zmin_plus_near
    #    gzmax=zmax_plus_near
    #elif(gridside=='minus'):
    #    print 'minus side'
    #    gxmin=xmin_minus_near
    #    gxmax=xmax_minus_near
    #    gymin=ymin_minus_near
        #    gymax=ymax_minus_near
    #    gzmin=zmin_minus_near
    #    gzmax=zmax_minus_near




    #gnx=griddata_near['global_nx']
    #gny=griddata_near['global_ny']
    #gnz=griddata_near['global_nz']



    #Calculate the x y and z axis positions for the grid on the run

    # xline_y = ((ymax-ymin)/2 + ymin)
        dxy=((float(gymax)-float(gymin))/2+float(gymin))
        #print 'dxy = ',dxy

    # xline_z = ((zmax-zmin)/2 + zmin)
    dxz=((float(gzmax)-float(gzmin))/2+float(gzmin))
        #print 'dxz = ',dxz

    # yline_x = ((xmax-xmin)/2 + xmin)
    dyx=((float(gxmax)-float(gxmin))/2+float(gxmin))
        #print 'dyx = ',dyx


    # yline_z = ((zmax-zmin)/2 + zmin)
    dyz=((float(gzmax)-float(gzmin))/2+float(gzmin))
        #print 'dyz = ',dyz


    # zline_x = ((xmax-xmin)/2 + xmin)
    dzx=((float(gxmax)-float(gxmin))/2+float(gxmin))
        #print 'dzx = ',dzx

    # zline_y = ((ymin+ymax)/2 + ymin)
    dzy=((float(gymax)-float(gymin))/2+float(gymin))
        #print 'dzy = ',dzy

    #dxy=griddata_near['out1D_xline_y']
    #dxz=griddata_near['out1D_xline_z']

    #dyx=griddata_near['out1D_yline_x']
    #dyz=griddata_near['out1D_yline_z']

    #dzx=griddata_near['out1D_zline_x']
    #dzy=griddata_near['out1D_zline_y']


    elif(case=='mid'):
    gtype=griddata_mid['type']
    gdomain=griddata_mid['domain']

        # Calculate mid grid zone -------------------------------
    # check for the symetry in x axis
    xbh_plus=xbh[0].split('x')
    xbh_minus=xbh[1].split('x')

        print 'x: ',xbh_plus[0]
    print 'y: ',xbh_plus[1]
    print 'z: ',xbh_plus[2]

    print 'x - : ',xbh_minus[0]
    print 'y - : ',xbh_minus[1]
    print 'z - : ',xbh_minus[2]
    # x - value


    xmin_plus_mid=float(xbh_minus[0])+((np.absolute(float(xbh_plus[0]))+np.absolute(float(xbh_minus[0]))-4.0)/2.0) # keep the width of the mid x grid = 4)
    xmax_plus_mid=float(xbh_plus[0])-((np.absolute(float(xbh_plus[0]))+np.absolute(float(xbh_minus[0]))-4.0)/2.0)
    ymin_plus_mid=float(xbh_plus[1])-ymin_mid_shift
    ymax_plus_mid=float(xbh_plus[1])+ymax_mid_shift
    zmin_plus_mid=float(xbh_plus[2])-zmin_mid_shift
    zmax_plus_mid=float(xbh_plus[2])+zmin_mid_shift
    # for mid case, its the same grid
    #
    #---------------------------------------------------------

        #print 'xmin_plus_mid =',xmin_plus_mid
    #print 'xmax_plus_mid =',xmax_plus_mid

    #print 'ymin_plus_mid =',ymin_plus_mid
    #print 'ymax_plus_mid =',ymax_plus_mid

        #print 'zmin_plus_mid =',zmin_plus_mid
    #print 'zmax_plus_mid =',zmax_plus_mid


    #print '======================================'



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

    if(ymin_mid!=''):
        gymin=ymin_mid
    else:
        gymin=griddata_mid['ymin']

    if(ymax_mid!=''):
        gymax=ymax_mid
    else:
        gymax=griddata_mid['ymax']

    if(zmin_mid!=''):
        gzmin=zmin_mid
    else:
        gzmin=griddata_mid['zmin']

    if(zmax_mid!=''):
        gzmax=zmax_mid
    else:
        gzmax=griddata_mid['zmax']

    #gymin=griddata_mid['ymin']
    #gzmin=griddata_mid['zmin']
    #gymax=griddata_mid['ymax']
    #gzmax=griddata_mid['zmax']
    gnx=griddata_mid['global_nx']
    gny=griddata_mid['global_ny']
    gnz=griddata_mid['global_nz']


    gxmin=xmin_plus_mid
    gxmax=xmax_plus_mid
    gymin=ymin_plus_mid
    gymax=ymax_plus_mid
    gzmin=zmin_plus_mid
    gzmax=zmax_plus_mid

    # xline_y = ((ymax-ymin)/2 + ymin)
        dxy=((float(gymax)-float(gymin))/2+float(gymin))
        #print 'dxy = ',dxy

    # xline_z = ((zmax-zmin)/2 + zmin)
    dxz=((float(gzmax)-float(gzmin))/2+float(gzmin))
        #print 'dxz = ',dxz

    # yline_x = ((xmax-xmin)/2 + xmin)
    dyx=((float(gxmax)-float(gxmin))/2+float(gxmin))
        #print 'dyx = ',dyx


    # yline_z = ((zmax-zmin)/2 + zmin)
    dyz=((float(gzmax)-float(gzmin))/2+float(gzmin))
        #print 'dyz = ',dyz


    # zline_x = ((xmax-xmin)/2 + xmin)
    dzx=((float(gxmax)-float(gxmin))/2+float(gxmin))
        #print 'dzx = ',dzx

    # zline_y = ((ymin+ymax)/2 + ymin)
    dzy=((float(gymax)-float(gymin))/2+float(gymin))
        #print 'dzy = ',dzy


    #dxy=griddata_mid['out1D_xline_y']
    #dxz=griddata_mid['out1D_xline_z']
    #dyx=griddata_mid['out1D_yline_x']
    #dyz=griddata_mid['out1D_yline_z']
    #dzx=griddata_mid['out1D_zline_x']
    #dzy=griddata_mid['out1D_zline_y']
    elif(case=='far'):
        gtype=griddata_far['type']
    gdomain=griddata_far['domain']

    # Calculate mid grid zone -------------------------------
    # check for the symetry in x axis
    xbh_plus=xbh[0].split('x')
    xbh_minus=xbh[1].split('x')
    #print 'x: ',xbh_plus[0]
    #print 'y: ',xbh_plus[1]
    #print 'z: ',xbh_plus[2]

        #print 'x - : ',xbh_minus[0]
    #print 'y - : ',xbh_minus[1]
    #print 'z - : ',xbh_minus[2]

    # x - value
    if(gridside=='plus'):
        xmin_plus_far=float(xbh_plus[0])+xmin_far_shift
        xmax_plus_far=float(xbh_plus[0])+xmax_far_shift
        ymin_plus_far=float(xbh_plus[1])+ymin_far_shift
        ymax_plus_far=float(xbh_plus[1])+ymax_far_shift
        zmin_plus_far=float(xbh_plus[2])+zmin_far_shift
        zmax_plus_far=float(xbh_plus[2])+zmax_far_shift
        elif(gridside=='minus'):
        xmin_minus_far=float(xbh_minus[0])+xmin_far_shift
        xmax_minus_far=float(xbh_minus[0])+xmax_far_shift
        ymin_minus_far=float(xbh_minus[1])+ymin_far_shift
        ymax_minus_far=float(xbh_minus[1])+ymax_far_shift
        zmin_minus_far=float(xbh_minus[2])+zmin_far_shift
        zmax_minus_far=float(xbh_minus[2])+zmax_far_shift




    #print 'xmin_plus_far =',xmin_plus_far
    #print 'xmax_plus_far =',xmax_plus_far

    #print 'ymin_plus_far =',ymin_plus_far
    #print 'ymax_plus_far =',ymax_plus_far

    #print 'zmin_plus_far =',zmin_plus_far
    #print 'zmax_plus_far =',zmax_plus_far


    #print '======================================'
        #------------------------------------------------------------------

    if(dxyz_far!=''):
        gdxyz=dxyz_far
    else:
        gdxyz=griddata_far['dxyz']


        #------------------------------------------------------------------
    if(xmin_far!=''):
        gxmin=xmin_far
    else:
        gxmin=griddata_far['xmin']

    if(xmax_far!=''):
        gxmax=xmax_far
    else:
        gxmax=griddata_far['xmax']


        #------------------------------------------------------------------


        if(ymin_far!=''):
        gymin=ymin_far
    else:
        gymin=griddata_far['ymin']


    if(ymax_far!=''):
        gymax=ymax_far
    else:
        gymax=griddata_far['ymax']

        #------------------------------------------------------------------


    if(zmin_far!=''):
        gzmin=zmin_far
    else:
        gzmin=griddata_far['zmin']

    if(zmax_far!=''):
        gzmax=zmax_far
    else:
        gzmax=griddata_far['zmax']

        #------------------------------------------------------------------
    #gymin=griddata_far['ymin']
    #gzmin=griddata_far['zmin']
    #gymax=griddata_far['ymax']
    #gzmax=griddata_far['zmax']
    gnx=griddata_far['global_nx']
    gny=griddata_far['global_ny']
    gnz=griddata_far['global_nz']

        if(gridside=='plus'):
        gxmin=xmin_plus_far
        gxmax=xmax_plus_far
        gymin=ymin_plus_far
        gymax=ymax_plus_far
        gzmin=zmin_plus_far
        gzmax=zmax_plus_far
        elif(gridside=='minus'):
        gxmin=xmin_minus_far
        gxmax=xmax_minus_far
        gymin=ymin_minus_far
        gymax=ymax_minus_far
        gzmin=zmin_minus_far
        gzmax=zmax_minus_far

    # xline_y = ((ymax-ymin)/2 + ymin)
        dxy=((float(gymax)-float(gymin))/2+float(gymin))

    # xline_z = ((zmax-zmin)/2 + zmin)
    dxz=((float(gzmax)-float(gzmin))/2+float(gzmin))

    # yline_x = ((xmax-xmin)/2 + xmin)
    dyx=((float(gxmax)-float(gxmin))/2+float(gxmin))

    # yline_z = ((zmax-zmin)/2 + zmin)
    dyz=((float(gzmax)-float(gzmin))/2+float(gzmin))

    # zline_x = ((xmax-xmin)/2 + xmin)
    dzx=((float(gxmax)-float(gxmin))/2+float(gxmin))

    # zline_y = ((ymin+ymax)/2 + ymin)
    dzy=((float(gymax)-float(gymin))/2+float(gymin))

    #dxy=griddata_far['out1D_xline_y']
    #dxz=griddata_far['out1D_xline_z']
    #dyx=griddata_far['out1D_yline_x']
    #dyz=griddata_far['out1D_yline_z']
    #dzx=griddata_far['out1D_zline_x']
    #dzy=griddata_far['out1D_zline_y']


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
