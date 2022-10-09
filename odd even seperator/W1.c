#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main(){
    int a[6],b[6],c[6],i=0,j=0,k=0;
    printf("Input 6 elements in the array : ");
    for(i=0;i<6;i++) {
        scanf("%d",&a[i]);
    }
for(i=0;i<=6;i++){
    if(a[i] %2 == 0 ){
        j++;
        b[j] = a[i];
    }
    else {
        k++;
        c[k] = a[i];
    }
}
printf("even ",j);
for(i=1;i<=j;i++){
    printf("\n %d ",b[i]);
}
printf("odd ",j);
for(i=1;i<=j;i++){
    printf("\n %d ",c[i]);
}}
