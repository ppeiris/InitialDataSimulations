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
import optparse
import pandas as pd

# update new values in in the default value set
def updatedf(data, key, col, val):

    if key in list(data.variables):
        # print("Updating key %s" %(key))
        index = data[data.variables == key].index[0]
        data.set_value(index, col, val)
        data.set_value(index, 'update', 'updated')
    else:
        # print("Key is not in the list. Adding the key (%s) to the data " %(key))
        newrow = {
            'variables': np.NaN,
            'global': np.NaN,
            'near': np.NaN,
            'mid': np.NaN,
            'far': np.NaN,
            'update': 'new'
        }
        newrow['variables'] = key
        newrow[col] = val
        data = data.append(newrow, ignore_index=True)
    return data

# get cell value from the df
def getVal(df, key, col='global'):
    val = df[df.variables == key][col].values[0]
    val = val.split(',')
    if len(val) == 1:
        return val[0]
    return val


VERSION = '1.0'
USAGE = '%prog [-h | --help] [--version][-f | --file]'
parser = optparse.OptionParser(usage=USAGE, version=VERSION)

parser.add_option(
    '-f',
    '--file',
    help='file name',
)

(options, args) = parser.parse_args()

if (options.file is None) or (not os.path.exists(options.file)):
    parser.error("Please enter a data file name with -f option")

datafile = os.path.join(os.getcwd(), options.file)

# Load the default values
data = pd.read_csv('initdata.csv', sep='\t', dtype=object)
# Load the data file in to dataframe
udata = pd.read_table(datafile, sep='\=', engine='python', comment='#', index_col='var')
tudata = udata
udata = udata.transpose()

data['update'] = 'initial'
for key in list(udata.columns):
    col = key.split('_')[-1]
    if col in ['near', 'mid', 'far']:
        nkey = "_".join(key.split('_')[:-1])
    else:
        nkey = key
        col = 'global'

    data = updatedf(data, nkey, col, udata[key]['val'])


# Build the dir for the par file

if data[data.variables == 'simname'].empty:
    print("Please define a simname varibale in your data file with the simulation name")
    sys.exit()

simname = getVal(data, 'simname')
simdir = os.path.join(os.getcwd(), simname)
if os.path.exists(simdir):
    reply = str(raw_input('Simulation filed already exists at ' + simdir + ', overwrite [y/n]')).lower().strip()
    if reply != 'y':
        print('Abort.')
        sys.exit()
    print("Continue...")
else:
    os.makedirs(simdir)
    os.makedirs(simdir + '/plots')


# Build the run script
runscriptName = os.path.join(os.getcwd(), simname, 'run_' + simname + '.sh')
runScript = open(runscriptName, 'w')
runScript.write("#!/bin/sh\n")
runScript.write("export SIM_PATH=`pwd`\n")
runScript.write("cd $SIM_PATH\n")
runScript.write("echo \"Simulation "+simname+"\" > SimulationStatus.out \n")
runScript.write("echo \"Simulation start at \" `date -u` >> SimulationStatus.out\n")
runScript.write("\n\n")
runScript.write("echo \"Simulations start\"\n")
# Plotting Script
plotScriptName = os.path.join(os.getcwd(), 'paroriginal/plot.py')
sh.copy(plotScriptName, simname + '/plots/')
newPlotScriptName = os.path.join(os.getcwd(), simname + '/plots/plot.py')
PlotScript=open(newPlotScriptName,'a+')

