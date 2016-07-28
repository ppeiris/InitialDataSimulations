//standard
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string>

#include <cmath>
#include <iomanip>
#include <fstream>

#include "nbr_spx.h"
#include "tbl.h"
#include "mtbl.h"
#include "map.h"
#include "binaire.h"
#include "param.h"
#include "unites.h"
#include "cmp.h"
#include "tenseur.h"
#include "utilitaires.h"

#include "manyBHpunc.h"

Many_BH::Many_BH (int& n, Map_et** mparray, BHpunc** bhparray, double* xvec) {
  nbh = n;
  maparray=mparray;
  bhpuncarray=bhparray;
  xbhvec = xvec;
}

Many_BH::~Many_BH() {}

void Many_BH::calc_us() {
  
  int ibh,jbh;
  for(ibh=0; ibh<nbh; ibh++) {
    
    bhpuncarray[ibh]->set_u2().allocate_all();
    bhpuncarray[ibh]->set_u().allocate_all();
    
    bhpuncarray[ibh]->set_rhsval().allocate_all();
    
    bhpuncarray[ibh]->set_kxxp().allocate_all();
    bhpuncarray[ibh]->set_kxxs().allocate_all();
    bhpuncarray[ibh]->set_kxyp().allocate_all();
    bhpuncarray[ibh]->set_kxys().allocate_all();
    bhpuncarray[ibh]->set_kxzp().allocate_all();
    bhpuncarray[ibh]->set_kxzs().allocate_all();
    bhpuncarray[ibh]->set_kyyp().allocate_all();
    bhpuncarray[ibh]->set_kyys().allocate_all();
    bhpuncarray[ibh]->set_kyzp().allocate_all();
    bhpuncarray[ibh]->set_kyzs().allocate_all();
    bhpuncarray[ibh]->set_kzzp().allocate_all();
    bhpuncarray[ibh]->set_kzzs().allocate_all();
    
    Mtbl Xabs1 (maparray[ibh]->xa) ;
    Mtbl Yabs1 (maparray[ibh]->ya) ;
    Mtbl Zabs1 (maparray[ibh]->za) ;
    //   Mtbl Xabs2 (mp2.xa) ;
    //   Mtbl Yabs2 (mp2.ya) ;
    //   Mtbl Zabs2 (mp2.za) ;
    
    int nz1 = maparray[ibh]->get_mg()->get_nzone() ;
    for (int l=0 ; l<nz1 ; l++) {
      int np = maparray[ibh]->get_mg()->get_np(l) ;
      int nt = maparray[ibh]->get_mg()->get_nt(l) ;
      int nr = maparray[ibh]->get_mg()->get_nr(l) ;
      for (int k=0 ; k<np ; k++)
      for (int j=0 ; j<nt ; j++)
        for (int i=0 ; i<nr ; i++) {
	  if((l!=nz1-1) || (i!=nr-1)) {
	    double xx=Xabs1(l,k,j,i);
	    double yy=Yabs1(l,k,j,i);
	    double zz=Zabs1(l,k,j,i);

	    //self
 	    double u1val=bhpuncarray[ibh]->set_u1().set().set(l,k,j,i);
	    
	    //sum over others - need r2,t2,p2!!!
	    double u2val=0.;
	    for (jbh=0; jbh<nbh; jbh++) {
	      if(ibh!=jbh) {
		double xd=xx+xbhvec[3*ibh]-xbhvec[3*jbh];
		double yd=yy+xbhvec[3*ibh+1]-xbhvec[3*jbh+1];
		double zd=zz+xbhvec[3*ibh+2]-xbhvec[3*jbh+2];
		double r2,t2,p2;
		maparray[jbh]->convert_absolute(xd,yd,zd,r2,t2,p2) ;
		u2val+=bhpuncarray[jbh]->set_u1().set().val_point(r2,t2,p2);
	      }
	    }
	    bhpuncarray[ibh]->set_u2().set().set(l,k,j,i) = u2val;
	    bhpuncarray[ibh]->set_u().set().set(l,k,j,i) = 1.0+u1val+u2val;
	    
	    double alpval = bhpuncarray[ibh]->set_alpha().set().set(l,k,j,i);
	    double betval = bhpuncarray[ibh]->set_beta().set().set(l,k,j,i);
 	    bhpuncarray[ibh]->set_rhsval().set().set(l,k,j,i) = -1.0*betval*pow(1.0+alpval*(1.0+u1val+u2val),-7);

 	    //	    if(i==j&&j==k&&k==l)cout << u1val<<" "<<u2val<<endl;
 	  } else {
 	    bhpuncarray[ibh]->set_u2().set().set(l,k,j,i) = 0.;
 	    bhpuncarray[ibh]->set_u().set().set(l,k,j,i) = 1.;
 	  }
 	}	    
    }
  
    
    bhpuncarray[ibh]->set_u2().set_std_base();
    bhpuncarray[ibh]->set_u().set_std_base();
    
    bhpuncarray[ibh]->set_rhsval().set_std_base();
    
    
  }
}


