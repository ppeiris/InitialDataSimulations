import numpy as np
import csv
import pandas as pd
import os
import sys
import optparse
pd.options.display.float_format = '{:.10g}'.format
global df
def getVal(askv):
    global df
    value = df[df.variable == askv]['value']
    if askv != 'zone':
        return float(value)
    return str(value)

def calOtherVariables():
    global df

    # calculate ymin and ymax

    yzlen = 5.0 * getVal('dxyz')
    ymax = yzlen/2
    ymin = -ymax
    zmax = ymax
    zmin = -ymax

    nvar = {'variable': 'ymax', 'value': ymax}
    df = df.append(nvar, ignore_index=True)

    nvar = {'variable': 'ymin', 'value': ymin}
    df = df.append(nvar, ignore_index=True)

    nvar = {'variable': 'zmin', 'value': zmin}
    df = df.append(nvar, ignore_index=True)

    nvar = {'variable': 'zmax', 'value': zmax}
    df = df.append(nvar, ignore_index=True)

    nvar = {'variable': 'nx', 'value': np.abs((getVal('xmax') - getVal('xmin')))/getVal('dxyz')}
    df = df.append(nvar, ignore_index=True)
    nvar = {'variable': 'ny', 'value': np.abs((getVal('ymax') - getVal('ymin')))/getVal('dxyz')}
    df = df.append(nvar, ignore_index=True)
    nvar = {'variable': 'nz', 'value': np.abs((getVal('zmax') - getVal('zmin')))/getVal('dxyz')}
    df = df.append(nvar, ignore_index=True)

    print(df)


def fVal(x, y ,z):
    m = 1.0
    x = x - 3.0
    r = np.sqrt(x*x + y*y + z*z)
    return (1.0 + m/(2.0 * r))


def solveLaplaceEq(outfile):
    nx = int(getVal('nx'))
    ny = int(getVal('ny'))
    nz = int(getVal('nz'))

    xmin = getVal('xmin')
    ymin = getVal('ymin')
    zmin = getVal('zmin')
    h = getVal('dxyz')

    datadf = pd.DataFrame()
    for i in range(2, nx-2):
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
        print('calc x = %s' %(h * i))
    datadf.to_csv(outfile, sep='\t', index=False)

    print(datadf)


def main():
    global df
    VERSION = '1.0'
    USAGE = '%prog [-h | --help] [--version] [-i | --inputfile] [-o | --outputfile]'
    parser = optparse.OptionParser(usage=USAGE, version=VERSION)

    parser.add_option(
        '-i',
        '--inputfile',
        help='input file name',
    )


    parser.add_option(
        '-o',
        '--outputfile',
        help='output file name',
    )

    (options, args) = parser.parse_args()

    if (options.inputfile is None) or (not os.path.exists(options.inputfile)):
        parser.error("Please enter a data inputfile name with -i option")

    if (options.outputfile is None):
        outfile = 'outtmpdata.csv'
        print('Output file name is not given, and will be use the default outputfile \"outtmpdata.csv\"')
    else:
        outfile = options.outputfile


    datafile = os.path.join(os.getcwd(), options.inputfile)
    df = pd.read_table(datafile, sep='\=', engine='python', comment='#', names=['variable', 'value'])

    calOtherVariables()
    solveLaplaceEq(outfile)

if __name__ == "__main__":
    main()




