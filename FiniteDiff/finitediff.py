import numpy as np
import csv
import pandas as pd
import os
import sys
import optparse
import numpy as np

pd.options.display.float_format = '{:.10g}'.format

inputFiles = {
    1: { 'file': 'dx0.000390625.txt', 'outfile': 'out0.000390625.csv'},
    2: { 'file': 'dx0.00078125.txt', 'outfile': 'out0.00078125.csv'},
    3: { 'file': 'dx0.0015625.txt', 'outfile': 'out0.0015625.csv'},
    4: { 'file': 'dx0.003125.txt', 'outfile': 'out0.003125.csv'},
    5: { 'file': 'dx0.00625.txt', 'outfile': 'out0.00625.csv'},
    6: { 'file': 'dx0.0125.txt', 'outfile': 'out0.0125.csv'},
    7: { 'file': 'dx0.025.txt', 'outfile': 'out0.025.csv'},
    8: { 'file': 'dx0.05.txt', 'outfile': 'out0.05.csv'},
    # 9: { 'file': 'dx0.1.txt', 'outfile': 'out0.1.csv'},
    # 10: { 'file': 'dx0.2.txt', 'outfile': 'out0.2.csv'},
    # 11: { 'file': 'dx0.4.txt', 'outfile': 'out0.4.csv'}
}

global df
global dfl2

def getVal(askv):
    global df
    value = df[df.variable == askv]['value']
    if askv != 'zone':
        return float(value)
    return str(value)

def calOtherVariables():
    global df

    # calculate ymin and ymax

    # yzlen = 5.0 * getVal('dxyz')
    # ymax = yzlen/2
    # ymin = -ymax
    # zmax = ymax
    # zmin = -ymax

    away = 0.5

    yzlen = 5.0 * getVal('dxyz')

    ymin = away - (yzlen/2)
    ymax = away + (yzlen/2)

    zmin = away - (yzlen/2)
    zmax = away + (yzlen/2)

    print(ymin)
    print(ymax)
    print(zmin)
    print(zmax)

    nvar = {'variable': 'ymax', 'value': ymax}
    df = df.append(nvar, ignore_index=True)

    nvar = {'variable': 'ymin', 'value': ymin}
    df = df.append(nvar, ignore_index=True)

    nvar = {'variable': 'zmin', 'value': zmin}
    df = df.append(nvar, ignore_index=True)

    nvar = {'variable': 'zmax', 'value': zmax}
    df = df.append(nvar, ignore_index=True)

    nvar = {'variable': 'nx', 'value': round(np.abs((getVal('xmax') - getVal('xmin')))/getVal('dxyz'), 0)}
    df = df.append(nvar, ignore_index=True)

    nvar = {'variable': 'ny', 'value': round(np.abs((getVal('ymax') - getVal('ymin')))/getVal('dxyz'), 0)}

    df = df.append(nvar, ignore_index=True)
    nvar = {'variable': 'nz', 'value': round(np.abs((getVal('zmax') - getVal('zmin')))/getVal('dxyz'), 0)}
    df = df.append(nvar, ignore_index=True)

    print(df)


def fVal(x, y ,z):
    m = 1.0
    x = x - 3.0
    r = np.sqrt(x*x + y*y + z*z)
    return (1.0 + m/(2.0 * r))


