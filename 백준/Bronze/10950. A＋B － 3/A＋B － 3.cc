#include <stdio.h>
int main(void){
    int i,j,a,b;
    j=0;
    scanf("%d", &i);
    int result[i];
    while(j<i){
        scanf("%d %d", &a, &b);
        result[j]=a+b;
        j++;
    }
    j=0;
    while(j<i){
        printf("%d\n",result[j]);
        j++;
    }
}