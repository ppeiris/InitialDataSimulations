#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 1bh_p0.75_dx0.003125_near_convergence" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# Twopunch near simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunnear_1bh_p0.75_dx0.003125_near_convergence_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_1bh_p0.75_dx0.003125_near_convergence_20.par > $SIM_PATH/twopunnear_1bh_p0.75_dx0.003125_near_convergence_20.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_p0.75_dx0.003125_near_convergence_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_1bh_p0.75_dx0.003125_near_convergence_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_1bh_p0.75_dx0.003125_near_convergence_30.par > $SIM_PATH/twopunnear_1bh_p0.75_dx0.003125_near_convergence_30.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_p0.75_dx0.003125_near_convergence_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_1bh_p0.75_dx0.003125_near_convergence_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_1bh_p0.75_dx0.003125_near_convergence_40.par > $SIM_PATH/twopunnear_1bh_p0.75_dx0.003125_near_convergence_40.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_p0.75_dx0.003125_near_convergence_40 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_1bh_p0.75_dx0.003125_near_convergence_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunnear_1bh_p0.75_dx0.003125_near_convergence_50.par > $SIM_PATH/twopunnear_1bh_p0.75_dx0.003125_near_convergence_50.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_p0.75_dx0.003125_near_convergence_50 end at "`date -u` >> SimulationStatus.out

# Twopunch mid simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunmid_1bh_p0.75_dx0.003125_near_convergence_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_1bh_p0.75_dx0.003125_near_convergence_20.par > $SIM_PATH/twopunmid_1bh_p0.75_dx0.003125_near_convergence_20.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_p0.75_dx0.003125_near_convergence_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_1bh_p0.75_dx0.003125_near_convergence_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_1bh_p0.75_dx0.003125_near_convergence_30.par > $SIM_PATH/twopunmid_1bh_p0.75_dx0.003125_near_convergence_30.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_p0.75_dx0.003125_near_convergence_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_1bh_p0.75_dx0.003125_near_convergence_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_1bh_p0.75_dx0.003125_near_convergence_40.par > $SIM_PATH/twopunmid_1bh_p0.75_dx0.003125_near_convergence_40.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_p0.75_dx0.003125_near_convergence_40 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_1bh_p0.75_dx0.003125_near_convergence_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunmid_1bh_p0.75_dx0.003125_near_convergence_50.par > $SIM_PATH/twopunmid_1bh_p0.75_dx0.003125_near_convergence_50.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_p0.75_dx0.003125_near_convergence_50 end at "`date -u` >> SimulationStatus.out

# Twopunch far simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunfar_1bh_p0.75_dx0.003125_near_convergence_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_1bh_p0.75_dx0.003125_near_convergence_20.par > $SIM_PATH/twopunfar_1bh_p0.75_dx0.003125_near_convergence_20.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_p0.75_dx0.003125_near_convergence_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_1bh_p0.75_dx0.003125_near_convergence_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_1bh_p0.75_dx0.003125_near_convergence_30.par > $SIM_PATH/twopunfar_1bh_p0.75_dx0.003125_near_convergence_30.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_p0.75_dx0.003125_near_convergence_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_1bh_p0.75_dx0.003125_near_convergence_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_1bh_p0.75_dx0.003125_near_convergence_40.par > $SIM_PATH/twopunfar_1bh_p0.75_dx0.003125_near_convergence_40.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_p0.75_dx0.003125_near_convergence_40 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_1bh_p0.75_dx0.003125_near_convergence_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ~/bbhcode $SIM_PATH/twopunfar_1bh_p0.75_dx0.003125_near_convergence_50.par > $SIM_PATH/twopunfar_1bh_p0.75_dx0.003125_near_convergence_50.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_p0.75_dx0.003125_near_convergence_50 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out