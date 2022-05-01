#include "Func.h"


double Func(int eq, double t, double w[], double G, double mu){
    double M;
    double r = sqrt(pow(w[1], 2) + pow(w[2], 2));
    if (eq == 1) {M = w[3];}
    else if (eq == 2) {M = w[4];}
    else if (eq == 3) {M = -mu*w[1] / pow(r, 3);}
    else if (eq == 4) {M = -mu*w[2] / pow(r, 3);}
    else {return 0;}

    return M;
}


double init_v(double M1, double R, double G){
    return sqrt(G*M1 / R);
}


