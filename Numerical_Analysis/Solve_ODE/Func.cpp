#include "Func.h"



double Func(int eq, double t, double w[]){
    double M;
    if (eq == 1) {M = w[2];}
    else if (eq == 2) {M = exp(2*t) * sin(t) - 2*w[1] + 2*w[2];}
    else {return 0;}

    return M;
}