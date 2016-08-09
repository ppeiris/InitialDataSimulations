#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 1bh_static_test" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# ManyBH near simulation
# ==================================
START=$(date +%s)
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_test_2x3x5 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_test_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_static_test_4x5x9.par > $SIM_PATH/manybhnear_1bh_static_test_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_test_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_test_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_static_test_12x13x17.par > $SIM_PATH/manybhnear_1bh_static_test_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_test_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_test_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_static_test_16x17x25.par > $SIM_PATH/manybhnear_1bh_static_test_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_test_16x17x25 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out
