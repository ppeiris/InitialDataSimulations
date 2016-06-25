#!/bin/sh
export SIM_PATH=`pwd`
cd $SIM_PATH
echo "Simulation 2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49" > SimulationStatus.out 
echo "Simulation start at " `date -u` >> SimulationStatus.out


echo "Simulations start"
# ManyBH near simulation
# ==========================
START=$(date +%s)
echo "Simulation ManyBHnear_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhnear_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49.par > $SIM_PATH/manybhnear_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHnear_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

# ManyBH mid simulation
# ==========================
START=$(date +%s)
echo "Simulation ManyBHmid_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhmid_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49.par > $SIM_PATH/manybhmid_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHmid_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

# ManyBH far simulation
# ==========================
START=$(date +%s)
echo "Simulation ManyBHfar_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49 start at "`date -u` >> SimulationStatus.out
echo "Still working on ..." >> SimulationStatus.out
nohup ./manybhexe_puncpow $SIM_PATH/manybhfar_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49.par > $SIM_PATH/manybhfar_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49.out
END=$(date +%s)
echo "Simulation ManyBHfar_2bh_SinX_PinY_equalm_nz12_rsurf0.25_40x41x49_40x41x49 end at "`date -u` >> SimulationStatus.out
echo "Simulation took" $($END-$START) "seconds" >> SimulationStatus.out

echo "Done!" >> SimulationStatus.out