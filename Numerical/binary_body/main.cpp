#include "Func.h"

using namespace std;


int main(){

    double G = 6.67;
    double M1 = 100;
    double M2 = 2;
    double mu = G*(M1 + M2);
    double R = 10; 

    double v_2_0 = init_v(M1, R, G);

    double t = 0.0;
    double pi_l = 2*3.1415926*R;
    double t_length = 100;
    double dt = pi_l / t_length;
    int eq = 4;
    double w[eq + 1], v1[eq + 1], v2[eq + 1], v3[eq + 1], v4[eq + 1];
    double k1[eq + 1], k2[eq + 1], k3[eq + 1], k4[eq + 1];
    int i, j;

    w[1] = R;
    w[2] = 0.0;
    w[3] = 0.0;
    w[4] = v_2_0;

    ofstream fout ("result.txt");
    if (!fout){
        cout<< "\n error" <<endl;
    }

    fout<< scientific;
    fout.precision(8);
    cout << "%Time(s.)" << "," << "rx (w[1])" << "," << "ry (w[2])" << "," << "vx (w[3])" << "," << "vy (w[4])" << "\n";
    fout << t << "," << w[1] << "," << w[2] << "," << w[3] << "," << w[4] << "\n";
    for (i = 1; i <= t_length; i++){

        for (j = 1; j <= eq; j++){
            k1[j] = dt*Func(j, t, w, G, mu, R);
            v1[j] = w[j] + 0.5*k1[j];
        }
        for (j = 1; j <= eq; j++){
            k2[j] = dt*Func(j, t + 0.5*dt, v1, G, mu, R);
            v2[j] = w[j] + 0.5*k2[j];
        }
        for (j = 1; j <= eq; j++){
            k3[j] = dt*Func(j, t + 0.5*dt, v2, G, mu, R);
            v3[j] = w[j] + k3[j];
        }
        for (j = 1; j <= eq; j++){
            k4[j] = dt*Func(j, t + dt, v3, G, mu, R);
        }

        for (j = 1; j <= eq; j++){
            w[j] = w[j] + (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) / 6.0;
        }

        t += dt;
        fout << t << "," << w[1] << "," << w[2] << "," << w[3] << "," << w[4] << "\n";

    }

    cout<< "w[1] = " << w[1] <<endl;
    cout<< "w[2] = " << w[2] <<endl;
    cout<< "w[3] = " << w[3] <<endl;
    cout<< "w[4] = " << w[4] <<endl;
    cout<< "t = " << t <<endl;


    system("pause");
    return 0;
}