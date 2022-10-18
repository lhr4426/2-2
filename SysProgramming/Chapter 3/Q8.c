// 문제 :
// 현재 디렉토리의 내용이 디렉토리인지 파일인지 구별하여 출력

#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <stdlib.h>
#include <stdio.h>

int main(void) {
	
	DIR *dp;
	struct dirent *dent;
	struct stat sbuf;
	char path[BUFSIZ];
	char *cwd;

	cwd = getcwd(NULL, BUFSIZ);

	if((dp = opendir(cwd)) == NULL) {
		perror("opendir");
		exit(1);
	}

	while ((dent = readdir(dp))) {
		sprintf(path, "%s/%s", cwd, dent->d_name);
		stat(path, &sbuf);
		printf("name : %s\n", dent->d_name);
		printf("Type : ");
		if(S_ISDIR(sbuf.st_mode)) printf("Directory\n");
		if(S_ISREG(sbuf.st_mode)) printf("Regular File\n");
		printf("=======\n");
	}

	closedir(dp);
}