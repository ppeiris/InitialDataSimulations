#include <stdlib.h>
#include <math.h>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cmath>
using namespace std;
//Return the function value at x
//

double funval(double x,double y, double z)
{
    // f = (1+m/2r)
    double m=1;
    x=x-3.0;
    //y=y-0.5;
    //z=z-0.5;

    double rval= sqrt(x*x+y*y+z*z);
    return (1.0+m/(2.0*rval));


}
void psi(void)
{
    FILE *psi_file;
    psi_file=fopen("psi.asc","w+");    
    
    double dx=0.003125;
    double xmin=2.9375;
    double xmax=3.0625;
    double x=0.0;
    double y=0.5;
    double z=0.5;
    double nx,val;

    
    nx=(xmax-xmin)/dx;

    for (int i=0;i<nx;i++)
    {
        x=xmin+dx*i;
        x=x-3.0;
        val=1+1/(2*sqrt(x*x+y*y+z*z));
        val=pow(val,4);
        fprintf(psi_file,"%.13f %.13f\n",xmin+dx*i,val);

    }


    fclose(psi_file);





}



int main(int argc, char* argv[])
{                                   
    double dxyz;
    double dx;
    double div;
    char filename[30];
    strcpy(filename,"StaticBH_away05_dx0.003125");



    double tolerence=0.001;
    double tmpval,converge;
    double xmin,xmax,ymin,ymax,zmin,zmax;
    int nx,ny,nz;
    

    //Near Zone when black-hole is at 3,0,0
    /*
    dxyz=0.003125;
    xmin=2.9375;
    xmax=3.0625;
    ymin=-0.0078125;
    ymax=0.0078125;
    zmin=-0.0078125;
    zmax=0.0078125;
    
    */

    //Near Zone when black-hole is at 3,0.5,0.5
    /*
    dxyz=0.003125;
    xmin=2.9375;
    xmax=3.0625;
    ymin=0.4921875;
    ymax=0.5078125;
    zmin=0.4921875;
    zmax=0.5078125;
    */

    //Near Zone Grid is 3,0.1,0.1 
    
    dxyz=0.003125;
    xmin=2.9375;
    xmax=3.0625;
    
    ymin=0.0921875;
    ymax=0.1078125;
    zmin=0.0921875;
    zmax=0.1078125;
    

    //Near Zone Grid is 3,0,0 (over the bh)
    /*
    dxyz=0.003125;
    xmin=2.9375;
    xmax=3.0625;
    
    ymin=-0.0078125;
    ymax=0.0078125;
    zmin=-0.0078125;
    zmax=0.0078125;
    */
      



    //dxyz/=div;

//dxyz=0.0125/div;
    //dxyz=0.003125;

    //dxyz=0.001562;
    //dxyz=0.00078125;
    //dxyz=0.000390625;

    //xmin=0;
    //xmax=6;
    //ymin=-0.0078125;
    //ymax=0.0078125;
    //zmin=-0.0078125;
    //zmax=0.0078125;




   

    // Mid Zone
    /*
    dxyz=0.003125;
    xmin =-2.0;
    xmax =2.0;

    ymax =0.5078125;
    ymin =0.4921875;

    zmax =0.5078125; 
    zmin =0.4921875;
    */


    // Far zone
    /*
    dxyz=0.00625;
    xmax =5.0625;
    xmin =4.9375;

    ymax =0.5078125;
    ymin =0.4921875;

    zmax =0.5078125; 
    zmin =0.4921875; 
    */


   


    nx=(xmax-xmin)/dxyz;
    ny=(ymax-ymin)/dxyz; //set up for 5
    nz=(zmax-zmin)/dxyz; //set up for 5

    cout<<nx<<":"<<ny<<":"<<nz<<endl;
     

   FILE *file;
   strcat(filename,".asc");
   file=fopen(filename,"w+");    


    for(int i=2;i<nx-2;i++)
    {
        for(int j=2;j<ny-2;j++)
        {
            for(int k=2;k<nz-2;k++)
            {

                    // 4th Order finite difference stencil
                    tmpval=-funval(xmin+dxyz*(i+2),ymin+dxyz*j,zmin+dxyz*k)+16.0*funval(xmin+dxyz*(i+1),ymin+dxyz*j,zmin+dxyz*k)-30.0*funval(xmin+dxyz*i,ymin+dxyz*j,zmin+dxyz*k)+16.0*funval(xmin+dxyz*(i-1),ymin+dxyz*j,zmin+dxyz*k)-funval(xmin+dxyz*(i-2),ymin+dxyz*j,zmin+dxyz*k)-funval(xmin+dxyz*i,ymin+dxyz*(j+2),zmin+dxyz*k)+16.0*funval(xmin+dxyz*i,ymin+dxyz*(j+1),zmin+dxyz*k)-30.0*funval(xmin+dxyz*i,ymin+dxyz*j,zmin+dxyz*k)+16.0*funval(xmin+dxyz*i,ymin+dxyz*(j-1),zmin+dxyz*k)-funval(xmin+dxyz*i,ymin+dxyz*(j-2),zmin+dxyz*k)-funval(xmin+dxyz*i,ymin+dxyz*j,zmin+dxyz*(k+2))+16.0*funval(xmin+dxyz*i,ymin+dxyz*j,zmin+dxyz*(k+1))-30.0*funval(xmin+dxyz*i,ymin+dxyz*j,zmin+dxyz*k)+16.0*funval(xmin+dxyz*i,ymin+dxyz*j,zmin+dxyz*(k-1))-funval(xmin+dxyz*i,ymin+dxyz*j,zmin+dxyz*(k-2));
                    
                    tmpval=tmpval/(12.0*dxyz*dxyz);
                    

                    //fprintf(file,"%.13f %.13f %.13f %.13f\n",xmin+dxyz*i,ymin+dxyz*i,zmin+dxyz*i,tmpval);
                    fprintf(file,"%.13f %.13f\n",xmin+dxyz*i,tmpval);
                    cout<<setw(1)<< setiosflags(ios::fixed)<<setprecision(13)<<xmin+dxyz*i<<"  "<<tmpval<<endl;



            }
        }
    }

    fclose(file);
    /*
    FILE *file;
    file=fopen("file.asc","w+");
    for(int i=2;i<nx-2;i++)
    {
                    fprintf(file,"%.13f %.13f\n",xmin+dxyz*i,lapmatrix[i][2][2]);
                    //cout<<setw(1)<< setiosflags(ios::fixed)<<setprecision(13)<<xmin+dxyz*i<<"  "<<lapmatrix[i][2][2]<<endl;
    }  
    */

    return 0;	
}        
