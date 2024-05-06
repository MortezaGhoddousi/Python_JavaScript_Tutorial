#include <stdio.h>

int factorial(int n){
    int a = 1;
    int x = 1;
    while(a<n){
        x = x*a;
        a++;
    }
    return x;
}

int main(){

    int x = factorial(5);
    printf("The value of 5! is: %d", x);
    return 0;
}
