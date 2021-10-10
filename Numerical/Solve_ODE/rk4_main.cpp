#include "rk4.h"
using namespace std;

int main(){

double t;
double dt;
double TF;
const int N = 2;
const int M = 1;
double x[N+1];
double u[M+1];

// RK4 constants
double a1 = 0.166;
double a23 = 0.333;
double a4 = 0.166;

// function approximators
double k1, k2 ,k3, k4;
double l1, l2 ,l3, l4;

// initial conditions
dt = 0.01;
TF = 150;
x[1] = 0.01;
x[2] = 0;
t = 0.0;

// Output the u data
ofstream fout ("u.csv");
if (!fout){
    cout<< "\n error" <<endl;
}
fout << scientific;
fout.precision(8);

fout << "%Time(s.)" << "," << "X-Position (x[2])" << "," << "Y-Position (x[1])" << "," << "Input u" << "\n";


while (t <= TF){
    u[1] = func_u(t);

    // placeholders
    double t_2 = t + 0.5*dt;
    double t_3 = t + dt;

    // at each time step, forward iterations
    k1 = dt*func1(x[1]);
    l1 = dt*func2(t, x[1], x[2], u[1]);

    k2 = dt*func1(x[1] + 0.5*l1);
    l2 = dt*func2(t_2, x[1] + 0.5*l1, x[2]+0.5*k1, u[1]);

    k3 = dt*func1(x[1] + 0.5*l2);
    l3 = dt*func2(t_2, x[1] + 0.5*l2, x[2] + 0.5*k2, u[1]);

    k4 = dt*func1(x[1] + l3);
    l4 = dt*func2(t_3, x[1] + l3, x[2] + k3, u[1]);



    // update X-Position
    x[2] = x[2] + a1*(k1 + k4) + a23*(k2 + k3);
    // update Y-Position
    x[1] = x[1] + a1*(l1 + l4) + a23*(l2 + l3);


    // Output
    fout << t << "," << x[2] << "," << x[1] << "," << u[1] << "\n";
    t += dt;

}

cout<< "x[1] = " << x[1] <<endl;
cout<< "x[2] = " << x[2] <<endl;
cout<< "t = " << t <<endl;

system("pause");
return 0;

}