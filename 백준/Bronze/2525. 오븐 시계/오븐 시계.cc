#include <stdio.h>
int main(void){
    int hr, min, time;
    scanf("%d %d %d", &hr, &min, &time);
    if((min+time / 60)>=1){ //걸리는 시간과 분을 더했을 때, 다음 시간으로 넘어감
        if((hr+((min+time) / 60)) >= 24){ //시간이 24시를 넘어갈 경우
            printf("%d %d",(hr+((min+time) / 60))-24,(min+time) % 60);
        } 
        else {
            printf("%d %d", hr+((min+time) / 60), (min+time) % 60);
        }
    } 
    else if(((min+time)/60) == 0){
        printf("%d %d", hr, (min+time) % 60);
    }
    return 0;
}