#include <stdio.h>
#include <math.h>

int main()
{
    double a= 2, b= -400, c= 50;
    double x_1, x_2, d;

    d = b*b - 4*a*c;

    if(d > 0)
    {
        x_1 = (-b - sqrt(d))	/ (2*a);
        x_2 = (-b + sqrt(d))	/ (2*a);

        printf("X1 = %1f\n", x_1);
        printf("X2 = %1f\n", x_2);
        printf("Two");
    }

    else if(d == 0)
    {
        x_1 =  -b / (2*a);

        printf("X = %1f\n", x_1);
        printf("One");
    }

    else
    {
        printf("Not possible");
    }

    return 0;


}
