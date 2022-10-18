// 문제 :
// 접근 권한 변경 (문자모드)

#include <sys/types.h>
#include <sys/stato.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

	struct stat buf;
	char *pointer = argv[1];
	char changemode[4];
	int n, k;

	if(argc != 3){
		perror("argc is not 3");
		exit(1);
	}

	for(n = 0; n < 3; n++) {
		changemode[n] = *(pointer + n);
	}

	changemode[3] = '\0';

	stat(argv[2], &buf);
	printf("1. Mode = %o\n", (unsigned int)buf.st_mode);
	switch(changemode[0]) {
		case 'u':
			k = 0b000111000000;
			break;
		case 'g':
			k = 0b000000111000;
			break;
		case 'o':
			k = 0b000000000111;
			break;
	}
	switch(changemode[2]) {
		case 'r':
			k &= 0b000100100100;
			break;
		case 'w':
			k &= 0b000010010010;
			break;
		case 'x':
			k &= 0b000001001001;
			break;
	}

	if(changemode[1] == '+') {
		buf.st_mode |= k;
	}
	else if(changemode[1]) == '-') {
		buf.st_mode &= ~(k);
	}

	chmod(argv[2], buf.st_mode);
	printf("2. Mode = %o\n", (unsigned int)buf.st_mode);
	}
}