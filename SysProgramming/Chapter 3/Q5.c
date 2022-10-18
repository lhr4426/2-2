// 문제 :
// 디렉토리 생성 후 작업 디렉토리 변경

#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]){

	DIR *dp;
	int n;
	char *cwd;

	if(argc != 2) {
		perror("argc error");
		exit(1);
	}

	if((n = mkdir(argv[1], 0777)) == -1) {
		perror("mkdir");
		exit(1);
	}

	if((n = chdir(argv[1])) == -1) {
		perror("chdir");
		exit(1);
	}

	cwd = getcwd(NULL, BUFSIZ);
	printf("Current Work Directory : %s\n", cwd);
}