#include <stdio.h>
int main(void){
    int hr, min;
    scanf("%d %d", &hr, &min);
    if(min >= 45){printf("%d %d",hr, min-45);}
    else if(hr == 0 && min < 45){printf("%d %d", 23, 60-(45-min));}
    else if(hr !=0 && min < 45){printf("%d %d", hr-1, 60-(45-min));}
    return 0;
}