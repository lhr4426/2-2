// 문제 : 
// 비어있는 디렉토리 삭제

#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]){
	DIR *dp;
	struct dirent *dent;
	struct stat sbuf;

	if (argc != 2) {
		perror("argc error");
		exit(1);
	} 

	if ((dp = opendir(argv[1])) == NULL ) {
		perror("open");
		exit(1)
	}

	while ((dent = readdir(dp))) {
		if (dent->d_name[0] == '.') continue;
		else{
			printf("%s is not empty\n", argv[1]);
			exit(1);
		}
	}
	rmdir(argv[1]);
	printf("%s is deleted\n", argv[1]);
}