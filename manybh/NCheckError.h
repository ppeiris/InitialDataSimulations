using namespace std;
class CheckError
{
	private:
		//Data from Grid_Input
		int n;
		long double x0,y0,z0;
		long double dx;
		//Structure to save values that read from the phi.dat file	
		struct psivalues
		{
			long double psi;
			long double xx,yy,zz;
			long double u;
			long double rhs_Lorene;
		};
		//Structure to save calculated laplace values.
		struct lappsi_values
		{
			
			 long double lappsi; //Laplace psi value
			 long double lapu; //Laplace u
			 long double xx,yy,zz; // psi position
			 long double psi; // psi value that read from phi.dat file
			 long double psiKK; // (1/8) * (psi^-7) * (K_ij) * (K^ij)
			 long double funval; // (laplace psi + psiKK) equation (24) on apper 0404056v2
			 long double rhs_Lorene;

			 
		};
		long double ulap;
		long double sbh1;
		long double sbh2;
		long double pbh;
		long double sep;
 
 		long double mbh1;
 		long double mbh2; 
		long double sbh1x; 
		long double sbh1y; 
		long double sbh1z; 
		long double sbh2x; 
		long double sbh2y; 
		long double sbh2z; 
		long double pbh1x; 
		long double pbh1y; 
		long double pbh1z; 
		long double pbh2x; 
		long double pbh2y; 
		long double pbh2z; 
		long double pos_x1; 
		long double pos_y1; 
		long double pos_z1; 
		long double pos_x2; 
		long double pos_y2; 
		long double pos_z2; 

	

 	public:	
		CheckError(); //Constructor 
		~CheckError();//Destructor
		void ReadData(int acount,char *varg[]);
		void Help();

		
};

CheckError::CheckError()
{

}

