#/bin/sh
echo "Starting batch process np =12 ";

./bbh -b BHPars_3d_n20_np12 -g Grid_Input_20 -p GridPars_12
./manybh -b many_BHPars_3d_n20_np12 -g Grid_Input_20 -p GridPars_12

./bbh -b BHPars_3d_n25_np12 -g Grid_Input_25 -p GridPars_12
./manybh -b many_BHPars_3d_n25_np12 -g Grid_Input_25 -p GridPars_12

./bbh -b BHPars_3d_n30_np12 -g Grid_Input_30 -p GridPars_12
./manybh -b many_BHPars_3d_n30_np12 -g Grid_Input_30 -p GridPars_12

echo 'Done ======'
