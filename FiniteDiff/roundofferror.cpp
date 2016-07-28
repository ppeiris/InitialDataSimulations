#include <stdio.h>
#include <iostream.h>
int main(int argc, char *argv[])
{
    double temp1, temp2, smallestNum;
    temp1 = 1.0;
    do {
        smallestNum = temp1;
        temp1 =temp1/2.0;
        temp2 = 1.0 + temp1;
    } while (temp2 > 1.0);
    cout<<smallestNum<<endl;
    return 0;
}
