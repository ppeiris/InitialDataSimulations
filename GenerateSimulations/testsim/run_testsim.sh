#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation testsim" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# Twopunch near simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunnear_testsim_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/twopunnear_testsim_50.par > $SIM_PATH/twopunnear_testsim_50.out
END=$(date +%s)
echo "Simulation twopunnear_testsim_50 end at "`date -u` >> SimulationStatus.out

# ManyBH near simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHnear_testsim_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_testsim_12x13x17.par > $SIM_PATH/manybhnear_testsim_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_testsim_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_testsim_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_testsim_16x17x25.par > $SIM_PATH/manybhnear_testsim_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHnear_testsim_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_testsim_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_testsim_24x25x33.par > $SIM_PATH/manybhnear_testsim_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHnear_testsim_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_testsim_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_testsim_32x33x41.par > $SIM_PATH/manybhnear_testsim_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHnear_testsim_32x33x41 end at "`date -u` >> SimulationStatus.out

# Twopunch mid simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunmid_testsim_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/twopunmid_testsim_50.par > $SIM_PATH/twopunmid_testsim_50.out
END=$(date +%s)
echo "Simulation twopunmid_testsim_50 end at "`date -u` >> SimulationStatus.out

# ManyBH mid simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHmid_testsim_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_testsim_12x13x17.par > $SIM_PATH/manybhmid_testsim_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHmid_testsim_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_testsim_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_testsim_16x17x25.par > $SIM_PATH/manybhmid_testsim_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHmid_testsim_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_testsim_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_testsim_24x25x33.par > $SIM_PATH/manybhmid_testsim_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHmid_testsim_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_testsim_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_testsim_32x33x41.par > $SIM_PATH/manybhmid_testsim_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHmid_testsim_32x33x41 end at "`date -u` >> SimulationStatus.out

# Twopunch far simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunfar_testsim_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/twopunfar_testsim_50.par > $SIM_PATH/twopunfar_testsim_50.out
END=$(date +%s)
echo "Simulation twopunfar_testsim_50 end at "`date -u` >> SimulationStatus.out

# ManyBH far simulation
# ==================================
START=$(date +%s)
echo "Simulation ManyBHfar_testsim_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_testsim_12x13x17.par > $SIM_PATH/manybhfar_testsim_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHfar_testsim_12x13x17 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_testsim_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_testsim_16x17x25.par > $SIM_PATH/manybhfar_testsim_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHfar_testsim_16x17x25 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_testsim_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_testsim_24x25x33.par > $SIM_PATH/manybhfar_testsim_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHfar_testsim_24x25x33 end at "`date -u` >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_testsim_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_testsim_32x33x41.par > $SIM_PATH/manybhfar_testsim_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHfar_testsim_32x33x41 end at "`date -u` >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out