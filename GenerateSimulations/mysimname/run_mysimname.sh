#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation mysimname" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_mysimname_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_mysimname_12x13x17.par > $SIM_PATH/manybhnear_mysimname_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_mysimname_12x13x17 end at "`date -u` >> SimulationStatus.out

# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_mysimname_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_mysimname_12x13x17.par > $SIM_PATH/manybhmid_mysimname_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHmid_mysimname_12x13x17 end at "`date -u` >> SimulationStatus.out

# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_mysimname_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_mysimname_12x13x17.par > $SIM_PATH/manybhfar_mysimname_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHfar_mysimname_12x13x17 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out
