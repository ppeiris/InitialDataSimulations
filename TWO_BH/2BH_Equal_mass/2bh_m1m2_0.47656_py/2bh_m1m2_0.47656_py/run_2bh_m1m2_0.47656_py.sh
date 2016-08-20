#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 2bh_m1m2_0.47656_py" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# Twopunch near simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_50.par > $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_50.out
END=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_50 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_60 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_60.par > $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_60.out
END=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_60 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_70 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_70.par > $SIM_PATH/twopunnear_2bh_m1m2_0.47656_py_70.out
END=$(date +%s)
echo "Simulation twopunnear_2bh_m1m2_0.47656_py_70 end at "`date -u` >> SimulationStatus.out

# Twopunch mid simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_50.par > $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_50.out
END=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_50 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_60 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_60.par > $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_60.out
END=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_60 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_70 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_70.par > $SIM_PATH/twopunmid_2bh_m1m2_0.47656_py_70.out
END=$(date +%s)
echo "Simulation twopunmid_2bh_m1m2_0.47656_py_70 end at "`date -u` >> SimulationStatus.out

# Twopunch far simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_50.par > $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_50.out
END=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_50 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_60 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_60.par > $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_60.out
END=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_60 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_70 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_70.par > $SIM_PATH/twopunfar_2bh_m1m2_0.47656_py_70.out
END=$(date +%s)
echo "Simulation twopunfar_2bh_m1m2_0.47656_py_70 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out