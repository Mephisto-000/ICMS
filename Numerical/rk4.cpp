#include "rk4.h"


double func1(double x1){
    return x1;
}

double func2(double &t, double x1, double x2, double u1){
    double f2 = u1*(1 - pow(x2, 2))*x1 - x2;
    return f2;
}

double func_u(double t){
    double u = sin(pow(t, 0.2));
    return u;
}

