#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation One_BH" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# Twopunch near simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunnear_One_BH_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_One_BH_20.par > $SIM_PATH/twopunnear_One_BH_20.out
END=$(date +%s)
echo "Simulation twopunnear_One_BH_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_One_BH_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_One_BH_30.par > $SIM_PATH/twopunnear_One_BH_30.out
END=$(date +%s)
echo "Simulation twopunnear_One_BH_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_One_BH_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_One_BH_40.par > $SIM_PATH/twopunnear_One_BH_40.out
END=$(date +%s)
echo "Simulation twopunnear_One_BH_40 end at "`date -u` >> SimulationStatus.out

# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_One_BH_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_One_BH_12x13x17.par > $SIM_PATH/manybhnear_One_BH_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_One_BH_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_One_BH_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_One_BH_16x17x25.par > $SIM_PATH/manybhnear_One_BH_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHnear_One_BH_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_One_BH_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_One_BH_24x25x33.par > $SIM_PATH/manybhnear_One_BH_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHnear_One_BH_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_One_BH_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_One_BH_32x33x41.par > $SIM_PATH/manybhnear_One_BH_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHnear_One_BH_32x33x41 end at "`date -u` >> SimulationStatus.out

# Twopunch mid simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunmid_One_BH_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_One_BH_20.par > $SIM_PATH/twopunmid_One_BH_20.out
END=$(date +%s)
echo "Simulation twopunmid_One_BH_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_One_BH_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_One_BH_30.par > $SIM_PATH/twopunmid_One_BH_30.out
END=$(date +%s)
echo "Simulation twopunmid_One_BH_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_One_BH_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_One_BH_40.par > $SIM_PATH/twopunmid_One_BH_40.out
END=$(date +%s)
echo "Simulation twopunmid_One_BH_40 end at "`date -u` >> SimulationStatus.out

# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_One_BH_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_One_BH_12x13x17.par > $SIM_PATH/manybhmid_One_BH_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHmid_One_BH_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_One_BH_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_One_BH_16x17x25.par > $SIM_PATH/manybhmid_One_BH_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHmid_One_BH_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_One_BH_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_One_BH_24x25x33.par > $SIM_PATH/manybhmid_One_BH_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHmid_One_BH_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_One_BH_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_One_BH_32x33x41.par > $SIM_PATH/manybhmid_One_BH_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHmid_One_BH_32x33x41 end at "`date -u` >> SimulationStatus.out

# Twopunch far simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunfar_One_BH_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_One_BH_20.par > $SIM_PATH/twopunfar_One_BH_20.out
END=$(date +%s)
echo "Simulation twopunfar_One_BH_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_One_BH_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_One_BH_30.par > $SIM_PATH/twopunfar_One_BH_30.out
END=$(date +%s)
echo "Simulation twopunfar_One_BH_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_One_BH_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_One_BH_40.par > $SIM_PATH/twopunfar_One_BH_40.out
END=$(date +%s)
echo "Simulation twopunfar_One_BH_40 end at "`date -u` >> SimulationStatus.out

# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_One_BH_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_One_BH_12x13x17.par > $SIM_PATH/manybhfar_One_BH_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHfar_One_BH_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_One_BH_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_One_BH_16x17x25.par > $SIM_PATH/manybhfar_One_BH_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHfar_One_BH_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_One_BH_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_One_BH_24x25x33.par > $SIM_PATH/manybhfar_One_BH_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHfar_One_BH_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_One_BH_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_One_BH_32x33x41.par > $SIM_PATH/manybhfar_One_BH_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHfar_One_BH_32x33x41 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out