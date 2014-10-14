#include <stdio.h>
#include <ctype.h>

#define MAX_DIGITS 10
char user_input[255];

void print_segment(int segment, int digit);
void print_digits(int a, int b, int c);


void print_segment(int segment, int digit){
	const int segments[10][7] = {
		{1, 1, 1, 1, 1, 1, 0},  // 0
		{0, 1, 1, 0, 0, 0, 0},  // 1
		{1, 1, 0, 1, 1, 0, 1},  // 2
		{1, 1, 1, 1, 0, 0, 1},  // 3
		{0, 1, 1, 0, 0, 1, 1},  // 4
		{1, 0, 1, 1, 0, 1, 1},  // 5
		{1, 0, 1, 1, 1, 1, 1},  // 6
		{1, 1, 1, 0, 0, 0, 0},  // 7
		{1, 1, 1, 1, 1, 1, 1},  // 8
		{1, 1, 1, 1, 0, 1, 1}   // 9
	};

	const char display[8] = "_||_||_";

	if((segment >= 0) && (segments[digit][segment])){
		printf("%c", display[segment]);
	}else{
		printf(" ");
		}
}


void print_digits(int a, int b, int c){

	int i, some_digit, digit_count;
	digit_count = 0;

	for(i = 0; user_input[i] != '\n' && digit_count < MAX_DIGITS; i++){
		if(isdigit(user_input[i])){
			some_digit = (int) user_input[i] - '0';
			print_segment(a,some_digit);
			print_segment(b,some_digit);
			print_segment(c,some_digit);
			printf(" ");

			digit_count++;
		}
	}
	printf("\n");
}


int main(void){

	printf("Enter a number up to %d digits: ", MAX_DIGITS);
	fgets(user_input, sizeof(user_input), stdin);
	

	print_digits(-1,0,-1);
	print_digits(5,6,1);
	print_digits(4,3,2);


	scanf_s("%c", user_input);
	return 0;

}