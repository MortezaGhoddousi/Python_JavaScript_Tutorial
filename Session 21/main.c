#include <stdio.h>

int main(){

    // printf("hello");
    int x1 = 20;
    int x2 = 18;
    float x3 = 19.5;

    float average = (x1+x2+x3)/3;

    float x[] = {x1, x2, x3};

    int i = 0;
    int Min = 21;
    int Max = -1;
    while (i<3){
        if (x[i] < Min){
            Min = x[i];
        }

        if (x[i] > Max){
            Max = x[i];
        }
        i++;
    }

    printf("average is %f \n", average);
    printf("minimum is %d \n", Min);
    printf("maximum is %d \n", Max);
}