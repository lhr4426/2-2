// 문제 :
// 파일 정보 자세히 출력

#include <sys/stat.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

	if (argc != 2) {
		perror("argc error");
		exit(1);
	}

	struct stat buf;
	int filtType, n;

	stat(argv[1], &buf);
	fileType = buf.st_mode & S_IFMT;
	printf("file name : %s\n", argv[1]);
	printf("inode : %d\n", (int)buf.st_ino);
	printf("type : ");
	switch(fileType) {
		case S_IFIFO :
			printf("FIFO File\n");
			break;
		case S_IFDIR :
			printf("Directory\n");
			break;
		case S_IFREG :
			printf("Regular File\n");
			break;
	}
	printf("mode : ");

	for(n = 0; n < 3; n++){
		if((buf.st_mode & (S_IREAD >> (n*3))) != 0 ){ printf("r"); }
		else{printf("-");}
		if((buf.st_mode & (S_IWRITE >> (n*3))) != 0 ){ printf("w"); }
		else{printf("-");}
		if((buf.st_mode & (S_IEXEC >> (n*3))) != 0 ){ printf("x"); }
		else{printf("-");}
	}
	printf("\n");
	printf("uid : %d\n", (int)buf.st_ino);
	printf("mtime : %d\n", (int)buf.st_mtime);
	
}