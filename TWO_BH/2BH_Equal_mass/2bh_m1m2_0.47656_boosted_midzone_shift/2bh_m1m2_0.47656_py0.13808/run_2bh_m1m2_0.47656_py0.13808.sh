#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 2bh_m1m2_0.47656_py0.13808" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# ManyBH near simulation
# ==================================
# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py0.13808_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py0.13808_8x9x13.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py0.13808_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py0.13808_8x9x13 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py0.13808_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py0.13808_16x17x25.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py0.13808_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py0.13808_16x17x25 end at "`date -u` >> SimulationStatus.out

# ManyBH far simulation
# ==================================
echo "Done!" >> SimulationStatus.out
