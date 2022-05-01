#include "Func.h"

using namespace std;



int main(){

    double t = 0.0;
    double dt = 0.1;
    double t_length = 10;
    int eq = 2;
    double w[eq + 1], v1[eq + 1], v2[eq + 1], v3[eq + 1], v4[eq + 1];
    double k1[eq + 1], k2[eq + 1], k3[eq + 1], k4[eq + 1];
    int i, j;

    w[1] = -0.4;
    w[2] = -0.6;

    ofstream fout ("result.txt");
    if (!fout){
        cout<< "\n error" <<endl;
    }

    fout<< scientific;
    fout.precision(8);
    fout << "%Time(s.)" << "," << "w1 (w[1])" << "," << "w2 (w[2])" << "\n";
    fout << t << "," << w[1] << "," << w[2] << "\n";
    for (i = 1; i <= t_length; i++){

        for (j = 1; j <= eq; j++){
            k1[j] = dt*Func(j, t, w);
            v1[j] = w[j] + 0.5*k1[j];
        }
        for (j = 1; j <= eq; j++){
            k2[j] = dt*Func(j, t + 0.5*dt, v1);
            v2[j] = w[j] + 0.5*k2[j];
        }
        for (j = 1; j <= eq; j++){
            k3[j] = dt*Func(j, t + 0.5*dt, v2);
            v3[j] = w[j] + k3[j];
        }
        for (j = 1; j <= eq; j++){
            k4[j] = dt*Func(j, t + dt, v3);
        }

        for (j = 1; j <= eq; j++){
            w[j] = w[j] + (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) / 6.0;
        }

        t += dt;
        fout << t << "," << w[1] << "," << w[2] << "\n";

    }

    cout<< "w[1] = " << w[1] <<endl;
    cout<< "w[2] = " << w[2] <<endl;
    cout<< "t = " << t <<endl;


    system("pause");
    return 0;
}