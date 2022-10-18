// 문제 :
// 저수준 파일 입출력으로 파일 복사 프로그램 작성

#include<sys/stat.h>
#include<fcntl.h>
#include<unistd.h>
#include<sys/types.h>
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[]){
	int rfd, wfd, n;
	char buf[BUFSIZ];

	if(argc != 3) {
		perror("argc");
		exit(1);
	}

	rfd = open(argv[1], O_RDONLY);
	if(rfd == -1) {
		perror("open");
		exit(1);
	}

	wfd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
	if(wfd == -1) {
		perror("open");
		exit(1);
	}

	while((n = read(rfd, buf, BUFSIZ)) > 0) {
		write(wfd, buf, n);
	}

	close(rfd);
	close(wfd);

}