#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation mysimname" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# Twopunch near simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunnear_mysimname_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/twopunnear_mysimname_50.par > $SIM_PATH/twopunnear_mysimname_50.out
END=$(date +%s)
echo "Simulation twopunnear_mysimname_50 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $(($END-$START)) "seconds" >> SimulationStatus.out

# Twopunch mid simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunmid_mysimname_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/twopunmid_mysimname_50.par > $SIM_PATH/twopunmid_mysimname_50.out
END=$(date +%s)
echo "Simulation twopunmid_mysimname_50 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $(($END-$START)) "seconds" >> SimulationStatus.out

# Twopunch far simulations
# =====================================
START=$(date +%s)
echo "Simulation twopunfar_mysimname_50 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/twopunfar_mysimname_50.par > $SIM_PATH/twopunfar_mysimname_50.out
END=$(date +%s)
echo "Simulation twopunfar_mysimname_50 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $(($END-$START)) "seconds" >> SimulationStatus.out

