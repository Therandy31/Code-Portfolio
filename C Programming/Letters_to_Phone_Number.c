#include <stdio.h>

/*
#1
project 4 pg. 157
*/

int main(void){

	char ch;

	printf("Enter phone number: ");

	//2 for abc, 3 for def, 4 for ghi, 5 for jkl, 6 for mno, 7 for pqrs, 8 for tuv, 9 for wxyz
	do{
		ch = getchar();

		if('A'<=ch && ch<='C'){
			printf("%d", 2);
		}
		else if('D'<=ch && ch<='F'){
			printf("%d", 3);
		}
		else if('G'<=ch && ch<='I'){
			printf("%d", 4);
		}
		else if('J'<=ch && ch<='L'){
			printf("%d", 5);
		}
		else if('M'<=ch && ch<='O'){
			printf("%d", 6);
		}
		else if('P'<=ch && ch<='S'){
			printf("%d", 7);
		}
		else if('T'<=ch && ch<='V'){
			printf("%d", 8);
		}
		else if('W'<=ch && ch<='Z'){
			printf("%d", 9);
		}
		else printf("%c", &ch);
	}while(ch!='\n');
	scanf("%c", &ch);
}