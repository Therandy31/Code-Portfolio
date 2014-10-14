#include <stdio.h>

int main(void){
	int i,x,y;

	printf("Enter a two-digit number:");
	scanf("%d",& i);

	x= i%10;
	y= i/10;
	i= x*10+y;

	printf("\n The reversal is:");
	printf("%d", i);
	
	scanf("%d",& i);
	return 0;
}