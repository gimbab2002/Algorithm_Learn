#include <stdio.h>
int main(void){
    int a,b;
    int temp;
    int pos10;
    int pos100;
    int pos1;
    scanf("%d", &a);
    scanf("%d", &b);
    pos100 = b / 100;
    pos10 = b % 100 /10;
    pos1 = b % 100 % 10;
    printf("%d\n", a*pos1);
    printf("%d\n", a*pos10);
    printf("%d\n", a*pos100);
    printf("%d", a*b);
    return 0;
}