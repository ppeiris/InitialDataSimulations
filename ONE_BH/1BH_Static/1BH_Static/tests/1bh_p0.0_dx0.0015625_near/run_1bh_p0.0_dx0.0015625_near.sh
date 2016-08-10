#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 1bh_p0.0_dx0.0015625_near" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.0_dx0.0015625_near_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_p0.0_dx0.0015625_near_4x5x9.par > $SIM_PATH/manybhnear_1bh_p0.0_dx0.0015625_near_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.0_dx0.0015625_near_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.0_dx0.0015625_near_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_p0.0_dx0.0015625_near_12x13x17.par > $SIM_PATH/manybhnear_1bh_p0.0_dx0.0015625_near_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.0_dx0.0015625_near_12x13x17 end at "`date -u` >> SimulationStatus.out

# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.0_dx0.0015625_near_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_p0.0_dx0.0015625_near_4x5x9.par > $SIM_PATH/manybhmid_1bh_p0.0_dx0.0015625_near_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.0_dx0.0015625_near_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.0_dx0.0015625_near_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_p0.0_dx0.0015625_near_12x13x17.par > $SIM_PATH/manybhmid_1bh_p0.0_dx0.0015625_near_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.0_dx0.0015625_near_12x13x17 end at "`date -u` >> SimulationStatus.out

# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.0_dx0.0015625_near_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_p0.0_dx0.0015625_near_4x5x9.par > $SIM_PATH/manybhfar_1bh_p0.0_dx0.0015625_near_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.0_dx0.0015625_near_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.0_dx0.0015625_near_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_p0.0_dx0.0015625_near_12x13x17.par > $SIM_PATH/manybhfar_1bh_p0.0_dx0.0015625_near_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.0_dx0.0015625_near_12x13x17 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out