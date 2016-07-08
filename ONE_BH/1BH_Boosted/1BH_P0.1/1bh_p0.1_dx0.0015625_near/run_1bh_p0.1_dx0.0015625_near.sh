#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 1bh_p0.1_dx0.0015625_near" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# Twopunch near simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunnear_1bh_p0.1_dx0.0015625_near_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_1bh_p0.1_dx0.0015625_near_20.par > $SIM_PATH/twopunnear_1bh_p0.1_dx0.0015625_near_20.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_p0.1_dx0.0015625_near_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_1bh_p0.1_dx0.0015625_near_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_1bh_p0.1_dx0.0015625_near_30.par > $SIM_PATH/twopunnear_1bh_p0.1_dx0.0015625_near_30.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_p0.1_dx0.0015625_near_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_1bh_p0.1_dx0.0015625_near_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_1bh_p0.1_dx0.0015625_near_40.par > $SIM_PATH/twopunnear_1bh_p0.1_dx0.0015625_near_40.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_p0.1_dx0.0015625_near_40 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_1bh_p0.1_dx0.0015625_near_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_1bh_p0.1_dx0.0015625_near_50.par > $SIM_PATH/twopunnear_1bh_p0.1_dx0.0015625_near_50.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_p0.1_dx0.0015625_near_50 end at "`date -u` >> SimulationStatus.out

# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_12x13x17.par > $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_16x17x25.par > $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_24x25x33.par > $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_32x33x41.par > $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_40x41x49.par > $SIM_PATH/manybhnear_1bh_p0.1_dx0.0015625_near_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_p0.1_dx0.0015625_near_40x41x49 end at "`date -u` >> SimulationStatus.out

# Twopunch mid simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunmid_1bh_p0.1_dx0.0015625_near_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_1bh_p0.1_dx0.0015625_near_20.par > $SIM_PATH/twopunmid_1bh_p0.1_dx0.0015625_near_20.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_p0.1_dx0.0015625_near_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_1bh_p0.1_dx0.0015625_near_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_1bh_p0.1_dx0.0015625_near_30.par > $SIM_PATH/twopunmid_1bh_p0.1_dx0.0015625_near_30.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_p0.1_dx0.0015625_near_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_1bh_p0.1_dx0.0015625_near_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_1bh_p0.1_dx0.0015625_near_40.par > $SIM_PATH/twopunmid_1bh_p0.1_dx0.0015625_near_40.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_p0.1_dx0.0015625_near_40 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_1bh_p0.1_dx0.0015625_near_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_1bh_p0.1_dx0.0015625_near_50.par > $SIM_PATH/twopunmid_1bh_p0.1_dx0.0015625_near_50.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_p0.1_dx0.0015625_near_50 end at "`date -u` >> SimulationStatus.out

# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_12x13x17.par > $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_16x17x25.par > $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_24x25x33.par > $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_32x33x41.par > $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_40x41x49.par > $SIM_PATH/manybhmid_1bh_p0.1_dx0.0015625_near_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_p0.1_dx0.0015625_near_40x41x49 end at "`date -u` >> SimulationStatus.out

# Twopunch far simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunfar_1bh_p0.1_dx0.0015625_near_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_1bh_p0.1_dx0.0015625_near_20.par > $SIM_PATH/twopunfar_1bh_p0.1_dx0.0015625_near_20.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_p0.1_dx0.0015625_near_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_1bh_p0.1_dx0.0015625_near_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_1bh_p0.1_dx0.0015625_near_30.par > $SIM_PATH/twopunfar_1bh_p0.1_dx0.0015625_near_30.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_p0.1_dx0.0015625_near_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_1bh_p0.1_dx0.0015625_near_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_1bh_p0.1_dx0.0015625_near_40.par > $SIM_PATH/twopunfar_1bh_p0.1_dx0.0015625_near_40.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_p0.1_dx0.0015625_near_40 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_1bh_p0.1_dx0.0015625_near_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_1bh_p0.1_dx0.0015625_near_50.par > $SIM_PATH/twopunfar_1bh_p0.1_dx0.0015625_near_50.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_p0.1_dx0.0015625_near_50 end at "`date -u` >> SimulationStatus.out

# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_12x13x17.par > $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_16x17x25.par > $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_24x25x33.par > $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_32x33x41.par > $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_40x41x49.par > $SIM_PATH/manybhfar_1bh_p0.1_dx0.0015625_near_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_p0.1_dx0.0015625_near_40x41x49 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out