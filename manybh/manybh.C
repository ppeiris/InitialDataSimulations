// headers C++
#include <iostream>
#include <fstream>

// headers C
#include <stdlib.h>
#include <math.h>
#include <string.h>

// headers Lorene
#include "nbr_spx.h"
#include "tbl.h"
#include "mtbl.h"
#include "map.h"
#include "binaire.h"
#include "eos.h"
#include"graphique.h"
#include "utilitaires.h"
#include "unites.h"

// Header perso
#include "manyBHpunc.h"
int main(int argc, char *argv[]){


  // We use nz nested radial domains, each of the same size

   char *bhparfile="BHPars_3d";
   char *gridinputfile="Grid_Input";
   char *gridparfile="GridPars";      
  
    
   for(int argcount=0;argcount<(argc-1);argcount++)
   {
   	if(strcmp(argv[argcount],"-b")==0)
   	{
   		bhparfile=argv[argcount+1];
   	}
   	else if(strcmp(argv[argcount],"-g")==0)     
   	{
   		gridinputfile=argv[argcount+1];
   	}
   		else if(strcmp(argv[argcount],"-p")==0)     
   	{
   		gridparfile=argv[argcount+1];
   	}
   } 
   
     
          cout<<"\n"<<bhparfile<<" : "<<gridinputfile<<" : "<<gridparfile<<"\n";      
 	//exit(1);
 
 


  int i,j,k,l,ii,jj;
  double ij;
  ifstream infile;
   //infile.open("GridPars");
   infile.open(gridparfile);
  if (!infile) {
    cerr << "Can't open GridPars" << endl;
    cerr << "Can't open "<<gridparfile<< endl;

    exit(1);
  }

  char buf[100],c;
  int nz,np,nt,nr,ite_max,ite_poisson_max;
  double precis,relax;

  //Lorene domain size parameters
  infile.get(buf,100,'='); infile.get(c); infile >> nz;
  infile.get(buf,100,'='); infile.get(c); infile >> np;
  infile.get(buf,100,'='); infile.get(c); infile >> nt;
  infile.get(buf,100,'='); infile.get(c); infile >> nr;
  //Relaxation parameters
  infile.get(buf,100,'='); infile.get(c); infile >> precis;
  infile.get(buf,100,'='); infile.get(c); infile >> ite_max;
  infile.get(buf,100,'='); infile.get(c); infile >> relax;
  infile.get(buf,100,'='); infile.get(c); infile >> ite_poisson_max;

  // Parameters for the fields solvers :
  //  int nz = 10 ;   // Number of domains.
  //  int np = 12 ;  // Number of phi
  //  int nt = 13 ;  // Number of theta
  //  int nr = 17 ;  // Number of r

  // Standard parameters to control the solver loop
  //  double precis = 1e-10;
  //  int ite_max = 100 ;
  //  double relax = 0.2 ;
  //  int ite_poisson_max = 4 ;

  infile.close();

  cout<<"Lorene grids:"<<nz<<" "<<np<<" "<<nt<<" "<<nr<<endl;

  // Construction of the field :
  int typep = NONSYM ;

    double* phis = new double [np] ;
  for (k=0 ; k<np ; k++)
    phis[k] = M_PI*2.*k/np ;
  
  //Values set after symmetry check!
  double* thetas = new double [nt] ;
  int typet;
  
  double rsurf=0.5;
  // This sets up the radial extent of each domain, currently in a geometric progression
  // We begin at a radius of rsurf for the outer radius of the innermost spherical domain

  double* r_lim = new double[nz+1] ;
  r_lim[0] = 0 ;
  for (i=1 ; i<nz ; i++) {
    r_lim[i]=rsurf*pow(1.8,i-1);

    cout<<" rlim:"<<i<<" "<<r_lim[i];
    //r_lim[i]=rsurf*pow(2.0,i-1);
  }
  cout<<endl;

  // Our domains extend to compactified spatial infinity
  r_lim[nz]=__infinity;
  


  //--------------------BH Pars-------------------- 
  
  int nbh,i3;
  double mbhtot,sep0;
  double xcm[3],pcm[3];
      
  double *mbhvec=NULL;
  double *pbhvec=NULL;
  double *sbhvec=NULL;
  double *xbhvec=NULL;
  double *sepbh = NULL;

  ifstream bhfile;
  bhfile.open(bhparfile);
  //bhfile.open("BHPars_3d");
  if (bhfile) {
    
    bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> nbh;
    // We need to set up the read in vectors!
    mbhvec = new double[nbh];
    pbhvec = new double[3*nbh];
    sbhvec = new double[3*nbh];
    xbhvec = new double[3*nbh];
    sepbh = new double[nbh*nbh];

    double mtot=0.;
    for (i=0; i<3; i++) {
      xcm[i] = 0.;
      pcm[i] = 0.;
    }

    for (ii=0; ii<nbh; ii++) {
      i3 = 3*ii;
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> mbhvec[ii];

      // This is S/M_tot^2, allowed to differ for the two black holes
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> sbhvec[i3];
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> sbhvec[i3+1];
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> sbhvec[i3+2];
      
      // This is P/M_tot; 
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> pbhvec[i3];
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> pbhvec[i3+1];
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> pbhvec[i3+2];
    
      //This is \vec{x}
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> xbhvec[i3];
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> xbhvec[i3+1];
      bhfile.get(buf,100,'='); bhfile.get(c); bhfile >> xbhvec[i3+2];

      cout<<"BH #"<<ii<<" m:"<<mbhvec[ii]<<
	" s:"<<sbhvec[i3]<<" "<<sbhvec[i3+1]<<" "<<sbhvec[i3+2]<<" "<<
	" p:"<<pbhvec[i3]<<" "<<pbhvec[i3+1]<<" "<<pbhvec[i3+2]<<" "<<
	" x:"<<xbhvec[i3]<<" "<<xbhvec[i3+1]<<" "<<xbhvec[i3+2]<<endl;
      
      for (i=0; i<3; i++) {
	xcm[i] += xbhvec[i3+i]*mbhvec[ii];
	pcm[i] += pbhvec[i3+i]*mbhvec[ii];
      }
      mbhtot += mbhvec[ii];
    }

    for (i=0; i<3; i++) {
      xcm[i] /= mbhtot;
      pcm[i] /= mbhtot;
    }

    //    cout<<"Correcting COM by :"<<xcm[0]<<" "<<xcm[1]<<" "<<xcm[2]<<endl;
    //    cout<<"Correcting Cent Mom. by :"<<pcm[0]<<" "<<pcm[1]<<" "<<pcm[2]<<endl;
    
    //    for (ii=0; ii<nbh; ii++) {
    //      for (i=0; i<3; i++) {
    //      xbhvec[3*ii+i] -= xcm[i];
    //      pbhvec[3*ii+i] -= pcm[i];
    //    }
    //    }

    for (ii=0; ii<nbh; ii++) {
      for (i=0; i<nbh; i++) {
	sepbh[ii*nbh+i] = sqrt(pow(xbhvec[3*ii]-xbhvec[3*i],2.0)+
			       pow(xbhvec[3*ii+1]-xbhvec[3*i+1],2.0)+
			       pow(xbhvec[3*ii+2]-xbhvec[3*i+2],2.0));
      }
    }
    
    
  } else {
    cerr<<"Couldn't open any BH par files!"<<endl;
    exit(1);
  }
  bhfile.close();
  
  int symcheck=0;
  for (ii=0; ii<nbh; ii++) {
    if(pbhvec[3*ii+2]!=0||sbhvec[3*ii]!=0||sbhvec[3*ii+1]!=0)symcheck=1;
  }

  //Symmetry check!
  if(symcheck==0) {
    //We have vertical symmetry!
    // This is tuned to only cover the upper half plane, assuming vertical symmetry 
    cout<<"Vertical symmetry!"<<endl;
    for (j=0 ; j<nt ; j++)
      thetas[j] = M_PI/2.*j/(nt-1) ;
    typet = SYM ;
  } else {
    //No symmetry, grid covers all of space
    cout<<"No vertical symmetry!"<<endl;
    for (j=0 ; j<nt ; j++)
      thetas[j] = M_PI*j/(nt-1) ;
    typet = NONSYM ;
  }
  
  //  As a general rule, we don't want black holes in the outermost domain, nor anywhere near it!
  for(ii=0; ii<nbh; ii++) {
    for(i=0; i<nbh; i++) {
      if(i!=ii) {
	if(sepbh[ii*nbh+i] > r_lim[nz-1]) {
	  cout<<"Sep0 is too close to the outermost domain!!!"<<endl;
	  cout<<"sep0="<<sepbh[ii*nbh+i]<<" "<<ii<<" "<<i<<" and r_lim="<<r_lim[nz-1]<<endl;
	  exit(1);
	}
      }
    }
  }
  
  // This line just establishes a 3-d radial/angular grid with the parameters given above
  Mg3d grid3d(nz,nr,nt,np,typet,typep,true) ;

  //NEW PART!!!
  Map_et *maparray[nbh];
  BHpunc *bhpuncarray[nbh];
 
  //To assign an initial guess, we want to put in the form from Laguna
  //We do this by figuring out the coords of the relevant points and evaluating his terms there

  //The map is related to the 3-d grid, but sets up a structure with all of the NZ nested domains
  //We extend to spatial infinity by using a coordinate transformation in the outermost domain

  for (ii=0; ii<nbh; ii++) {
    maparray[ii] = new Map_et(grid3d,r_lim);
    maparray[ii]->set_rot_phi(0);
    bhpuncarray[ii] = new BHpunc(*maparray[ii]);
  }

  Many_BH manybh(nbh,maparray,bhpuncarray,xbhvec);

  int ibh,jbh;

  for (ibh=0; ibh<nbh; ibh++) {

    // Star n :
    //Mtbl Xabs1 (mp1.xa) ;
    Mtbl Xabs (maparray[ibh]->xa) ;
    Mtbl Yabs (maparray[ibh]->ya) ;
    Mtbl Zabs (maparray[ibh]->za) ;

//   // Alpha and beta are terms in the RHS of the equatin for psi taken from Brandt & Brugmann
    Tenseur alp1 (*maparray[ibh]) ;
    alp1.allocate_all() ;
    Tenseur bet1 (*maparray[ibh]) ;
    bet1.allocate_all() ;
    Tenseur uterm1 (*maparray[ibh]) ;
    uterm1.allocate_all() ;

    //   Tenseur alp2 (mp2) ;
    //   alp2.allocate_all() ;
    //   Tenseur bet2 (mp2) ;
    //   bet2.allocate_all() ;
    //   Tenseur uterm2 (mp2) ;
    //   uterm2.allocate_all() ;
    
    Tenseur kxxp1 (*maparray[ibh]) ;
    kxxp1.allocate_all() ;
    Tenseur kxyp1 (*maparray[ibh]) ;
    kxyp1.allocate_all() ;
    Tenseur kxzp1 (*maparray[ibh]) ;
    kxzp1.allocate_all() ;
    Tenseur kyyp1 (*maparray[ibh]) ;
    kyyp1.allocate_all() ;
    Tenseur kyzp1 (*maparray[ibh]) ;
    kyzp1.allocate_all() ;
    Tenseur kzzp1 (*maparray[ibh]) ;
    kzzp1.allocate_all() ;
    Tenseur kxxs1 (*maparray[ibh]) ;
    kxxs1.allocate_all() ;
    Tenseur kxys1 (*maparray[ibh]) ;
    kxys1.allocate_all() ;
    Tenseur kxzs1 (*maparray[ibh]) ;
    kxzs1.allocate_all() ;
    Tenseur kyys1 (*maparray[ibh]) ;
    kyys1.allocate_all() ;
    Tenseur kyzs1 (*maparray[ibh]) ;
    kyzs1.allocate_all() ;
    Tenseur kzzs1 (*maparray[ibh]) ;
    kzzs1.allocate_all() ;


    double kxxp1v,kxyp1v,kxzp1v,kyyp1v,kyzp1v,kzzp1v;
    double kxxs1v,kxys1v,kxzs1v,kyys1v,kyzs1v,kzzs1v;

    for (l=0 ; l<nz ; l++)
      for (k=0 ; k<np ; k++)
	for (j=0 ; j<nt ; j++)
	  for (i=0 ; i<nr ; i++) {


	    double rom1,rom2,distfact;

	    double alpvaldenom = 0.;

	    //Self term
	    double xx = Xabs(l,k,j,i) ;
	    double yy = Yabs(l,k,j,i) ;
	    double zz = Zabs(l,k,j,i) ;

	    // Solve for Kxx1 around star 1
	    double r1=pow(xx*xx+yy*yy+zz*zz,0.5);
	    double mbh1=mbhvec[ibh];
	    rom1=r1/mbh1;
	    if(r1!=0)alpvaldenom = 0.5*mbh1/r1;
  
	    double n1[3];
	    n1[0]=xx/r1;
	    n1[1]=yy/r1;
	    n1[2]=zz/r1;
	    double pn1=0.;
	    for (ii=0; ii<3; ii++)pn1+=pbhvec[3*ibh+ii]*n1[ii];

	    double k1[9];
	    
	    ij=0.;
	    for (ii=0; ii<3; ii++) {
	      for (jj=0; jj<3; jj++) {
		int ind=3*ii+jj;
		if(ii==jj){
		  ij=1.;
		} else {
		  ij=0.;
		}
		k1[ind]=1.5*(pbhvec[3*ibh+ii]*n1[jj]+pbhvec[3*ibh+jj]*n1[ii]-
			     (ij-n1[ii]*n1[jj])*pn1)/r1/r1;

		if(ind==0)kxxp1v = k1[ind];
		if(ind==1)kxyp1v = k1[ind];
		if(ind==2)kxzp1v = k1[ind];
		if(ind==4)kyyp1v = k1[ind];
		if(ind==5)kyzp1v = k1[ind];
		if(ind==8)kzzp1v = k1[ind];
		
		if(sbhvec[3*ibh]!=0.||sbhvec[3*ibh+1]!=0.||sbhvec[3*ibh+2]!=0.) {
		  int i1 = (ii==2) ? 0 : ii+1;
		  int i2 = (ii==0) ? 2 : ii-1;
		  int j1 = (jj==2) ? 0 : jj+1;
		  int j2 = (jj==0) ? 2 : jj-1;
		  k1[ind]+=3.0*((sbhvec[3*ibh+i1]*n1[i2]-sbhvec[3*ibh+i2]*n1[i1])*n1[jj]+
				(sbhvec[3*ibh+j1]*n1[j2]-sbhvec[3*ibh+j2]*n1[j1])*n1[ii])/pow(r1,3.0);
		}

		if(ind==0)kxxs1v = k1[ind]-kxxp1v;
		if(ind==1)kxys1v = k1[ind]-kxyp1v;
		if(ind==2)kxzs1v = k1[ind]-kxzp1v;
		if(ind==4)kyys1v = k1[ind]-kyyp1v;
		if(ind==5)kyzs1v = k1[ind]-kyzp1v;
		if(ind==8)kzzs1v = k1[ind]-kzzp1v;

	      }
	    }
	    
	    
	    // Take care of the cross terms too!

	    double k12[9];
	    for (ii=0; ii<9; ii++)k12[ii]=0.;
	    
	    for (jbh=0; jbh<nbh; jbh++) {
	      if(ibh!=jbh) {
		double x12[3];
		for (ii=0; ii<3; ii++)x12[ii]=xbhvec[3*ibh+ii]-xbhvec[3*jbh+ii];
		
		//solve for Kxx2 around star 1
		double r12=pow(pow(xx+x12[0],2.)+pow(yy+x12[1],2.)+pow(zz+x12[2],2.),0.5);

		if(r12!=0)alpvaldenom += 0.5*mbhvec[jbh]/r12;

		double n12[3];
		n12[0]=(xx+x12[0])/r12;
		n12[1]=(yy+x12[1])/r12;
		n12[2]=(zz+x12[2])/r12;
		double pn12=0.;
		for (ii=0; ii<3; ii++)pn12+=pbhvec[3*jbh+ii]*n12[ii];
		
		// 	  //	  cout<<"ijkl:"<<i<<" "<<j<<" "<<k<<" "<<l<<" "<<r1<<" "<<r12<<" "<<yy+x12[1]<<" "<<n1[0]<<" "<<n1[1]<<" "<<n1[2]<<" "<<pn1/mbh1/mbh1<<" "<<n12[0]<<" "<<n12[1]<<" "<<n12[2]<<" "<<pn12/mbh2/mbh2<<endl;
		
		ij=0.;
		for (ii=0; ii<3; ii++) {
		  for (jj=0; jj<3; jj++) {
		    int ind=3*ii+jj;
		    if(ii==jj){
		      ij=1.;
		    } else {
		      ij=0.;
		    }
		    double kp=1.5*(pbhvec[3*jbh+ii]*n12[jj]+pbhvec[3*jbh+jj]*n12[ii]-
				  (ij-n12[ii]*n12[jj])*pn12)/r12/r12;
		
		    double ks = 0.;
		    if(sbhvec[3*jbh]!=0.||sbhvec[3*jbh+1]!=0.||sbhvec[3*jbh+2]!=0.) {
		      int i1 = (ii==2) ? 0 : ii+1;
		      int i2 = (ii==0) ? 2 : ii-1;
		      int j1 = (jj==2) ? 0 : jj+1;
		      int j2 = (jj==0) ? 2 : jj-1;
		      ks=3.0*((sbhvec[3*jbh+i1]*n12[i2]-sbhvec[3*jbh+i2]*n12[i1])*n12[jj]+
				     (sbhvec[3*jbh+j1]*n12[j2]-sbhvec[3*jbh+j2]*n12[j1])*n12[ii])/pow(r12,3.0);
		      
		      
		      
		    }

		    rom2 = r12 / mbhvec[jbh];

		    distfact = 2.0*rom2*rom2/(rom1*rom1+rom2*rom2); 
		    
		    k12[ind] += distfact*(kp+ks);
		  }
		}
	      }
	    }
	  
 	  
	  
	    // This is where we give an initial guess u1, taken from Laguna
	    //We will calculate the u cross-terms accurately,
	    //since this needs to be done after each solver iteration

	    //Star 1	  
	    double rh1=r1/mbh1;
	    double pbh1sq=pow(pbhvec[3*ibh],2.)+pow(pbhvec[3*ibh+1],2.)+pow(pbhvec[3*ibh+2],2.)+1.0e-10;
	    double uf=pbh1sq/mbh1/mbh1/8.0/pow(1.0+2.0*rh1,5);
	    double u0=1.0+10.0*rh1+40.0*rh1*rh1+80.0*pow(rh1,3)+80.0*pow(rh1,4);
	    double p2,u2;
	    if(r1>0) {
	      p2=1.5*pn1*pn1/pbh1sq-0.5;
	      u2=p2/5.0/pow(rh1,3)*(42.0*rh1+378.0*rh1*rh1+1316.0*pow(rh1,3)+
 				     2156.0*pow(rh1,4)+1536.0*pow(rh1,5)+240.0*pow(rh1,6)-
 				     21.0*pow(1.0+2.0*rh1,5)*log(1.0+2.0*rh1));
	    } else {
	      p2=0.;
	      u2=0.;
	    }
	    double uval1=uf*(u0+u2);
	    
	    // 	  //	  cout<<"ijkl:"<<i<<" "<<j<<" "<<k<<" "<<l<<" "<<rh1<<" "<<uf<<" "<<u0<<" "<<u2<<" "<<p2<<" "<<uval1<<endl;
	    
	    
	    // Handle the star
	    double alpval1;
	    
	    double kk1=0.;
	    for (ii=0; ii<9; ii++) {
	      kk1+=k1[ii]*(k1[ii]+k12[ii]);
	    }	    
	  
	    alpval1=1.0/alpvaldenom;
	  
	    double alp17=pow(alpval1,7);
	    double betval1=0.125*alp17*kk1;
	  
	    if((l==nz-1) && (i==nr-1)){
	      alpval1=0.;
	      betval1=0.;
	      uval1=0.;
	    }
	    if(r1==0) {
	      alpval1=0.;
	      betval1=0.;
	      kk1=0.;
	    
	    }

	    // 	  //	  cout<<"ijkl:"<<i<<" "<<j<<" "<<k<<" "<<l<<" "<<kk1<<" "<<kk2<<" "<<alpval1<<" "<<alpval2<<" "<<betval1<<" "<<betval2<<" "<<uval1<<" "<<uval2<<endl;
	    
	    // 	  //	  if(i==j&&j==k&&k==l)cout <<i<<" "<<j<<" "<<k<<" "<<l<<" "<<xx <<" "<<yy<<" "<<zz<<" "<<alpval1<<" "<<betval1<<" "<<uval1<<" "<<alpval2<<" "<<betval2<<" "<<uval2<<" "<<kk1<<" "<<kk2<<" "<<kxx1<<" "<<kxx12<<" "<<px2<<" "<<nx12<<" "<<pn12<<" "<<rh12<<endl;
	    // 	  //	  if(i==j&&j==k&&k==l)cout <<i<<" "<<j<<" "<<k<<" "<<l<<" "<<xx <<" "<<yy-sep0/2.0<<" "<<zz<<" al:"<<alpval1<<" bet:"<<betval1<<" "<<uval1<<" kk:"<<kk1<<" "<<kxx1<<" "<<kxx12<<" "<<rh1*mbh1<<" "<<px1*mbh1*mbh1<<" "<<nx1<<" "<<pn1*mbh1*mbh1<<endl;
	    // 	  //	  if(i==j&&j==k&&k==l)cout <<xx <<" "<<yy-sep0/2.0<<" "<<zz<<" "<<alpval1<<" "<<1.0/rh1<<" "<<1.0/rh12<<" "<<mbh1<<" "<<r1<<" "<<r12<<" "<<xx<<" "<<y12<<" "<<zz<<" "<<yy<<" "<<sep0<<endl;
	    
	    // 	  //	  if(r1!=0 && ((l!=nz-1) || (i!=nr-1))) {
	    // 	    //	    fprintf(file1,"%.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g\n",xx,yy-sep0/2.0,zz,alpval1,betval1,kk1,kxx1,kxy1,kxz1,kyy1,kyz1,kzz1,kxx12,kxy12,kxz12,kyy12,kyz12,kzz12);
	    // 	  //    fprintf(file2,"%.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g %.16g\n",-1.0*xx,-1.0*yy-sep0/2.0,zz,alpval2,betval2,kk2,kxx2,kxy2,kxz2,kyy2,kyz2,kzz2,kxx21,kxy21,kxz21,kyy21,kyz21,kzz21);
	    // 	  //	  }
	    
	    alp1.set().set(l,k,j,i) = alpval1 ;

	    bet1.set().set(l,k,j,i) = betval1 ;
	    uterm1.set().set(l,k,j,i) = uval1 ;
	    
	    kxxp1.set().set(l,k,j,i) = kxxp1v;
	    kxyp1.set().set(l,k,j,i) = kxyp1v;
	    kxzp1.set().set(l,k,j,i) = kxzp1v;
	    kyyp1.set().set(l,k,j,i) = kyyp1v;
	    kyzp1.set().set(l,k,j,i) = kyzp1v;
	    kzzp1.set().set(l,k,j,i) = kzzp1v;
	    kxxs1.set().set(l,k,j,i) = kxxs1v;
	    kxys1.set().set(l,k,j,i) = kxys1v;
	    kxzs1.set().set(l,k,j,i) = kxzs1v;
	    kyys1.set().set(l,k,j,i) = kyys1v;
	    kyzs1.set().set(l,k,j,i) = kyzs1v;
	    kzzs1.set().set(l,k,j,i) = kzzs1v;
	    
	  }
    
    //   //  fclose(file1);
    //   //  fclose(file2);
    
    alp1.set_std_base() ;
    bet1.set_std_base() ;
    uterm1.set_std_base() ;
    
    kxxp1.set_std_base() ;
    kxyp1.set_std_base() ;
    kxzp1.set_std_base() ;
    kyyp1.set_std_base() ;
    kyzp1.set_std_base() ;
    kzzp1.set_std_base() ;
    kxxs1.set_std_base() ;
    kxys1.set_std_base() ;
    kxzs1.set_std_base() ;
    kyys1.set_std_base() ;
    kyzs1.set_std_base() ;
    kzzs1.set_std_base() ;
    
    manybh.set_bh(ibh)->set_alpha() = alp1;
    manybh.set_bh(ibh)->set_beta() = bet1;
    manybh.set_bh(ibh)->set_u1() = uterm1;
    
    manybh.set_bh(ibh)->set_kxxp() = kxxp1;
    manybh.set_bh(ibh)->set_kxyp() = kxyp1;
    manybh.set_bh(ibh)->set_kxzp() = kxzp1;
    manybh.set_bh(ibh)->set_kyyp() = kyyp1;
    manybh.set_bh(ibh)->set_kyzp() = kyzp1;
    manybh.set_bh(ibh)->set_kzzp() = kzzp1;
    manybh.set_bh(ibh)->set_kxxs() = kxxs1;
    manybh.set_bh(ibh)->set_kxys() = kxys1;
    manybh.set_bh(ibh)->set_kxzs() = kxzs1;
    manybh.set_bh(ibh)->set_kyys() = kyys1;
    manybh.set_bh(ibh)->set_kyzs() = kyzs1;
    manybh.set_bh(ibh)->set_kzzs() = kzzs1;
    
    manybh.set_bh(ibh)->mbh=mbhvec[ibh];
    
    for(ii=0; ii<3; ii++) {
      manybh.set_bh(ibh)->pbh[ii]=pbhvec[3*ibh+ii];
      manybh.set_bh(ibh)->sbh[ii]=sbhvec[3*ibh+ii];
    }
    
  }

  cout<<"About to calc us!"<<endl;

  manybh.calc_us();

  // Solve the fields

  manybh.solve_config(precis,ite_max,relax,ite_poisson_max) ;

  //manybh.export_data();
  manybh.export_data(bhparfile,gridinputfile);

    

}
