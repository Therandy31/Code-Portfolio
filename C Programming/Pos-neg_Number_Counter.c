#include <stdio.h>


/*#2
prompt the user to enter numbers.
read a stream of numbers until user enters "0".
find and print the number of positive and negative numbers entered by user.
also find the sum of the positive and negative numbers.
*/
int main(void){

	int ch,pos_num,neg_num,count_pos,count_neg;
	pos_num = neg_num = count_pos = count_neg = 0;


	printf("Enter the stream of numbers: ");

	do{
		
		scanf("%d", &ch);

		if(0<ch){
			pos_num+= ch;
			count_pos+= 1;
		}
		else if(0>ch){
			neg_num+= ch;
			count_neg+= 1;
		}
		printf("Enter the stream of numbers: ");
	}while(ch!=0);
	printf("The stream of numbers has %d positive numbers, %d negative numbers, the sum of positive numbers was %d, and the sum of the negative numbers is %d.", count_pos, count_neg, pos_num, neg_num);
	scanf("%d", &ch);
}