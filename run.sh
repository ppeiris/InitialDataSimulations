cd '2bh_diffm_WithSpin_WithMomentum/'


echo 'start !'

nohup ./cactus_manybhexe manybhnear_2bh_unequalmass_q_1_to_8_bh1_Py0.054063_S0_m0.10174_bh2_Py-0.054063_Sx0.31957_Sy-0.55351_m0.55179_away0.5_40x41x49.par > manybhnear_2bh_unequalmass_q_1_to_8_bh1_Py0.054063_S0_m0.10174_bh2_Py-0.054063_Sx0.31957_Sy-0.55351_m0.55179_away0.5_40x41x49.out

echo 'manybh is done !'

nohup ./cactus_manybhexe twopunnear_2bh_unequalmass_q_1_to_8_bh1_Py0.054063_S0_m0.10174_bh2_Py-0.054063_Sx0.31957_Sy-0.55351_m0.55179_away_0.5_40x41x49.par > twopunnear_2bh_unequalmass_q_1_to_8_bh1_Py0.054063_S0_m0.10174_bh2_Py-0.054063_Sx0.31957_Sy-0.55351_m0.55179_away_0.5_40x41x49.out 

echo 'twopun is done !'
echo 'Done !'
