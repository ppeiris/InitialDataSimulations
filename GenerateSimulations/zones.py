import numpy as np




#dx=0.003125

#xmin=2.9375
#xmax=3.0625

#ymin=0.4375
#ymax=0.5625

#zmin=0.4375
#zmax=0.5625


dx=0.000390625
xmin =2.9375
ymin =0.4375
zmin =0.4375
xmax =3.0625
ymax =0.5625
zmax =0.5625



nx=(xmax-xmin)/dx
ny=(ymax-ymin)/dx
nz=(zmax-zmin)/dx


lenx=xmax-xmin
leny=ymax-ymin
lenz=zmax-zmin


print 'nx = ', nx
print 'ny = ', ny
print 'nz = ', nz

print '----------------'

print 'lenx = ', lenx
print 'leny = ', leny
print 'lenz = ', lenz

print '----------------'

newdx=dx/2.0

reduce_lenx=lenx/4.0
reduce_leny=leny/4.0
reduce_lenz=lenz/4.0

new_xmin=xmin+reduce_lenx
new_xmax=xmax-reduce_lenx
newnx=(new_xmax-new_xmin)/newdx


new_ymin=ymin+reduce_leny
new_ymax=ymax-reduce_leny

new_zmin=zmin+reduce_lenz
new_zmax=zmax-reduce_lenz

new_lenx=(new_xmax-new_xmin)

print 'xmin, new_xmin ', xmin, new_xmin
print 'xmax, new_xmax ', xmax, new_xmax
print 'ymin, new_ymin ', ymin, new_ymin
print 'ymax, new_ymax ', ymax, new_ymax
print 'zmin, new_zmin ', zmin, new_zmin
print 'zmax, new_zmax ', zmax, new_zmax

print 'new dx ', newdx
print 'New mid point (x) ',xmin+(xmax-xmin)/2.0 , new_xmin+(new_xmax-new_xmin)/2.0 
print 'New mid point (y) ',ymin+(ymax-ymin)/2.0, new_ymin+(new_ymax-new_ymin)/2.0 
print 'New mid point (z) ',zmin+(zmax-zmin)/2.0, new_zmin+(new_zmax-new_zmin)/2.0 

#ny=(ymax-ymin)/dx
#nz=(zmax-zmin)/dx
 


