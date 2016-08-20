#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 2bh_m1m2_0.47656_py" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out

# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_py_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_py_16x17x25.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_py_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_py_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_py_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_py_24x25x33.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_py_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_py_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_py_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_py_32x33x41.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_py_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_py_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_py_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_py_40x41x49.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_py_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_py_40x41x49 end at "`date -u` >> SimulationStatus.out


# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py_16x17x25.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py_24x25x33.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py_32x33x41.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py_40x41x49.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_py_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_py_40x41x49 end at "`date -u` >> SimulationStatus.out


# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_py_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_py_16x17x25.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_py_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_py_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_py_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_py_24x25x33.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_py_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_py_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_py_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_py_32x33x41.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_py_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_py_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_py_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_py_40x41x49.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_py_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_py_40x41x49 end at "`date -u` >> SimulationStatus.out

echo "Simulations start"

# Twopunch near simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_20.par > $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_20.out
END=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_30.par > $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_30.out
END=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_40.par > $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_40.out
END=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_40 end at "`date -u` >> SimulationStatus.out

# Twopunch mid simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_20.par > $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_20.out
END=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_30.par > $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_30.out
END=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_40.par > $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_40.out
END=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_40 end at "`date -u` >> SimulationStatus.out

# Twopunch far simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_20.par > $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_20.out
END=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_30.par > $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_30.out
END=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_40.par > $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_40.out
END=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_40 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out
