#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 2bh_noS_PinY_TEST" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# Twopunch near simulations
# ==========================
START=$(date +%s)
echo "Simulation twopunnear_2bh_noS_PinY_TEST_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/twopunnear_2bh_noS_PinY_TEST_50.par > $SIM_PATH/twopunnear_2bh_noS_PinY_TEST_50.out
END=$(date +%s)
echo "Simulation twopunnear_2bh_noS_PinY_TEST_50 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $(($END-$START)) "seconds" >> SimulationStatus.out

# ManyBH near simulation
# ==========================
START=$(date +%s)
echo "Simulation ManyBHnear_2bh_noS_PinY_TEST_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_2bh_noS_PinY_TEST_12x13x17.par > $SIM_PATH/manybhnear_2bh_noS_PinY_TEST_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_noS_PinY_TEST_12x13x17 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_noS_PinY_TEST_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_2bh_noS_PinY_TEST_16x17x25.par > $SIM_PATH/manybhnear_2bh_noS_PinY_TEST_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_noS_PinY_TEST_16x17x25 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_noS_PinY_TEST_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_2bh_noS_PinY_TEST_24x25x33.par > $SIM_PATH/manybhnear_2bh_noS_PinY_TEST_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_noS_PinY_TEST_24x25x33 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHnear_2bh_noS_PinY_TEST_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_2bh_noS_PinY_TEST_32x33x41.par > $SIM_PATH/manybhnear_2bh_noS_PinY_TEST_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_noS_PinY_TEST_32x33x41 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

# Twopunch mid simulations
# ==========================
START=$(date +%s)
echo "Simulation twopunmid_2bh_noS_PinY_TEST_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/twopunmid_2bh_noS_PinY_TEST_50.par > $SIM_PATH/twopunmid_2bh_noS_PinY_TEST_50.out
END=$(date +%s)
echo "Simulation twopunmid_2bh_noS_PinY_TEST_50 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $(($END-$START)) "seconds" >> SimulationStatus.out

# ManyBH mid simulation
# ==========================
START=$(date +%s)
echo "Simulation ManyBHmid_2bh_noS_PinY_TEST_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_2bh_noS_PinY_TEST_12x13x17.par > $SIM_PATH/manybhmid_2bh_noS_PinY_TEST_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_noS_PinY_TEST_12x13x17 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_noS_PinY_TEST_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_2bh_noS_PinY_TEST_16x17x25.par > $SIM_PATH/manybhmid_2bh_noS_PinY_TEST_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_noS_PinY_TEST_16x17x25 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_noS_PinY_TEST_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_2bh_noS_PinY_TEST_24x25x33.par > $SIM_PATH/manybhmid_2bh_noS_PinY_TEST_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_noS_PinY_TEST_24x25x33 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHmid_2bh_noS_PinY_TEST_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_2bh_noS_PinY_TEST_32x33x41.par > $SIM_PATH/manybhmid_2bh_noS_PinY_TEST_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_noS_PinY_TEST_32x33x41 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

# Twopunch far simulations
# ==========================
START=$(date +%s)
echo "Simulation twopunfar_2bh_noS_PinY_TEST_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/twopunfar_2bh_noS_PinY_TEST_50.par > $SIM_PATH/twopunfar_2bh_noS_PinY_TEST_50.out
END=$(date +%s)
echo "Simulation twopunfar_2bh_noS_PinY_TEST_50 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $(($END-$START)) "seconds" >> SimulationStatus.out

# ManyBH far simulation
# ==========================
START=$(date +%s)
echo "Simulation ManyBHfar_2bh_noS_PinY_TEST_12x13x17 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_2bh_noS_PinY_TEST_12x13x17.par > $SIM_PATH/manybhfar_2bh_noS_PinY_TEST_12x13x17.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_noS_PinY_TEST_12x13x17 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_noS_PinY_TEST_16x17x25 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_2bh_noS_PinY_TEST_16x17x25.par > $SIM_PATH/manybhfar_2bh_noS_PinY_TEST_16x17x25.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_noS_PinY_TEST_16x17x25 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_noS_PinY_TEST_24x25x33 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_2bh_noS_PinY_TEST_24x25x33.par > $SIM_PATH/manybhfar_2bh_noS_PinY_TEST_24x25x33.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_noS_PinY_TEST_24x25x33 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

START=$(date +%s)
echo "Simulation ManyBHfar_2bh_noS_PinY_TEST_32x33x41 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_2bh_noS_PinY_TEST_32x33x41.par > $SIM_PATH/manybhfar_2bh_noS_PinY_TEST_32x33x41.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_noS_PinY_TEST_32x33x41 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out