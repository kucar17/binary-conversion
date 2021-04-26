#include <iostream>
#include <cmath>
#include <string>
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[])
{
    int Remainder[15], quotient[15], dNumber, system, loopCount;
    loopCount = 0;
    
    int count = 0;

    while (argv[++count] != NULL);

    if (count != 3)
    {
        cout << "You entered invalid number of arguments. The program will terminate." << endl;
        return 0;
    }

    else if (stoi(argv[2]) < 2 || stoi(argv[2]) > 9)
    {
        cout << "You entered a base number which is outside the range of the program (2:9). The program will terminate." << endl;
        return 0;
    }

    else
    {
        //Getting parameters:
        cout << "Running File: " << argv[0] << endl;
        system = atoi(argv[2]);
        dNumber = atoi(argv[1]);

        int ndigits = 1;

        while (dNumber > pow(system, ndigits))
        {
            ndigits++;
        }


        int dNumberNew = dNumber;

        // Converted number will be calculated by repeated division operations and recording remainders until quotient reaches 0.


        for (int i = 0; i >= 0; i++) //Infinite for loop
        {
            loopCount = i + 1;
            Remainder[i] = dNumberNew % system;
            quotient[i] = dNumberNew / system; // Since the variables are integers, this line does not assign the decimal places and finds the quotient easily.

            dNumberNew = quotient[i];

            if (quotient[i] == 0)
            {
                break;
            }

        }

        cout << "(" << dNumber << ")" << "_(" << 10 << ")" << " = ";

        for (int i = loopCount - 1; i >= 0; i--) //To print the remainder array in reverse order
        {
            cout << Remainder[i];
        }
        cout << "_(" << system << ")" << endl;

        cout << "" << endl;
    }
    return 0;
}





#include "Exp.h"
#include <cmath>
#include <iomanip>
#include <iostream>

using namespace std;

// x -> kuvvet n-> loop genişliği.
Exp::Exp(float src_x, int src_n){
    x = src_x;
    n = src_n;
}

double Exp::apprErr(){
    double realValue = exp(x);
    double calculatedValue = value();
    return realValue - calculatedValue;   
}

double Exp::value(){
    double factorial = 1;

    double calculated = 0;

    for(int k = 1; k <= n; k++){

        if(k != 0 && k != 1){

        for(int i = k; i >= 0; i--){
            factorial = factorial * (i - 1);
        }

        }
        else{
            factorial = 1;
        }

        calculated = calculated + (pow(x, k) / factorial);
        
        factorial = 1;
    }
    

    return calculated;
}

void Exp::print(){
    cout << value() << endl;
}



