#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 1bh" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# Twopunch near simulations
# =====================================
# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_1bh_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_12x13x17.par > $SIM_PATH/manybhnear_1bh_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_16x17x25.par > $SIM_PATH/manybhnear_1bh_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_24x25x33.par > $SIM_PATH/manybhnear_1bh_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_32x33x41.par > $SIM_PATH/manybhnear_1bh_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_40x41x49.par > $SIM_PATH/manybhnear_1bh_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_40x41x49 end at "`date -u` >> SimulationStatus.out

# Twopunch mid simulations
# =====================================
# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_1bh_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_12x13x17.par > $SIM_PATH/manybhmid_1bh_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_16x17x25.par > $SIM_PATH/manybhmid_1bh_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_24x25x33.par > $SIM_PATH/manybhmid_1bh_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_32x33x41.par > $SIM_PATH/manybhmid_1bh_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_40x41x49.par > $SIM_PATH/manybhmid_1bh_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_40x41x49 end at "`date -u` >> SimulationStatus.out

# Twopunch far simulations
# =====================================
# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_1bh_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_12x13x17.par > $SIM_PATH/manybhfar_1bh_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_16x17x25.par > $SIM_PATH/manybhfar_1bh_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_24x25x33.par > $SIM_PATH/manybhfar_1bh_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_32x33x41.par > $SIM_PATH/manybhfar_1bh_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_40x41x49.par > $SIM_PATH/manybhfar_1bh_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_40x41x49 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out