# build the par files
cases = getVal(data, 'cases')
twopunDirlist = ''
manybhDirlist = ''
mbh = getVal(data, 'mbh')
for case in cases:
    #Read the par file
    ParFileName = os.path.join(os.getcwd(), 'paroriginal/manybh' + case + '.par')
    twopParFileName = os.path.join(os.getcwd(), 'paroriginal/twopunc' + case + '.par')
    oParfile = open(ParFileName,'r')
    otwopParfile = open(twopParFileName,'r')

    # twopunch sim files
    runScript.write("# Twopunch " + case + " simulations\n")
    runScript.write("# =====================================\n")
    twopunch_resArr = getVal(data, 'twopunch_res')

    if not type(twopunch_resArr) is 'list':
        twopunch_resArr = [twopunch_resArr]
    exename = getVal(data, 'exename')
    for tres in twopunch_resArr:
        newtwoParFileName = os.path.join(os.getcwd(), simname, 'twopun' + case + '_' + simname + '_' + tres + '.par')
        inputFileName = '/twopun' + case + '_' + simname + '_' + tres + '.par'
        simulationDir = 'twopun' + case + '_' + simname + '_' + tres
        outputFileName = '/twopun' + case + '_' + simname + '_' + tres + '.out'
        sh.copy(twopParFileName, newtwoParFileName)
        twoeditFile = open(newtwoParFileName, 'a+')

        if (twopunDirlist):
            twopunDirlist+=',\''+simulationDir+'\''
        else:
            twopunDirlist+='\''+simulationDir+'\''

        # print inputFileName
        runScript.write("START=$(date +%s)\n")
        runScript.write("echo \"Simulation twopun"+case+"_"+simname+"_"+tres+" start at \"`date -u` >> SimulationStatus.out\n")
        runScript.write("echo \"Still working on ...\" >> SimulationStatus.out\n")
        runScript.write("nohup ./"+exename+" $SIM_PATH"+inputFileName+" > $SIM_PATH"+outputFileName+"\n")
        runScript.write("END=$(date +%s)\n")
        runScript.write("echo \"Simulation twopun"+case+"_"+simname+"_"+tres+" end at \"`date -u` >> SimulationStatus.out\n")
        #runScript.write("echo \"Simulation took\" $(($END-$START)) \"seconds\" >> SimulationStatus.out\n")
        runScript.write("\n")

        # fill the grid info
        twoeditFile.write('\n')
        twoeditFile.write("#--------------------------------------------------------------------------------------- \n")
        twoeditFile.write("# Grid Parameters:\n")
        twoeditFile.write("#--------------------------------------------------------------------------------------- \n")

        twoeditFile.write('\n')

        twoeditFile.write('grid::type       = \"%s\"\n' % getVal(data, 'type', case))
        twoeditFile.write('grid::domain     = \"%s\"\n' % getVal(data, 'domain', case))
        twoeditFile.write('grid::dxyz       = %s\n' % getVal(data, 'dxyz', case))
        twoeditFile.write('grid::xmin       = %s\n' % getVal(data, 'xmin', case))
        twoeditFile.write('grid::ymin       = %s\n' % getVal(data, 'ymin', case))
        twoeditFile.write('grid::zmin       = %s\n' % getVal(data, 'zmin', case))
        twoeditFile.write('grid::xmax       = %s\n' % getVal(data, 'xmax', case))
        twoeditFile.write('grid::ymax       = %s\n' % getVal(data, 'ymax', case))
        twoeditFile.write('grid::zmax       = %s\n' % getVal(data, 'zmax', case))

        twoeditFile.write('\n')

        twoeditFile.write('driver::global_nx    = %s\n' % getVal(data, 'global_nx', case))
        twoeditFile.write('driver::global_ny    = %s\n' % getVal(data, 'global_ny', case))
        twoeditFile.write('driver::global_nz    = %s\n' % getVal(data, 'global_nz', case))
        twoeditFile.write('driver::ghost_size   = %s\n' % getVal(data, 'ghost_size', case))

        twoeditFile.write('\n')

        twoeditFile.write('CoordBase::boundary_size_x_lower = %s\n' % getVal(data, 'boundary_size_x_lower', case))
        twoeditFile.write('CoordBase::boundary_size_x_upper = %s\n' % getVal(data, 'boundary_size_x_upper', case))
        twoeditFile.write('CoordBase::boundary_size_y_lower = %s\n' % getVal(data, 'boundary_size_y_lower', case))
        twoeditFile.write('CoordBase::boundary_size_y_upper = %s\n' % getVal(data, 'boundary_size_y_upper', case))
        twoeditFile.write('CoordBase::boundary_size_z_lower = %s\n' % getVal(data, 'boundary_size_z_lower', case))
        twoeditFile.write('CoordBase::boundary_size_z_upper = %s\n' % getVal(data, 'boundary_size_z_upper', case))

        twoeditFile.write('\n')

        twoeditFile.write('IOASCII::out1D_xline_y = %s\n' % getVal(data, 'out1D_xline_y', case))
        twoeditFile.write('IOASCII::out1D_xline_z = %s\n' % getVal(data, 'out1D_xline_z', case))
        twoeditFile.write('\n')
        twoeditFile.write('IOASCII::out1D_yline_x = %s\n' % getVal(data, 'out1D_yline_x', case))
        twoeditFile.write('IOASCII::out1D_yline_z = %s\n' % getVal(data, 'out1D_yline_z', case))
        twoeditFile.write('\n')
        twoeditFile.write('IOASCII::out1D_zline_x = %s\n' % getVal(data, 'out1D_zline_x', case))
        twoeditFile.write('IOASCII::out1D_zline_y = %s\n' % getVal(data, 'out1D_zline_y', case))

        twoeditFile.write('\n')

        twoeditFile.write("#--------------------------------------------------------------------------------------- \n")
        twoeditFile.write("# ManyBH Parameters:\n")
        twoeditFile.write("#--------------------------------------------------------------------------------------- \n")

        twoeditFile.write("twopunctures :: verbose=\"yes\"\n")
        twoeditFile.write("twopunctures :: grid_setup_method = \"evaluation\"\n")
        twoeditFile.write("twopunctures :: npoints_A = %s\n" % tres)
        twoeditFile.write("twopunctures :: npoints_B = %s\n" % tres)
        twoeditFile.write("twopunctures :: npoints_phi = %s\n" % tres)

        nbh = getVal(data, 'nbh')
        if (int(nbh) == 2):
            twoeditFile.write("twopunctures :: par_m_plus = %s\n" % mbh[0])
            twoeditFile.write("twopunctures :: par_m_minus = %s\n" % mbh[1])
        elif(int(nbh) == 1):
            twoeditFile.write("twopunctures :: par_m_plus = %s\n" % mbh[0])

        xbh = getVal(data, 'xbh')
        pbh = getVal(data, 'pbh')
        sbh = getVal(data, 'sbh')
        xbhval = xbh[0].split('x')
        twoeditFile.write("twopunctures :: par_b = %s\n"% xbhval[0])

        for i in range(0, int(nbh)):
            pbhval = pbh[i].split('x')
            sbhval = sbh[i].split('x')
            if(i == 0):
                twoeditFile.write('\n')
                twoeditFile.write("twopunctures :: par_P_plus[0] = %s\n" % pbhval[0])
                twoeditFile.write("twopunctures :: par_P_plus[1] = %s\n" % pbhval[1])
                twoeditFile.write("twopunctures :: par_P_plus[2] = %s\n" % pbhval[2])
            elif(i == 1):
                twoeditFile.write('\n')
                twoeditFile.write("twopunctures :: par_P_minus[0] = %s\n" % pbhval[0])
                twoeditFile.write("twopunctures :: par_P_minus[1] = %s\n" % pbhval[1])
                twoeditFile.write("twopunctures :: par_P_minus[2] = %s\n" % pbhval[2])
            if(i == 0):
                twoeditFile.write('\n')
                twoeditFile.write("twopunctures :: par_S_plus[0] = %s\n" % sbhval[0])
                twoeditFile.write("twopunctures :: par_S_plus[1] = %s\n" % sbhval[1])
                twoeditFile.write("twopunctures :: par_S_plus[2] = %s\n" % sbhval[2])
            elif(i == 1):
                twoeditFile.write('\n')
                twoeditFile.write("twopunctures :: par_S_minus[0] = %s\n" % sbhval[0])
                twoeditFile.write("twopunctures :: par_S_minus[1] = %s\n" % sbhval[1])
                twoeditFile.write("twopunctures :: par_S_minus[2] = %s\n" % sbhval[2])

    # ManyBH Simulation par files
    runScript.write("# ManyBH " + case + " simulation\n")
    runScript.write("# ==================================\n")
    resArray = getVal(data, 'nzpt')
    for res in resArray:
        newParFileName = os.path.join(os.getcwd(), simname +'/manybh' + case + '_' + simname + '_' + res + '.par')
        simulationDir='manybh'+case+'_'+simname+'_'+res
        inputFileName='/manybh'+case+'_'+simname+'_'+res+'.par'
        outputFileName='/manybh'+case+'_'+simname+'_'+res+'.out'
        # copy file with the new name
        sh.copy(ParFileName, newParFileName)
        # open the new file
        editFile = open(newParFileName, 'a+')

        #Plot Script==============
        #plotScriptName
        if(manybhDirlist):
            manybhDirlist+=',\''+simulationDir+'\''
        else:
            manybhDirlist+='\''+simulationDir+'\''


        runScript.write("START=$(date +%s)\n")
        runScript.write("echo \"Simulation ManyBH"+case+"_"+simname+"_"+res+" start at \"`date -u` >> SimulationStatus.out\n")
        runScript.write("echo \"Still working on ...\" >> SimulationStatus.out\n")
        runScript.write("nohup ./"+exename+" $SIM_PATH"+inputFileName+" > $SIM_PATH"+outputFileName+"\n")
        runScript.write("END=$(date +%s)\n")
        runScript.write("echo \"Simulation ManyBH"+case+"_"+simname+"_"+res+" end at \"`date -u` >> SimulationStatus.out\n")
        # runScript.write("echo \"Simulation took\" $($END-$START) \"seconds\" >> SimulationStatus.out\n")
        runScript.write("\n")


        #---Grid Parameters-------------------------------
        editFile.write("#--------------------------------------------------------------------------------------- \n")
        editFile.write("# Grid Parameters:\n")
        editFile.write("#--------------------------------------------------------------------------------------- \n")

        editFile.write('\n')

        editFile.write('grid::type = \"%s\"\n' % getVal(data, 'type', case))
        editFile.write('grid::domain = \"%s\"\n' % getVal(data, 'domain', case))
        editFile.write('grid::dxyz = %s\n' % getVal(data, 'dxyz', case))
        editFile.write('grid::xmin = %s\n' % getVal(data, 'xmin', case))
        editFile.write('grid::ymin = %s\n' % getVal(data, 'ymin', case))
        editFile.write('grid::zmin = %s\n' % getVal(data, 'zmin', case))
        editFile.write('grid::xmax = %s\n' % getVal(data, 'xmax', case))
        editFile.write('grid::ymax = %s\n' % getVal(data, 'ymax', case))
        editFile.write('grid::zmax = %s\n' % getVal(data, 'zmax', case))

        editFile.write('\n')

        editFile.write('driver::global_nx = %s\n' % getVal(data, 'global_nx', case))
        editFile.write('driver::global_ny = %s\n' % getVal(data, 'global_ny', case))
        editFile.write('driver::global_nz = %s\n' % getVal(data, 'global_nz', case))
        editFile.write('driver::ghost_size = %s\n' % getVal(data, 'ghost_size', case))

        editFile.write('\n')

        editFile.write('CoordBase::boundary_size_x_lower = %s\n' % getVal(data, 'boundary_size_x_lower', case))
        editFile.write('CoordBase::boundary_size_x_upper = %s\n' % getVal(data, 'boundary_size_x_upper', case))
        editFile.write('CoordBase::boundary_size_y_lower = %s\n' % getVal(data, 'boundary_size_y_lower', case))
        editFile.write('CoordBase::boundary_size_y_upper = %s\n' % getVal(data, 'boundary_size_y_upper', case))
        editFile.write('CoordBase::boundary_size_z_lower = %s\n' % getVal(data, 'boundary_size_z_lower', case))
        editFile.write('CoordBase::boundary_size_z_upper = %s\n' % getVal(data, 'boundary_size_z_upper', case))

        editFile.write('\n')

        editFile.write('IOASCII::out1D_xline_y = %s\n' %  getVal(data, 'out1D_xline_y', case))
        editFile.write('IOASCII::out1D_xline_z = %s\n' %  getVal(data, 'out1D_xline_z', case))
        editFile.write('\n')
        editFile.write('IOASCII::out1D_yline_x = %s\n' %  getVal(data, 'out1D_yline_x', case))
        editFile.write('IOASCII::out1D_yline_z = %s\n' %  getVal(data, 'out1D_yline_z', case))
        editFile.write('\n')
        editFile.write('IOASCII::out1D_zline_x = %s\n' %  getVal(data, 'out1D_zline_x', case))
        editFile.write('IOASCII::out1D_zline_y = %s\n' %  getVal(data, 'out1D_zline_y', case))


        editFile.write('\n')
        #---ManyBH Parameters-------------------------------
        editFile.write("#--------------------------------------------------------------------------------------- \n")
        editFile.write("# ManyBH Parameters:\n")
        editFile.write("#--------------------------------------------------------------------------------------- \n")

        rsurf = getVal(data, 'rsurf')

        editFile.write("ManyBH :: rsurf=%s" % rsurf)
        editFile.write("\n")

        nzpt = res.split('x')
        editFile.write("ManyBH :: nz        = 10\n")
        editFile.write("ManyBH :: np        = %s\n" % nzpt[0])
        editFile.write("ManyBH :: nt        = %s\n" % nzpt[1])
        editFile.write("ManyBH :: nr        = %s\n" % nzpt[2])
        editFile.write("ManyBH :: precis    = 1.0e-9\n")
        editFile.write("ManyBH :: ite_max   = 500\n")
        editFile.write("ManyBH :: relax     = 0.5\n")

        editFile.write("\n")

        editFile.write("ManyBH :: nbh = %s" % nbh)

        editFile.write("\n")

        for i in range(0,int(nbh)):
            editFile.write("\n")
            editFile.write("ManyBH :: mbh[%s] = %s\n" % (i, mbh[i]))

            sbhval=sbh[i].split('x')
            editFile.write("ManyBH :: sbh[%s] = %s\n" % ((i*3), sbhval[0]))
            editFile.write("ManyBH :: sbh[%s] = %s\n" % ((i*3)+1, sbhval[1]))
            editFile.write("ManyBH :: sbh[%s] = %s\n" % ((i*3)+2, sbhval[2]))

            pbhval=pbh[i].split('x')
            editFile.write("ManyBH :: pbh[%s] = %s\n" % ((i*3), pbhval[0]))
            editFile.write("ManyBH :: pbh[%s] = %s\n" % ((i*3)+1, pbhval[1]))
            editFile.write("ManyBH :: pbh[%s] = %s\n" % ((i*3)+2, pbhval[2]))

            xbhval=xbh[i].split('x')
            editFile.write("ManyBH :: xbh[%s] = %s\n" % ((i*3), xbhval[0]))
            editFile.write("ManyBH :: xbh[%s] = %s\n" % ((i*3)+1, xbhval[1]))
            editFile.write("ManyBH :: xbh[%s] = %s\n" % ((i*3)+2, xbhval[2]))

runScript.write("echo \"Done!\" >> SimulationStatus.out")
editFile.close()
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
f = open(plotScriptName,'r+')
w = open(simname+'/plots/plot.py','w+')
for line in f:
    line = line.replace('[==manybhDirArr==]',manybhDirlist+'\n\n')
    line = line.replace('[==twopunDirArr==]',twopunDirlist+'\n\n')
    line = line.replace('[==simname==]','simname=\''+simname+'\'\n\n')
    w.write(line)

print 'Par files are created in ' + simname + ' directory'

print('Done.')
