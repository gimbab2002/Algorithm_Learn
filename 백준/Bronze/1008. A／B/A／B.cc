#include <stdio.h>
int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    if(a>0, a<10, b>0, b<10){
        printf("%.9f", (double)a/b);
        return 0;
    }
    else{return 0;}
}