void Many_BH::solve_config (double precis, int ite_max, 
			    double relax, int ite_poisson_max) {
  
  int ibh;
  int looping = 1 ;
  int count = 0 ;
  double err=0.;
  
  while (looping == 1) {
    err=0.;
    for(ibh=0; ibh<nbh; ibh++) {
      Cmp u1_old (bhpuncarray[ibh]->set_u1().set()) ;
      
      bhpuncarray[ibh]->solve_equation (relax, ite_poisson_max) ;
      
      double err1 = max(diffrelmax(u1_old,bhpuncarray[ibh]->set_u1().set())) ;
      err = max(err1,err);
    
    }  
    cout << "STEP " << count << " ; DIFF : " << err << endl ;
    
    count ++ ;
    if ((err < precis) || (count > ite_max))looping = -1 ;
    
    calc_us();
    
  }
}


void Many_BH::export_data(char *fname=NULL, char *fGridInput_name=NULL ) {

  int n,nx,ny,nz,ibh;
   double x0,y0,z0,dx;
   string ofile,fgridinput;  

        if(fname==NULL)
	{
		ofile="many_phi.dat";		
	}
	else
	{
		ofile="many_phi_";
		ofile+=fname;	
		ofile+=".dat";
	}


	if(fGridInput_name==NULL)
	{
		fgridinput="Grid_Input";	
	}
	else
	{
		fgridinput=fGridInput_name;
	}



cout<<"\n"<<ofile<<" : "<<fgridinput<<"\n";
                                             



  ifstream filein;
  //filein.open("Grid_Input");
  filein.open(fGridInput_name);
  if (!filein) {
    cerr << "Can't open "<<fGridInput_name<< endl;
    exit(1);
  }
  char buf[100],c;
  filein.get(buf,100,'='); filein.get(c); filein >> n;
  filein.get(buf,100,'='); filein.get(c); filein >> x0;
  filein.get(buf,100,'='); filein.get(c); filein >> y0;
  filein.get(buf,100,'='); filein.get(c); filein >> z0;
  filein.get(buf,100,'='); filein.get(c); filein >> dx;
  //  filein.get(buf,100,'='); filein.get(c); filein >> nx;
  //  filein.get(buf,100,'='); filein.get(c); filein >> ny;
  //  filein.get(buf,100,'='); filein.get(c); filein >> nz;
  //  filein.get(buf,100,'='); filein.get(c); filein >> dx;
  filein.close();
  
   nx=n;
   ny=n;
   nz=n;

   //  cout << "nx="<<nx <<" dx="<<dx<< endl;

  ofstream outfilephi;
  std::ostringstream filenamephi;
  filenamephi << ofile << ends;
  outfilephi.open(filenamephi.str().c_str(),ios::out | ios::ate);

  //  outfilephi << nx<<" "<<ny<<" "<<nz<<" "<<dx<<endl;

  for (int i=0; i<nx; i++) {
    double xx=dx*(i-nx/2.0+0.5)+x0;
    for (int j=0; j<ny; j++) {
      double yy=dx*(j-ny/2.0+0.5)+y0;
      for (int k=0; k<nz; k++) {
	double zz=dx*(k-nz/2.0+0.5)+z0;

	double r=sqrt(xx*xx+yy*yy+zz*zz);
 	double r1,p1,t1;

	double psisum=0.;
	double uptsum=0.;
	double rhssum=0.;

	for (ibh=0; ibh<nbh; ibh++) {
	  maparray[ibh]->convert_absolute(xx-xbhvec[3*ibh],yy-xbhvec[3*ibh+1],zz-xbhvec[3*ibh+2],r1,t1,p1) ;
	  uptsum += bhpuncarray[ibh]->set_u1().set().val_point(r1,t1,p1);

	  psisum += 0.5*(bhpuncarray[ibh]->mbh)/r1;

	  rhssum += bhpuncarray[ibh]->set_rhsval().set().val_point(r1,t1,p1);
	}

	double psiv=1.0+psisum+uptsum;

 	outfilephi << setw(22) << setiosflags(ios::fixed) << setprecision(19)<< psiv <<" "<<uptsum<<" "<<xx<<" "<<yy<<" "<<zz<<" "<<rhssum<<endl;
	
      }
    }
  }
 outfilephi.close();   
 cout<<"\nOutput data file ===> "<<ofile<<"\n"; 
}


