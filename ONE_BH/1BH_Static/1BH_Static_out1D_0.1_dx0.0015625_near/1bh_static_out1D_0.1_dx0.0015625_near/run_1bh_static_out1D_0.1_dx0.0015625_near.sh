#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 1bh_static_out1D_0.1_dx0.0015625_near" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# Twopunch near simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_10 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_10.par > $SIM_PATH/twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_10.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_10 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_20.par > $SIM_PATH/twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_20.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_30.par > $SIM_PATH/twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_30.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_40.par > $SIM_PATH/twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_40.out
END=$(date +%s)
echo "Simulation twopunnear_1bh_static_out1D_0.1_dx0.0015625_near_40 end at "`date -u` >> SimulationStatus.out

# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9.par > $SIM_PATH/manybhnear_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13.par > $SIM_PATH/manybhnear_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17.par > $SIM_PATH/manybhnear_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhnear_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25.par > $SIM_PATH/manybhnear_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHnear_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25 end at "`date -u` >> SimulationStatus.out

# Twopunch mid simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_10 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_10.par > $SIM_PATH/twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_10.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_10 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_20.par > $SIM_PATH/twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_20.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_30.par > $SIM_PATH/twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_30.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_40.par > $SIM_PATH/twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_40.out
END=$(date +%s)
echo "Simulation twopunmid_1bh_static_out1D_0.1_dx0.0015625_near_40 end at "`date -u` >> SimulationStatus.out

# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9.par > $SIM_PATH/manybhmid_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13.par > $SIM_PATH/manybhmid_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17.par > $SIM_PATH/manybhmid_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhmid_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25.par > $SIM_PATH/manybhmid_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHmid_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25 end at "`date -u` >> SimulationStatus.out

# Twopunch far simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_10 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_10.par > $SIM_PATH/twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_10.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_10 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_20 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_20.par > $SIM_PATH/twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_20.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_20 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_30 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_30.par > $SIM_PATH/twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_30.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_30 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_40 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_40.par > $SIM_PATH/twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_40.out
END=$(date +%s)
echo "Simulation twopunfar_1bh_static_out1D_0.1_dx0.0015625_near_40 end at "`date -u` >> SimulationStatus.out

# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9.par > $SIM_PATH/manybhfar_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_static_out1D_0.1_dx0.0015625_near_4x5x9 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13.par > $SIM_PATH/manybhfar_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_static_out1D_0.1_dx0.0015625_near_8x9x13 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17.par > $SIM_PATH/manybhfar_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_static_out1D_0.1_dx0.0015625_near_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./bbhcode $SIM_PATH/manybhfar_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25.par > $SIM_PATH/manybhfar_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHfar_1bh_static_out1D_0.1_dx0.0015625_near_16x17x25 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out