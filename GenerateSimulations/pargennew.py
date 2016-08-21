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
sys.path.append('../zones')
import zones

# pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# BASEPATH = os.path.dirname(os.path.realpath(__file__))
BASEPATH = os.path.dirname(os.path.realpath(__file__)) #+ '/simulations/GenerateSimulations'


defaultData = os.path.join(BASEPATH, 'paroriginal/initdata.csv')

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
    try:
        val = df[df.variables == key][col].values[0]
        val = val.split(',')
        if len(val) == 1:
            return val[0]
        return val
    except IndexError:
        return False
    except Exception as e:
        print(str(e))
        sys.exit()


def getDataCollectionShiftFromUser(udata, key, case):

    try:
        tmpval = udata[key + '_' + case]['val']
        return tmpval
    except KeyError:
        return False


def calculateN(df):

    cases = getVal(df, 'cases')

    for case in cases:
        dx = float(getVal(df, 'dxyz', case))
        xmin = float(getVal(df, 'xmin', case))
        xmax = float(getVal(df, 'xmax', case))
        ymin = float(getVal(df, 'ymin', case))
        ymax = float(getVal(df, 'ymax', case))
        zmin = float(getVal(df, 'zmin', case))
        zmax = float(getVal(df, 'zmax', case))

        # driver::global_nx = 2561
        # driver::global_ny = 41
        # driver::global_nz = 41

        tmp_global_nx = int(np.abs(xmax - xmin)/dx) + 1
        df = updatedf(df, 'global_nx', case, str(tmp_global_nx))

        tmp_global_ny = int(np.abs(ymax - ymin)/dx) + 1
        df = updatedf(df, 'global_ny', case, str(tmp_global_ny))

        tmp_global_nz = int(np.abs(zmax - zmin)/dx) + 1
        df = updatedf(df, 'global_nz', case, str(tmp_global_nz))


    return df

def dataCollectionAxis(df, udata):

    # near case

    cases = getVal(df, 'cases')

    for case in cases:
        xmin = float(getVal(df, 'xmin', case))
        xmax = float(getVal(df, 'xmax', case))
        ymin = float(getVal(df, 'ymin', case))
        ymax = float(getVal(df, 'ymax', case))
        zmin = float(getVal(df, 'zmin', case))
        zmax = float(getVal(df, 'zmax', case))

        tmpval = getDataCollectionShiftFromUser(udata, 'out1D_xline_y', case)
        if tmpval:
            if (float(tmpval)) > ymax or (float(tmpval)) < ymin:
                print('Error - out1D_xline_y = %s: data collection axis is outside the grid [%s ... %s]' %(tmpval, ymin, ymax))
            df = updatedf(df, 'out1D_xline_y', case, tmpval)
        else:
            df = updatedf(df, 'out1D_xline_y', case, str((ymax - ymin)/2 + ymin))


        tmpval = getDataCollectionShiftFromUser(udata, 'out1D_xline_z', case)
        if tmpval:
            if float(tmpval) > zmax or (float(tmpval)) < zmin:
                print('Error - out1D_xline_z = %s: data collection axis is outside the grid [%s ... %s]' %(tmpval, zmin, zmax))
            df = updatedf(df, 'out1D_xline_z', case, tmpval)
        else:
            df = updatedf(df, 'out1D_xline_z', case, str((zmax - zmin)/2 + zmin))


        tmpval = getDataCollectionShiftFromUser(udata, 'out1D_yline_x', case)
        if tmpval:
            if float(tmpval) > xmax or (float(tmpval)) < xmin:
                print('Error - out1D_yline_x = %s: data collection axis is outside the grid [%s ... %s]' %(tmpval, xmin, xmax))
            df = updatedf(df, 'out1D_yline_x', case, tmpval)
        else:
            df = updatedf(df, 'out1D_yline_x', case, str((xmax - xmin)/2 + xmin))

        tmpval = getDataCollectionShiftFromUser(udata, 'out1D_yline_z', case)
        if tmpval:
            if float(tmpval) > zmax or (float(tmpval)) < zmin:
                print('Error - out1D_yline_z = %s: data collection axis is outside the grid [%s ... %s]' %(tmpval, zmin, zmax))
            df = updatedf(df, 'out1D_yline_z', case, tmpval)
        else:
            df = updatedf(df, 'out1D_yline_z', case, str((zmax - zmin)/2 + zmin))

        tmpval = getDataCollectionShiftFromUser(udata, 'out1D_zline_x', case)
        if tmpval:
            if float(tmpval) > xmax or (float(tmpval)) < xmin:
                print('Error - out1D_zline_x = %s: data collection axis is outside the grid [%s ... %s]' %(tmpval, xmin, xmax))
            df = updatedf(df, 'out1D_zline_x', case, tmpval)
        else:
            df = updatedf(df, 'out1D_zline_x', case, str((xmax - xmin)/2 + xmin))

        tmpval = getDataCollectionShiftFromUser(udata, 'out1D_zline_y', case)
        if tmpval:
            if float(tmpval) > ymax or (float(tmpval)) < ymin:
                print('Error - out1D_zline_y = %s: data collection axis is outside the grid [%s ... %s]' %(tmpval, ymin, ymax))
            df = updatedf(df, 'out1D_zline_y', case, tmpval)
        else:
            df = updatedf(df, 'out1D_zline_y', case, str((ymax - ymin)/2 + ymin))

    return df


