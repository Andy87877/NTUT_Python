# include <stdio.h>
int main() {
    int n = 0;
    scanf("%d", &n);
    int a = n;
    int num = 0;

    while (n!=1) {
        num += 1;
        n = (a-num)+1;
        printf("%d",num);
        if (n == 1) printf("\n");
    } 
    if(a==1){
        printf("1");
    }
    return 0;
}