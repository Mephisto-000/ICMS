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


double init_ecce_v(double e, double init_v){
    return sqrt((1 - e)*pow(init_v, 2));
}


double barycentric_sys(int eq, double w[], double M1, double M2){
    double M;
    double ratio_M1 = M2 / (M1 + M2);
    double ratio_M2 = M1 / (M1 + M2);
    // r : 
    if (eq == 1) {M = w[1]*ratio_M1;}
    else if (eq == 2) {M = w[2]*ratio_M1;}
    else if (eq == 3) {M = -w[1]*ratio_M2;}
    else if (eq == 4) {M = -w[2]*ratio_M2;}
    // v : 
    else if (eq == 5) {M = w[3]*ratio_M2;}
    else if (eq == 6) {M = w[4]*ratio_M2;}
    else if (eq == 7) {M = -w[3]*ratio_M2;}
    else if (eq == 8) {M = -w[4]*ratio_M2;}

    else {return 0;}


    return M;
}

