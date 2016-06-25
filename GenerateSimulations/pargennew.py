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

print(data)

# print(udata)
# print(udata['xmax_mid']['val'])
