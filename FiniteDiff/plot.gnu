set terminal postscript  col
#set out "black-hole_3_0.5_0.5.eps"
#set grid

#set title "Black Hole is at 3,0.5,0.5" 
#plot "0.0125.asc" u ($1):(log10(abs($2*8))) w l ls 1 title "dxyz=0.0125",\
#        +"3-0.5-0.5-0.00625.asc" u ($1):(log10(abs($2*8))) w l ls 2  title "dxyz=0.00625",\
#        +"3-0.5-0.5-0.003125.asc" u ($1):(log10(abs($2*8))) w l ls 3 title "dxyz=0.003125",\
#        +"8.asc" u ($1):(log10(abs($2*8))) w l ls 4 title "dxyz=0.001562"



        #+"3-0.5-0.5-0.00078125_5_6.asc" u ($1):(log10(abs($2*8))) w l ls 2 title "dxyz=0.00078125",\
        #+"3-0.5-0.5-0.00078125_2.8_3.2.asc" u ($1):(log10(abs($2*8))) w l ls 2 title "dxyz=0.00078125"
        #+"3-0.5-0.5-0.000390625.asc" u ($1):(log10(abs($2*8))) w l ls 3 title "dxyz=0.000390625"
        #+"3-0.5-0.5-0.000390625_2.8_3.2.asc" u ($1):(log10(abs($2*8))) w l ls 3 title "dxyz=0.000390625",\
        #+"3-0.5-0.5-0.00078125_2.8_3.2.asc" u ($1):(log10(abs($2*8))) w l ls 2 title "dxyz=0.00078125",\
        #+"3-0.5-0.5-0.001562_0_1.asc" u ($1):(log10(abs($2*8))) w l ls 1 title "dxyz=0.00001562",\
        #+"3-0.5-0.5-0.001562_2.8_3.2.asc" u ($1):(log10(abs($2*8))) w l ls 1 title "dxyz=0.00001562"
        
        

set out "black-hole_3_0_0.eps"
set title "Black Hole is at 3,0,0" 
plot "0.0125_1_300.asc" u ($1):(log10(abs($2*8))) w l  title "dxyz=0.0125",\
        +"0.0125_16_300.asc" u ($1):(log10(abs($2*8))) w l  title "dxyz=0.00078125",\
        +"0.0125_8_300.asc" u ($1):(log10(abs($2*8))) w l  title "dxyz=0.0015625",\
        +"0.0125_2_300.asc" u ($1):(log10(abs($2*8))) w d title "dxyz=0.00625",\
        +"0.0125_4_300.asc" u ($1):(log10(abs($2*8))) w l  title "dxyz=0.003125"


 
#set out "black-hole_3_0_0_center.eps"
#set title "Black Hole is at 3,0,0" 
#plot "0.0125_1_300_center.asc" u ($1):(log10(abs($2*8))) w l  title "dxyz=0.0125",\
#        +"0.0125_2_300_center.asc" u ($1):(log10(abs($2*8))) w d title "dxyz=0.00625",\
#        +"0.0125_4_300_center.asc" u ($1):(log10(abs($2*8))) w l  title "dxyz=0.003125",\
#        +"0.0125_8_300_center.asc" u ($1):(log10(abs($2*8))) w l  title "dxyz=0.0015625",\
#        +"0.0125_16_300_center.asc" u ($1):(log10(abs($2*8))) w l  title "dxyz=0.00078125",\
#        +"0.0125_32_300_center.asc" u ($1):(log10(abs($2*8))) w l  title "dxyz=0.00078125"
 



#plot "3-0-0-0.003125.asc" u ($1):(log10(abs($2))) w l title "dxyz=0.003125", "3-0-0-0.001562.asc" u ($1):(log10(abs($2))) w l title "dxyz=0.00001562", "3-0-0-0.000390625.asc" u ($1):(log10(abs($2))) w l title "dxyz=0.000390625", "3-0-0-0.00078125.asc" u ($1):(log10(abs($2))) w l title "dxyz=0.00078125" 