def zoneplot(df, case):
    global BASEPATH, simname

    zplotScriptName = os.path.join(BASEPATH, 'paroriginal/zone.tex')

    dx = getVal(df, 'dxyz')

    # Near
    xmin = getVal(df, 'xmin', case)
    xmax = getVal(df, 'xmax', case)
    ymin = getVal(df, 'ymin', case)
    ymax = getVal(df, 'ymax', case)
    zmin = getVal(df, 'zmin', case)
    zmax = getVal(df, 'zmax', case)

    out1D_xline_y = getVal(df, 'out1D_xline_y', case)
    out1D_xline_z = getVal(df, 'out1D_xline_z', case)
    out1D_yline_x = getVal(df, 'out1D_yline_x', case)
    out1D_yline_z = getVal(df, 'out1D_yline_z', case)
    out1D_zline_x = getVal(df, 'out1D_zline_x', case)
    out1D_zline_y = getVal(df, 'out1D_zline_y', case)

    z = zones.zone(
        dx,
        xmin,
        xmax,
        ymin,
        ymax,
        zmin,
        zmax,
        out1D_xline_y,
        out1D_xline_z,
        out1D_yline_x,
        out1D_yline_z,
        out1D_zline_x,
        out1D_zline_y
    )

    xbh = getVal(df, 'xbh')
    boxpoints = z.gridBoxPoints()
    dataAxis = z.dataAxis()

    if type(xbh) is list:
        xbh=xbh[0]
    xbh = xbh.replace('x', ',')

    # line = line.replace('[==manybhDirArr==]',manybhDirlist+'\n\n')

    bhposition = "\\newcommand\\bhone{(%s)}" % (xbh)

    boxpointsList = {}
    for key in boxpoints:
        line = "\\newcommand\\%s{(%s, %s, %s)}" % (key, boxpoints[key][0], boxpoints[key][1], boxpoints[key][2])
        boxpointsList[key] = line

    boxpointsList['bhposition'] = bhposition

    dataAxisList = {}
    for key in dataAxis:
        line = "\\newcommand\\%s{(%s, %s, %s)}" % (key, dataAxis[key][0], dataAxis[key][1], dataAxis[key][2])
        dataAxisList[key] = line

    f = open(zplotScriptName, 'r+')
    w = open(simname + '/plots/zone_' + case + '.tex', 'w+')
    for line in f:
        newline = line
        for key in boxpointsList:
            old = "[==%s==]" % (key)
            newline = line.replace(old, boxpointsList[key] + '\n')
            if newline != line:
                break

        if newline == line:
            for key in dataAxisList:
                old = "[==%s==]" % (key)
                # print(old)
                newline = line.replace(old, dataAxisList[key] + '\n')
                if newline != line:
                    break

        w.write(newline)


