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

inidf = pd.DataFrame()



# Near Region Parameters
xmin_near_shift = 0.0625
xmax_near_shift = 0.0625
ymin_near_shift = 0.4375
ymax_near_shift = 0.5625
zmin_near_shift = 0.4375
zmax_near_shift = 0.5625

# Mid Reagion Parameters
xmin_mid_shift = 1.0
xmax_mid_shift = 1.0
ymin_mid_shift = 0.0125
ymax_mid_shift = 0.0125
zmin_mid_shift = 0.0125
zmax_mid_shift = 0.0125

# Far Reagion Paramters
xmin_far_shift = 1.9375
xmax_far_shift = 2.0625
ymin_far_shift = 4.9375
ymax_far_shift = 5.0625
zmin_far_shift = 4.9375
zmax_far_shift = 5.0625


griddata_far = {
    'type': 'Byrange',
    'domain': 'full',
    'dxyz': 0.003125,
    'xmin': 4.9375,
    'ymin': 4.9375,
    'zmin': 4.9375,
    'xmax': 5.0625,
    'ymax': 5.0625,
    'zmax': 5.0625,
    'global_nx': 41,
    'global_ny': 41,
    'global_nz': 41,
    'out1D_xline_y': 5.0,
    'out1D_xline_z': 5.0,
    'out1D_yline_x': 5.0,
    'out1D_yline_z': 5.0,
    'out1D_zline_x': 5.0,
    'out1D_zline_y': 5.0,
}

griddata_mid = {
    'type': 'Byrange',
    'domain': 'full',
    'dxyz': 0.003125,
    'ymin': -0.0125,
    'zmin': -0.0125,
    'xmax': 2.0,
    'ymax': 0.0125,
    'zmax': 0.0125,
    'global_nx': 1281,
    'global_ny': 9,
    'global_nz': 9,
    'out1D_xline_y': 0.0,
    'out1D_xline_z': 0.0,
    'out1D_yline_x': 0.0,
    'out1D_yline_z': 0.0,
    'out1D_zline_x': 0.0,
    'out1D_zline_y': 0.0,
}

griddata_near = {
    'type': 'Byrange',
    'domain': 'full',
    'dxyz': 0.003125,
    'xmin': 2.9375,
    'ymin': 0.4375,
    'zmin': 0.4375,
    'xmax': 3.0625,
    'ymax': 0.5625,
    'zmax': 0.5625,
    'global_nx': 41,
    'global_ny': 41,
    'global_nz': 41,
    'out1D_xline_y': 0.5,
    'out1D_xline_z': 0.5,
    'out1D_yline_x': 3.0,
    'out1D_yline_z': 0.5,
    'out1D_zline_x': 3.0,
    'out1D_zline_y': 0.5,
}

# Load the data file in to dataframe
data = pd.read_table(datafile, sep='\=', engine='python', comment='#', index_col='var')
data = data.transpose()

print(data)
print(data['xmax_mid']['val'])
