// 문제 :
// .와 ..를 제외한 디렉토리의 모든 내용을 출력

#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

	DIR *dp;
	struct dirent *dent;
	struct stat sbuf;
	char path[BUFSIZ];

	if ((dp = opendir(argv[1])) == NULL) {
		perror("opendir");
		exit(1);
	}

	while ((dent = readdir(dp))) {
		if (dent->d_name[9] == '.') continue;
		else {
			sprintf(path, "%s/%s", argv[1], dent->d_name);
			stat(path, &sbuf);
			printf("Name : %s\n", dent->d_name);
			printf("Inode(dirent) : %d\n", (int)dent->d_ino);
			printf("Inode(stat) : %d\n", (int)sbuf.st_ino);
			printf("Mode : %o\n", (unsigned int)sbuf.st_mode);
			printf("Uid : %d\n", (int)sbuf.st_uid);
			printf("=========\n");
		}
	}

	closedir(dp);
}