CheckError::~CheckError()
{

}
void CheckError::Help()
{	
    cout<<"\n How to run the error check code\n";
    cout <<"\n ./Ncheck -b BHPars_3d_Test -g Grid_Input -d  phi_BHPars_3d_NoSpin.dat -o error \n";
    cout<<"\n -d  phi_BHPars_3d_NoSpin.dat:   Data file from the manybh lorene code";
    cout<<"\n -o error data will save in this file \n";
    cout<<"\n\n";

}
void CheckError::ReadData(int acount,char *varg[])
{


	      //string bhparfile,datfile,outputfile;
	      char *gridfile="Grid_Input";
              char *bhparfile="BHPars_3d";
              char *datfile;
              char *outputfile="Numerical_error";
              int check=0;
	      
	       for(int c=0;c<(acount-1);c++)
	        {
	            cout<<acount<<" : "<<c<<" : "<<varg[c]<<"\n";
		   if(strcmp(varg[1],"-h")==0)
		   {
		  	this->Help();
		  	exit(1);
		   }
		    
                    if(strcmp(varg[c],"-b")==0)
		    {
		        bhparfile=varg[c+1];
		    }
                    else if(strcmp(varg[c],"-g")==0)
		    {
                       gridfile=varg[c+1];
		    }
		    else if(strcmp(varg[c],"-d")==0)
		    {
			datfile=varg[c+1];
			check=1;
		    }
		    else if(strcmp(varg[c],"-o")==0)
		    {
			outputfile=varg[c+1];
		    }
                }
		char tm[100];
		if(check==0)
		{
                  
                  strcpy(tm,"many_phi_");
                  strcat(tm,bhparfile);
                  strcat(tm,".dat");
		  datfile=tm;
                }

	
	    //  cout<<"\n"<<bhparfile<<" : "<<datfile<<" : "<<outputfile<<" : "<<gridfile<<"\n";

           //     exit(1);

	  	ifstream filein,filedata;
		filein.open(gridfile);

		if (!filein) 
		{
    			cerr << "Can't open "<<gridfile<< endl;
    			exit(1);
  		}
		else
		{
		    	cout<<"\n Grid input file open [ "<<gridfile<< " ]\n";
		}
  		
		char buf[1000],c;
  		filein.get(buf,100,'='); filein.get(c); filein >> n;
  		filein.get(buf,100,'='); filein.get(c); filein >> x0; 
  		filein.get(buf,100,'='); filein.get(c); filein >> y0; 
  		filein.get(buf,100,'='); filein.get(c); filein >> z0; 
  		filein.get(buf,100,'='); filein.get(c); filein >> dx; 
		filein.close();	

		
                long double *mbhvec=NULL;
                long double *pbhvec=NULL;
                long double *sbhvec=NULL;
                long double *xbhvec=NULL;
                long double *sepbh=NULL;
	         

		filein.open(bhparfile);
		if(!filein)
		{
			cerr << "Can't open BHPars file" << endl;
    			exit(1);
		}
                else
                {
                 	cout<<"\n BH Par file open [ "<<bhparfile<<" ] \n";
		}

		int nbh;
  		filein.get(buf,100,'='); filein.get(c); filein >> nbh;
                 cout<<"nbh = "<<nbh<<endl;
		mbhvec=new long double[nbh];
                sbhvec=new long double[3*nbh];
		pbhvec=new long double[3*nbh];
		xbhvec=new long double[3*nbh];
		sepbh=new long double[nbh+nbh];


                for(int i=0;i<nbh;i++)
		{
		    int i3=3*i;
  			filein.get(buf,100,'='); filein.get(c); filein >> mbhvec[i];


  			filein.get(buf,100,'='); filein.get(c); filein >> sbhvec[i3];
  			filein.get(buf,100,'='); filein.get(c); filein >> sbhvec[i3+1];
  			filein.get(buf,100,'='); filein.get(c); filein >> sbhvec[i3+2];

  			filein.get(buf,100,'='); filein.get(c); filein >> pbhvec[i3];
  			filein.get(buf,100,'='); filein.get(c); filein >> pbhvec[i3+1];
  			filein.get(buf,100,'='); filein.get(c); filein >> pbhvec[i3+2];

  			filein.get(buf,100,'='); filein.get(c); filein >> xbhvec[i3];
  			filein.get(buf,100,'='); filein.get(c); filein >> xbhvec[i3+1];
  			filein.get(buf,100,'='); filein.get(c); filein >> xbhvec[i3+2];

                    	
                          cout<<"BH #"<<i<<" m:"<<mbhvec[i]<<
     			   " s:"<<sbhvec[i3]<<" "<<sbhvec[i3+1]<<" "<<sbhvec[i3+2]<<" "<<
     			   " p:"<<pbhvec[i3]<<" "<<pbhvec[i3+1]<<" "<<pbhvec[i3+2]<<" "<<
    			    " x:"<<xbhvec[i3]<<" "<<xbhvec[i3+1]<<" "<<xbhvec[i3+2]<<endl;   
		}

                 psivalues* psiarray = new psivalues[n*n*n];
    		filedata.open(datfile);

		if (!filedata) 
		{
    			cerr << "\nCan't open phi.dat" << endl;
    			exit(1);
  		}
                else
		{
                 	cout<<"\n Data file is open [ "<<filedata<<" ] \n";
		}




		long double sum_lapu_psiKK,sum_lapu_psikk_tmp;
		sum_lapu_psiKK=0;
		sum_lapu_psikk_tmp=0;

  		int i,j,k;
		long double psi1,u,x,y,z;
		i=0;
		int count=0;
		                


                //Read all the values from phi.dat file and put in to 3D array.
		for(int i=0;i<n;i++) //go through x axis of 3D array.
		{
		 // cout<<"i:"<<i<<endl;
			for(int j=0;j<n;j++) //go through y axis of 3D  array
			{
				
				for(int k=0;k<n;k++)//go through z axis of 3D array
				{

				  int indx=i*n*n+j*n+k;
				  filedata >>psiarray[indx].psi;
				  filedata >>psiarray[indx].u;
				  filedata >>psiarray[indx].xx;
				  filedata >>psiarray[indx].yy;
				  filedata >>psiarray[indx].zz;
				  filedata >>psiarray[indx].rhs_Lorene;
				  count++;
				  
				}
			}
		}	
  		filedata.close();	

		cout<<"Done reading, n="<<n<<endl;
		

		//-----------------------------------------------------------
		lappsi_values* lappsiarray = new lappsi_values[n*n*n];	
		//		lappsi_values lappsiarray[n-2][n-2][n-2];	

		cout<<"Done lappsi"<<endl;
		long double lap;
		lap=0;  

                for(i=1;i<(n-1);i++) //i,j,k start from 1 and to to n-1 to avoid boundaries
		{

			for(j=1;j<(n-1);j++)
			{
				for(k=1;k<(n-1);k++)
				{
				  int indx=i*n*n+j*n+k;
				  int di=n*n;
				  int dj=n;
				  int dk=1;
					lap=(psiarray[indx+di].psi+psiarray[indx-di].psi+psiarray[indx+dj].psi+psiarray[indx-dj].psi+psiarray[indx+dk].psi+psiarray[indx-dk].psi-(6*psiarray[indx].psi));
					ulap=(psiarray[indx+di].u+psiarray[indx-di].u+psiarray[indx+dj].u+psiarray[indx-dj].u+psiarray[indx+dk].u+psiarray[indx-dk].u-(6*psiarray[indx].u));
					//cout <<"\n============"<<"\nlap ="<<lap<<"\n===============\n";

					
					lappsiarray[indx].lappsi=lap/(dx*dx);
					lappsiarray[indx].lapu=ulap/(dx*dx);
					lappsiarray[indx].xx=psiarray[indx].xx;
					lappsiarray[indx].yy=psiarray[indx].yy;
					lappsiarray[indx].zz=psiarray[indx].zz;
					lappsiarray[indx].psi=psiarray[indx].psi;
					lappsiarray[indx].rhs_Lorene=psiarray[indx].rhs_Lorene;
				}
			}

		}	
		

	        for (int ii=0; ii<nbh; ii++) {
      			for (i=0; i<nbh; i++) {
				sepbh[ii*nbh+i] = sqrt(pow(xbhvec[3*ii]-xbhvec[3*i],2.0)+
			       				pow(xbhvec[3*ii+1]-xbhvec[3*i+1],2.0)+
			       				pow(xbhvec[3*ii+2]-xbhvec[3*i+2],2.0));
      			}
    		}

		long double KK_tmp;
		long double Kab_ps1;
		long double Kab_ps2;
		long double Kab;
		long double Kab_p1,Kab_s1,Kab_p2,Kab_s2;
		long double tmp1,tmp2,tmp3,tmp4,tmp5;
		long double S1xn[3];
		long double S2xn[3];

                string datafile;
		ofstream outfilephi,fNerror;
     		std::ostringstream filenamephi;
     		std::ostringstream fileerror;  
                datafile="phi_check_";
		datafile+=bhparfile;
		datafile+=".dat";
       		filenamephi <<datafile << ends;
		outfilephi.open(filenamephi.str().c_str(),ios::out | ios::ate);

		for(int i=1;i<(n-1);i++) 
		{
			for(int j=1;j<(n-1);j++)
			{
				for(int k=1;k<(n-1);k++)
				{
                                  int indx=i*n*n+j*n+k;
				  int total_interations=(n-2)*n*n+(n-2)*n+(n-2);  
				  long double k_ps=0.0;
				  long double KK=0.0;
                                  long double *r_magvec=NULL;  
				  long double *unitvec=NULL;
				  long double *Sxn=NULL;
				  long double *pdotn=NULL;
 				  r_magvec=new long double[nbh]; 
 				  unitvec=new long double[3*nbh]; 
				  Sxn=new long double[3*nbh];
                                  pdotn=new long double[nbh];
	
				  for(int ibh=0;ibh<nbh;ibh++)
				  {
                                      r_magvec[ibh]=pow(pow(lappsiarray[indx].xx-xbhvec[3*ibh],2)+pow(lappsiarray[indx].yy-xbhvec[3*ibh+1],2)+pow(lappsiarray[indx].zz-xbhvec[3*ibh+2],2),0.5);
 				      unitvec[3*ibh]=(lappsiarray[indx].xx-xbhvec[3*ibh])/r_magvec[ibh];
				      unitvec[3*ibh+1]=(lappsiarray[indx].yy-xbhvec[3*ibh+1])/r_magvec[ibh];
				      unitvec[3*ibh+2]=(lappsiarray[indx].zz-xbhvec[3*ibh+2])/r_magvec[ibh];
				      pdotn[ibh]=pbhvec[3*ibh]*unitvec[3*ibh]+pbhvec[3*ibh+1]*unitvec[3*ibh+1]+pbhvec[3*ibh+2]*unitvec[3*ibh+2];
				  }

				    for(int ii=0;ii<3;ii++)
				    {
					 for(int jj=0;jj<3;jj++)
					 {
					     int ind=3*ii+jj;
					     int gamma;
				  	     long double k_ab=0.0;
					     if(ii==jj)
					     {
						gamma=1.0;
					     }
					     else
					     {
						gamma=0.0;
					     }
						 for(int ibh=0;ibh<nbh;ibh++)
						 {
						    long double k_p=0.0;
						    long double k_s=0.0;
					     	    k_p=1.5*(pbhvec[3*ibh+ii]*unitvec[3*ibh+jj]+pbhvec[3*ibh+jj]*unitvec[3*ibh+ii]-(gamma-(unitvec[3*ibh+ii]*unitvec[3*ibh+jj]))*(pdotn[ibh]))/(pow(r_magvec[ibh],2));
					     	    k_s=(3.0/pow(r_magvec[ibh],3.0))*((Sxn[3*ibh+ii]*unitvec[3*ibh+jj])+(Sxn[3*ibh+jj]*unitvec[3*ibh+ii]));
					     	    k_ps=k_p+k_s;
                                                    k_ab+=k_ps;
					 	}
					
                                       
                                            KK=KK+(k_ab*k_ab);
				     }
				}
				lappsiarray[indx].psiKK=(0.125)*pow(lappsiarray[indx].psi,-7)*KK;	

				sum_lapu_psikk_tmp=sum_lapu_psikk_tmp+(pow((lappsiarray[indx].lapu+lappsiarray[indx].psiKK),2)/(pow(lappsiarray[indx].lapu,2)+pow(lappsiarray[indx].psiKK,2)));
				
				lappsiarray[indx].funval=lappsiarray[indx].lappsi+lappsiarray[indx].psiKK;

			        outfilephi << setw(22) << setiosflags(ios::fixed) << setprecision(19)<< lappsiarray[indx].lappsi <<" "<< lappsiarray[indx].lapu <<" "<<lappsiarray[indx].psiKK<<" "<<lappsiarray[indx].funval<<" "<<lappsiarray[indx].xx<<" "<<lappsiarray[indx].yy<<" "<<lappsiarray[indx].zz<<" "<<lappsiarray[indx].psi<<" "<<lappsiarray[indx].rhs_Lorene<<" "<<(lappsiarray[indx].rhs_Lorene-lappsiarray[indx].psiKK)<<endl;
				if((indx%100)==1)
				{
				        cout<<indx<<" of "<<total_interations<<", data file = "<<datfile<<"\n";
				}

			}
		}
	}
		sum_lapu_psiKK=sqrt((sum_lapu_psikk_tmp/pow((n-2),3)));
		fileerror<<outputfile<< ends;
		fNerror.open(fileerror.str().c_str(),ios::app | ios::ate);
		fNerror<<n<<" "<<dx<<" "<<(n-2)<<" "<<(pow(((n-2)/dx),3))<<" "<<sum_lapu_psiKK<<endl;
		fNerror.close();
		cout <<"Sum = "<<sum_lapu_psiKK<<"\n";
		outfilephi.close();
	        cout<<"\nError Data saved.\nData saved in ====>  "<<outputfile<<"\n\n"; 
}
