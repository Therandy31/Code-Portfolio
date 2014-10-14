#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Sieve of Eratosthenes primes method for finding all primes 2 to n
int main(int n){
	

	//output file
	FILE *ofp;
	char outputFilename[] = "outputPrimesFile.txt";

	ofp = fopen(outputFilename, "w");

	if (ofp == NULL){
		fprintf(stderr, "Can't open output file %s!\n", outputFilename);
		exit(1);
	}


	//highest integer the user would like to search through for primes, my computer can only handle 1258
	int size;
	printf("Enter an integer n to find all the prime numbers less than or equal to n: ");
	scanf_s("%d", &size); 

	int *primes = (int*)malloc(size*sizeof(int)); //dynamic memory allocation

	//create array containing all members from 2 to n
	for (int x = 0; x <= size; x++){
		primes[x] = 1;
	}
	
	primes[0] = 0; //zero is not a prime
	primes[1] = 0; //nor is 1

	//set non-prime values in our primes array to false 
	for (int i = 2; i <= size; i++){
		if (primes[i] == 1){
			for (int j = 2; i*j <= size; j++){
				primes[i*j] = 0;
			}
		}
	}

	//write our remaining array of primes to an output file
	for (int i = 0; i <= size; i++){
		if (primes[i] == 1){
			fprintf(ofp, "%d ", i);
		}
	}


	fclose(ofp);

	int x;
	scanf_s("%d", &x);
}