#include <stdio.h>
#include <math.h>

int main()
{
    double a= 2, b= -400, c= 50;
    double x1, x2, d;

    d = pow(b,2) - 4*a*c;

    if(d > 0)
    {
        x1 = (-b - sqrt(d)) / (2*a);
        x2 = (-b + sqrt(d)) / (2*a);

        printf("X1 = %.2f\n", x1);
        printf("X2 = %.2f\n", x2);
        printf("Two roots");
    }

    else if(d == 0)
    {
        x1 =  -b / (2*a);

        printf("X = %.2f\n", x1);
        printf("One root");
    }

    else
    {
        printf("Not possible");
    }

    return 0;
}
