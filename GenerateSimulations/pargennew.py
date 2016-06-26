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
        print("Updating key %s" %(key))

        index = data[data.variables == key].index[0]

        data.set_value(index, col, val)
        data.set_value(index, 'update', 'updated')

    else:
        # print("Key is not in the list. Adding the key (%s) to the data " %(key))
        newrow = {'variables':np.NaN, 'global':np.NaN, 'near':np.NaN, 'mid':np.NaN, 'far':np.NaN, 'update':'new'}
        newrow['variables'] = key
        newrow[col] = val
        data = data.append(newrow, ignore_index=True)
    return data

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
    # parser.print_help()
    parser.error("Please enter a data file name with -f option")

datafile = os.path.join(os.getcwd(), options.file)

# Load the default values
data = pd.read_csv('initdata.csv', sep='\t', dtype=object)
# Load the data file in to dataframe
udata = pd.read_table(datafile, sep='\=', engine='python', comment='#', index_col='var')
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

print(data)
