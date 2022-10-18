// 문제 :
// lseek 함수 사용해 한 칸씩 띄어서 출력

#include<fcntl.h>
#include<stdlib.h>
#include<stdio.h>

int main(void) {
	int rfd, n;
	char buf[3];
	off_t cur;

	rfd = open("a.dat", O_RDONLY);
	if(rfd == -1){
		perror("open");
		exit(1);
	}

	cur = lseek(rfd, 0, SEEK_SET);

	while((n = read(rfd, buf, 1)) > 0) {
		write(1, buf, 1);
		cur = lseek(rfd, 1, SEEK_CUR);
	}

	close(rfd);

}