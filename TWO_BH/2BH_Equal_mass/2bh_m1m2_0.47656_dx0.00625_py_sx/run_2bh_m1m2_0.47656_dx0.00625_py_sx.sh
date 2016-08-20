#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 2bh_m1m2_0.47656_dx0.00625_py_sx" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49.par > $SIM_PATH/manybhnear_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49 end at "`date -u` >> SimulationStatus.out

# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49.par > $SIM_PATH/manybhmid_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49 end at "`date -u` >> SimulationStatus.out

# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_8x9x13 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_32x33x41 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49.par > $SIM_PATH/manybhfar_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_m1m2_0.47656_dx0.00625_py_sx_40x41x49 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out