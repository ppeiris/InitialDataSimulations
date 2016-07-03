set terminal postscript  col
set out 'far_dif_rsurs.eps'
set grid

set title "rsurf 0.1"
plot "../2bh_noS_PinY/manybhfar_2bh_noS_PinY_32x33x41/admconstraints::hamiltonian.x.asc" u ($10):(log10(abs($13))) index 0 w lp  title "rsurf 0.1, precis e-9"
