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
//    z=z-0.5;

    double rval= sqrt(x*x+y*y+z*z);
    return (1.0+m/rval);


}
int main(int argc, char* argv[])
{                                   

    double tolerence=0.001;
    double tmpval,converge;
    double xmin,xmax,ymin,ymax,zmin,zmax;
    double dxyz;
    int nx,ny,nz;
    /*
    dxyz=0.003125;
    xmin=2.9375;
    xmax=3.0625;
    ymin=-0.0625;
    ymax=0.0625;
    zmin=-0.0625;
    zmax=0.0625;
    */

    //dxyz=0.003125;
    //dxyz=0.001562;
    dxyz=0.00078125;
    //dxyz=0.000390625;

    xmin=0;
    xmax=6;
    ymin=-0.0078125;
    ymax=0.0078125;
    zmin=-0.0078125;
    zmax=0.0078125;

    cout<<"I am here";
    nx=(xmax-xmin)/dxyz;
    ny=(ymax-ymin)/dxyz; //set up for 5
    nz=(zmax-zmin)/dxyz; //set up for 5
    
    //double matrix[nx][ny][nz];


    double ***matrix=new double**[nx]; 
    for(int i=0;i<nx;i++)
        matrix[i]=new double*[ny];
    for(int i=0;i<nx;i++)
        for(int j=0;j<ny;j++)
            matrix[i][j]=new double[nz];

    


/*
     for(int i=0;i<nx;i++)
    {
        for(int j=0;j<ny;j++)
        {
            for(int k=0;k<nz;k++)
            {
                mat[i][j][k]=0.0;
                
            }
        }
    

    }

 
  *
  *
int ***a = new int**[Dim1];
for( int i(0); i < Dim1; i++ )
    a[i] = new int*[Dim2];

for( int i(0); i < Dim1; i++ )
    for( int j(0); j < Dim2; j++ )
        a[i][j] = new int[Dim3];
    */











    double lapmatrix[nx][ny][nz];

    //cout<<nx<<','<<ny<<','<<nz<<endl;

    for(int i=0;i<nx;i++)
    {
        cout<<"i = "<<i;
        for(int j=0;j<ny;j++)
        {
            for(int k=0;k<nz;k++)
            {
                matrix[i][j][k]=funval((xmin+dxyz*i),(ymin+dxyz*j),(zmin+dxyz*k));
                //lapmatrix[i][j][k]=0.0;
            }
        }
    }

    return 0;

   double tmperror=0.0;
   double error_max=0.0;
   double error; 

    for(int i=2;i<nx-2;i++)
    {
        for(int j=2;j<ny-2;j++)
        {
            for(int k=2;k<nz-2;k++)
            {

                    // 4th Order finite difference stencil
                    tmpval=-matrix[i+2][j][k]+16.0*matrix[i+1][j][k]-30.0*matrix[i][j][k]+16.0*matrix[i-1][j][k]-matrix[i-2][j][k]-matrix[i][j+2][k]+16.0*matrix[i][j+1][k]-30.0*matrix[i][j][k]+16.0*matrix[i][j-1][k]-matrix[i][j-2][k]-matrix[i][j][k+2]+16.0*matrix[i][j][k+1]-30.0*matrix[i][j][k]+16.0*matrix[i][j][k-1]-matrix[i][j][k-2];
                    
                    tmpval=tmpval/(12.0*dxyz*dxyz);
                    lapmatrix[i][j][k]=tmpval;
            }
        }
    }


    for(int i=2;i<nx-2;i++)
    {
                    //cout<<xmin+dxyz*i<<' '<<lapmatrix[i][2][2]<<endl;
                    cout<<setw(1)<< setiosflags(ios::fixed)<<setprecision(13)<<xmin+dxyz*i<<"  "<<lapmatrix[i][2][2]<<endl;
    }  
        
      
    //return 0;
      //cout<<setw(1)<< setiosflags(ios::fixed)<<setprecision(13)<<real_val<<"  "<<approx<<"  "<<error<<"  "<<h_val<<endl;


        return 0;	
}        