def solveLaplaceEq(outfile):
    global dfl2
    nx = int(getVal('nx'))
    ny = int(getVal('ny'))
    nz = int(getVal('nz'))

    xmin = getVal('xmin')
    ymin = getVal('ymin')
    zmin = getVal('zmin')
    h = getVal('dxyz')

    datadf = pd.DataFrame()
    for i in range(0, nx+1):
        for j in range(2, ny-2):
            for k in range(2, nz-2):
                dxx = -fVal(xmin + (h * (i + 2)), ymin + (h * j), zmin + (h * k))
                dxx += 16.0 * fVal(xmin + (h * (i + 1)), ymin + (h * j), zmin + (h * k))
                dxx += -30.0 * fVal(xmin + (h * i), ymin + (h * j), zmin + (h * k))
                dxx += 16.0 * fVal(xmin + (h * (i - 1)), ymin + (h * j), zmin + (h * k))
                dxx += -fVal(xmin + (h * (i - 2)), ymin + (h * j), zmin + (h * k))

                dyy = -fVal(xmin + (h * i), ymin + (h * (j + 2)), zmin + (h * k))
                dyy += 16.0 * fVal(xmin + (h * i), ymin + (h * (j + 1)), zmin + (h * k))
                dyy += -30.0 * fVal(xmin + (h * i), ymin + (h * j), zmin + (h * k))
                dyy += 16.0 * fVal(xmin + (h * i), ymin + (h * (j - 1)), zmin + (h * k))
                dyy += -fVal(xmin + (h * i), ymin + (h * (j - 2)), zmin + (h * k))

                dzz = -fVal(xmin + (h * i), ymin + (h * j), zmin + (h * (k + 2)))
                dzz += 16.0 * fVal(xmin + (h * i), ymin + (h * j), zmin + (h * (k + 1)))
                dzz += -30.0 * fVal(xmin + (h * i), ymin + (h * j), zmin + (h * k))
                dzz += 16.0 * fVal(xmin + (h * i), ymin + (h * j), zmin + (h * (k - 1)))
                dzz += -fVal(xmin + (h * i), ymin + (h * j), zmin + (h * (k - 2)))

                pointValue = (dxx + dyy + dzz) / (12.0 * h * h)
                dval = {'x': xmin + (h * i), 'y': ymin + (h * j), 'z': zmin + (h * k), 'fvalue': pointValue}

                datadf = datadf.append(dval, ignore_index=True)
        # print('calc x = %s' %(h * i))
    # print(outfile)
    # print(datadf)
    datadf.to_csv(outfile, sep='\t', index=False)

    # Calculate the L2 norm
    # l2val = {'dx': h, 'l2': np.linalg.norm(datadf['fvalue'])}

    # Avoid the
    # tmpdf = datadf[(datadf.x > 3.5) | (datadf.x < 2.5)]

    # l2val = {'dx': h, 'l2': np.mean(tmpdf['fvalue'])}
    # l2val = {'dx': h, 'l2': np.linalg.norm(tmpdf['fvalue'])}
    # dfl2 = dfl2.append(l2val, ignore_index=True)

    # print(datadf)
    # print('X = %s' % (nx))

def main():
    global df
    global dfl2
    global inputFiles
    VERSION = '1.0'
    USAGE = '%prog [-h | --help] [--version] [-i | --inputfile] [-o | --outputfile]'
    parser = optparse.OptionParser(usage=USAGE, version=VERSION)

    # parser.add_option(
    #     '-i',
    #     '--inputfile',
    #     help='input file name',
    # )


    # parser.add_option(
    #     '-o',
    #     '--outputfile',
    #     help='output file name',
    # )

    # (options, args) = parser.parse_args()

    # if (options.inputfile is None) or (not os.path.exists(options.inputfile)):
    #     parser.error("Please enter a data inputfile name with -i option")

    # if (options.outputfile is None):
    #     outfile = 'outtmpdata.csv'
    #     print('Output file name is not given, and will be use the default outputfile \"outtmpdata.csv\"')
    # else:
    #     outfile = options.outputfile

    dfl2 = pd.DataFrame()
    for key in inputFiles:
        print('Working on %s' %(inputFiles[key]['file']))
        df = pd.DataFrame()
        datafile = os.path.join(os.getcwd(), inputFiles[key]['file'])
        df = pd.read_table(datafile, sep='\=', engine='python', comment='#', names=['variable', 'value'])
        calOtherVariables()
        # solveLaplaceEq(inputFiles[key]['outfile'])


    # print(dfl2)
    # dfl2.to_csv('l2Norms.csv', sep='\t', index=False)
    print('done')


if __name__ == "__main__":
    main()




