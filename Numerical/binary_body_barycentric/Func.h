#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <fstream>

using namespace std;



double Func(int eq, double t, double w[], double G, double mu);

double init_v(double M1, double R, double G);

double init_ecce_v(double e, double init_v);

double barycentric_sys(int eq, double w[], double M1, double M2);
