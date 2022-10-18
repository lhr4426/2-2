// 문제 :
// 현재 디렉토리의 파일을 지정한 디렉토리로 이동

#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
	
	DIR *dp;
	struct dirent *dent;
	char path[BUFSIZ];

	if(argc != 3) {
		perror("argc not 3");
		exit(1);
	}

	sprintf(path, "%s/%s", argv[2], argv[1]);

	link(argv[1], path);
	remove(argv[1]);
}