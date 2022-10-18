// 문제 :
// 접근 권한 변경 (숫자모드)

#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

	struct stat buf;
	unsigned long modeItem = 0;

	if(argc != 3) {
		perror("argc is not 3");
		exit(1);
	}

	modeItem = strtol(argv[1], &argv[1], 8);

	stat(argv[2], &buf);
	printf("1. Mode = %o\n", (unsigned int)buf.st_mode);
	chmod(argv[2], modeItem);
	stat(argv[2], &buf);
	printf("2. Mode = %o\n", (unsigned int)buf.st_mode);

}

