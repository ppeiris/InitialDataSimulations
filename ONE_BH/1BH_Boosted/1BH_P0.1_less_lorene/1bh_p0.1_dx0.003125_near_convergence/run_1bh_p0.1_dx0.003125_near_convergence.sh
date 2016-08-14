#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 1bh_p0.1_dx0.003125_near_convergence" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.003125_near_convergence_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_1bh_p0.1_dx0.003125_near_convergence_8x9x13.par > $SIM_PATH/manybhnear_1bh_p0.1_dx0.003125_near_convergence_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.003125_near_convergence_8x9x13 end at "`date -u` >> SimulationStatus.out

# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.003125_near_convergence_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_1bh_p0.1_dx0.003125_near_convergence_8x9x13.par > $SIM_PATH/manybhmid_1bh_p0.1_dx0.003125_near_convergence_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.003125_near_convergence_8x9x13 end at "`date -u` >> SimulationStatus.out

# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.003125_near_convergence_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_1bh_p0.1_dx0.003125_near_convergence_8x9x13.par > $SIM_PATH/manybhfar_1bh_p0.1_dx0.003125_near_convergence_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.003125_near_convergence_8x9x13 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out
