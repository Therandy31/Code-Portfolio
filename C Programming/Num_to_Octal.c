#include <stdio.h>

int main(void){

	int num,number1,number2,number3,number4,number5;

	printf("Enter a numer between 0 and 32767: ");
	scanf("%d", &num);

	number1 = num % 8;
	num = num / 8;

	number2 = num % 8;
	num = num / 8;

	number3 = num % 8;
	num = num / 8;

	number4 = num % 8;
	num = num / 8;

	number5 = num % 8;
	
	printf("In octal, your number is: %d%d%d%d%d", number5,number4,number3,number2,number1);
	scanf("%d", &num);

	return 0;
}