//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////

BHpunc::BHpunc (Map_et & mpi) : 
  mp(mpi),u(mpi),u1(mpi),u2(mpi),alpha(mpi),beta(mpi),rhsval(mpi),
  kxxp(mpi),kxyp(mpi),kxzp(mpi),kyyp(mpi),kyzp(mpi),kzzp(mpi),
  kxxs(mpi),kxys(mpi),kxzs(mpi),kyys(mpi),kyzs(mpi),kzzs(mpi),
  so_jm1_u(mpi) {}

BHpunc::~BHpunc() {}

void BHpunc::solve_equation (double relax, int itemax) {
  so_jm1_u.allocate_all() ;
  so_jm1_u.set_etat_qcq() ;
  so_jm1_u.set().set_etat_zero() ;

  Cmp rhsterm
    (-1.0*beta()*pow((1.0+alpha()*u()),-7));
  rhsterm.std_base_scal();
  rhsterm.set_dzpuis(0);
  rhsterm.inc_dzpuis();
  rhsterm.inc_dzpuis();
  rhsterm.inc_dzpuis();

  for (int ii=0; ii<7; ii++) {
    cout << rhsterm.set(ii,ii,ii,ii)<<" "<<alpha.set().set(ii,ii,ii,ii)<<" "<<beta.set().set(ii,ii,ii,ii)<<" "<<u1.set().set(ii,ii,ii,ii)<<" "<<u.set().set(ii,ii,ii,ii)<<endl;
  }

// Parameters for the Poisson solver
  double precis_poisson = 1e-16 ;
  int niter;

  Param par_poisson ;
  par_poisson.add_int(itemax,  0) ;
  par_poisson.add_double(relax,  0) ;
  par_poisson.add_double(precis_poisson, 1) ;
  par_poisson.add_int_mod(niter, 0) ;
  par_poisson.add_cmp_mod(so_jm1_u.set()) ;
  
  rhsterm.poisson(par_poisson, u1.set()) ;

  Cmp rhscheck (u1().laplacien());

  cout <<"rhs:"<< rhscheck.set(1,1,1,1)<<" "<<rhsterm.set(1,1,1,1)<<" "<<alpha.set().set(1,1,1,1)<<" "<<beta.set().set(1,1,1,1)<<endl;
}
