/*#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string.h>
#include <math.h>
#include "CheckError.h"
*/
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>

#include <cmath>
#include <iomanip>
#include <fstream>

#include "NCheckError.h"


using namespace std;
int main(int argc,char *argv[])
{
	CheckError *error=new CheckError();
	error->ReadData(argc,argv);
	delete(error);

	return 0;	
}