def createZoneplotFile(df):
    cases = getVal(df, 'cases')
    for case in cases:
        zoneplot(df, case)




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
data = pd.read_csv(defaultData, sep='\t', dtype=object)
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

dataCollectionAxis(data, udata)
calculateN(data)

print("Simulation Parameters")
print('--------------------------------------------------------------------------------------------------------')
print(data.sort_values(by=['global']))
print('--------------------------------------------------------------------------------------------------------')

con = str(raw_input('These are the parameters for this simulation, Continue ? [y/n]')).lower().strip()
if con != 'y':
    print('Abort.')
    sys.exit()

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
plotScriptName = os.path.join(BASEPATH, 'paroriginal/plot.py')
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
    ParFileName = os.path.join(BASEPATH, 'paroriginal/manybh' + case + '.par')
    twopParFileName = os.path.join(BASEPATH, 'paroriginal/twopunc' + case + '.par')
    oParfile = open(ParFileName,'r')
    otwopParfile = open(twopParFileName,'r')

    simmethods = getVal(data, 'simmethods')
    exename = getVal(data, 'exename')
    nbh = getVal(data, 'nbh')
    xbh = getVal(data, 'xbh')
    if not type(xbh) is list:
        xbh = [xbh]

    pbh = getVal(data, 'pbh')
    if not type(pbh) is list:
        pbh = [pbh]

    sbh = getVal(data, 'sbh')
    if not type(sbh) is list:
        sbh = [sbh]

    resArray = getVal(data, 'nzpt')

    if 'twopunc' in simmethods:
        # twopunch sim files
        runScript.write("# Twopunch " + case + " simulations\n")
        runScript.write("# =====================================\n")
        twopunch_resArr = getVal(data, 'twopunch_res')

        if twopunch_resArr:
            if not type(twopunch_resArr) is list:
                twopunch_resArr = [twopunch_resArr]

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
                runScript.write("nohup ~/"+exename+" $SIM_PATH"+inputFileName+" > $SIM_PATH"+outputFileName+"\n")
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


                if (int(nbh) == 2):
                    twoeditFile.write("twopunctures :: par_m_plus = %s\n" % mbh[0])
                    twoeditFile.write("twopunctures :: par_m_minus = %s\n" % mbh[1])
                elif(int(nbh) == 1):
                    twoeditFile.write("twopunctures :: par_m_plus = %s\n" % mbh[0])


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
        else:
            print("Skipping Twopunch...")


    if 'manybh' in simmethods:
        # ManyBH Simulation par files
        runScript.write("# ManyBH " + case + " simulation\n")
        runScript.write("# ==================================\n")

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
            runScript.write("nohup ~/"+exename+" $SIM_PATH"+inputFileName+" > $SIM_PATH"+outputFileName+"\n")
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
            nz = getVal(data, 'nz')
            puncpower = getVal(data, 'puncpower')

            editFile.write("\n")

            nzpt = res.split('x')
            editFile.write("ManyBH :: nz        = %s\n" % (nz))
            editFile.write("ManyBH :: np        = %s\n" % nzpt[0])
            editFile.write("ManyBH :: nt        = %s\n" % nzpt[1])
            editFile.write("ManyBH :: nr        = %s\n" % nzpt[2])

            editFile.write("\n")

            editFile.write("ManyBH :: precis    = 1.0e-9\n")
            editFile.write("ManyBH :: ite_max   = 500\n")
            editFile.write("ManyBH :: relax     = 0.5\n")

            editFile.write("\n")

            editFile.write("ManyBH :: puncpower   = %s\n" % (puncpower))
            editFile.write("ManyBH :: rsurf     = %s" % (rsurf))

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
if 'editFile' in globals():
    editFile.close()
if 'twoeditFile' in globals():
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

print ('Par files are created in ' + simname + ' directory')


createZoneplotFile(data)

print('Done.')



