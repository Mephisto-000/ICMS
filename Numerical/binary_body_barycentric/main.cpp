#include "Func.h"

using namespace std;


int main(){

    double pi = 3.1415926;
    double G = 4*pow(pi, 2);            // AU^3 / (M * yr^{2})
    double M1 = 1;                      
    double M2 = 1;               
    double mu = G*(M1 * M2);
    double R = 1;           // AU
    double e = 0.5;        // eccentricity 

    double v_2_0 = init_v(M1, R, G);
    double v_e2_0 = init_ecce_v(e, v_2_0); // 計算有離心率時的初始速度

    double t = 0.0;
    double t_length = 100;
    double dt = 0.01;          
    int eq = 4;
    double w[eq + 1], v1[eq + 1], v2[eq + 1], v3[eq + 1], v4[eq + 1];
    double k1[eq + 1], k2[eq + 1], k3[eq + 1], k4[eq + 1];
    double w2[eq*2 + 1];
    int i, j;

    w[1] = R;
    w[2] = 0.0;
    w[3] = 0.0;
    w[4] = v_e2_0;

    w2[1] = w[1];
    w2[2] = w[2];
    w2[3] = 0.0;
    w2[4] = 0.0;
    w2[5] = w[3];
    w2[6] = w[4];
    w2[7] = 0.0;
    w2[8] = 0.0;


    ofstream fout ("result.txt");
    if (!fout){
        cout<< "\n error" <<endl;
    }

    fout<< scientific;
    fout.precision(8);
    cout << "r1x (w2[1])" << "," << "r1y (w2[2])" << "r2x (w2[3])" << "," << "r2y (w2[4])" << "," << "v1x (w2[5])" << "," << "v1y (w2[6])" << "v2x (w2[7])" << "," << "v2y (w2[8])" << "\n";
    for (i = 1; i <= t_length; i++){

        for (j = 1; j <= eq; j++){
            k1[j] = dt*Func(j, t, w, G, mu);
            v1[j] = w[j] + 0.5*k1[j];
        }
        for (j = 1; j <= eq; j++){
            k2[j] = dt*Func(j, t + 0.5*dt, v1, G, mu);
            v2[j] = w[j] + 0.5*k2[j];
        }
        for (j = 1; j <= eq; j++){
            k3[j] = dt*Func(j, t + 0.5*dt, v2, G, mu);
            v3[j] = w[j] + k3[j];
        }
        for (j = 1; j <= eq; j++){
            k4[j] = dt*Func(j, t + dt, v3, G, mu);
        }

        for (j = 1; j <= eq; j++){
            w[j] = w[j] + (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) / 6.0;
        }


        for (j = 1; j <= eq*2 + 1; j++){
                w2[j] = barycentric_sys(j, w, M1, M2);
            }


        t += dt;
        fout << w2[1] << "," << w2[2] << "," << w2[3] << "," << w2[4] << "," 
            << w2[5] << "," << w2[5] << "," << w2[7] << "," << w2[8] << "\n";

    }

    cout<< "w[1] = " << w[1] <<endl;
    cout<< "w[2] = " << w[2] <<endl;
    cout<< "w[3] = " << w[3] <<endl;
    cout<< "w[4] = " << w[4] <<endl;
    cout<< "t = " << t << "\n" <<endl;
    cout<< "w2[1] = " << w2[1] <<endl;
    cout<< "w2[2] = " << w2[2] <<endl;
    cout<< "w2[3] = " << w2[3] <<endl;
    cout<< "w2[4] = " << w2[4] <<endl;
    cout<< "w2[5] = " << w2[5] <<endl;
    cout<< "w2[6] = " << w2[6] <<endl;
    cout<< "w2[7] = " << w2[7] <<endl;
    cout<< "w2[8] = " << w2[8] <<endl;

    fout.close();

    system("pause");
    return 0;
}