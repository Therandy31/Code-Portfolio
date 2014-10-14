#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROW 10
#define COL 10
#define DIRECTIONS 4


int main(void){

	//x for row, y for col
	int letter_count = 0;
	int row = 0;
	int col = 0;
	int move_direction;

	char board[ROW][COL];

	const char letters[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	
	for(row = 0; row < ROW; row++){
		for(col = 0; col < COL; col++){
			board[row][col] = '.';
		}
	}

	row = 0;
	col = 0;

	srand((unsigned)time(NULL));

	board[row][col] = letters[0];

	while(letters[letter_count] != 'Z'){

		move_direction = rand()% DIRECTIONS;

		if(board[row][col] == '.'){
			board[row][col] = letters[++letter_count];
		}
		if((board[row][col + 1] != '.' || row == ROW - 1 )&& (board[row + 1][col] != '.' || row == COL -1) && (board[row - 1][col] != '.' || row == 0) && (board[row][col - 1] != '.' || col == 0)){
			break;
		}
		

		switch(move_direction){
		case 0:
			if (col < ROW - 1 && board[row][col + 1] == '.'){ // UP
              col++;
			  break;
			}
		case 1: if (row < COL -1 && board[row + 1][col] == '.') { // RIGHT
              row++;
              break;
			}
		case 2: if (row > 0 && board[row - 1][col] == '.'){ // DOWN
              row--;
              break;
			}
		case 3: if (col > 0 && board[row][col - 1] == '.') { // LEFT
              col--;
              break;
			}
		}
	}

	for(row = 0; row < ROW; row++){
		for(col = 0; col < COL; col++){
			printf("%c", board[row][col]);
		}
		printf("\n");
	}
	getchar();
	return 0;

}
