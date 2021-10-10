/**                                                                                              **\
Reference : https://www.youtube.com/watch?v=XxHSes3RLgM&list=LL&index=8&t=387s
\**                                                                                              **/

#include <iostream>
#include <cmath>
#include <cstdio>
#include <fstream>

using namespace std;

// Define the ODE system functions : 
// Example : 
// (1)   dx/dt = y
// (2)   dy/dt = u(1-x^2)y - x
// (3)   u = sin(t)^{1/5}

double func1(double x1);

double func2(double &t, double x1, double x2, double u1);

double func_u(double t);


// TODO : 
// Define the Runge Kutta 4th : 
// Example : 

