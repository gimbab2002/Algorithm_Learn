#include <stdio.h>
int main(void){
    int a,b,c;
    scanf("%d %d %d", &a,&b,&c);
    if(a==b && b==c){
        printf("%d", 10000+(a*1000));
        return 0;
    }
    else if(((a==b)&&(b!=c)) || ((b==c)&&(a!=c)) || ((a==c)&&(b!=c))){
        if(a==b){printf("%d", 1000+(a*100));}
        if(b==c){printf("%d", 1000+(b*100));}
        if(a==c){printf("%d", 1000+(a*100));}
        return 0;
    }
    else if((a!=b) && (b!=c) && (c!=a)){
        if((a>b) && (a>c)){printf("%d",a*100);}
        if((b>a) && (b>c)){printf("%d",b*100);}
        if((c>a) && (c>b)){printf("%d",c*100);}
        return 0;
    }
    return 0;
}