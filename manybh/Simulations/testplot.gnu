#plot "phi_BHPars_3d_n20_np12.dat" u 3:6, "many_phi_many_BHPars_3d_n20_np12.dat" u 3:6
#plot "phi_BHPars_3d_n25_np12.dat" u 3:1, "many_phi_many_BHPars_3d_n25_np12.dat" u 3:1

plot "all.txt" u 1:7,x

#plot "phi_BHPars_3d_n25_np12.dat" u (log10(abs($3))):(log10(abs($6))), "many_phi_many_BHPars_3d_n25_np12.dat" u (log10(abs($3))):(log10(abs($6)))



#plot "phi_BHPars_3d_n30_np12.dat" u 3:1, "many_phi_many_BHPars_3d_n30_np12.dat" u 3:1
