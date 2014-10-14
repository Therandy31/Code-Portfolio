#include <stdio.h>

int main(void){

	int a,b,num,GCD;

	printf("Enter a fraction: ");
	scanf("%d/%d", &a, &b);

	if(a>b){
		for(num=1;num<=b;num++){
			if(a%num==0 && b%num==0){
				GCD = num;
			}
		}
	}
	else if(b>a){
		for(num=1;num<=b;num++){
			if(a%num==0 && b%num==0){
				GCD = num;
			}
		}
	}
	a = a/GCD;
	b = b/GCD;

	printf("\n In lowest terms: %d/%d", a, b);
	scanf("%d");

}