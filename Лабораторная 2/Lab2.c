#include<stdio.h>

int main()
{
    double matrix_3x3[3][3];
    double MainDiagonal = 0;
    double SideDiagonal = 0;

    printf("Enter 9 numbers for 3x3 matrix:\n");

    for(int row = 0; row < 3; row++) {
        printf("Enter row %d:", row + 1);
       for(int col = 0; col < 3; col++) {
           scanf("%lf", &matrix_3x3[row][col]);
       }
    }

    for(int row = 0; row < 3; row++) {
        MainDiagonal = MainDiagonal + matrix_3x3[row][row];
        SideDiagonal = SideDiagonal + matrix_3x3[row][2 - row];
    }
    printf("Main diagonal = %.2f\n", MainDiagonal);
    printf("Side diagonal = %.2f\n", SideDiagonal);

    return 0;
}
