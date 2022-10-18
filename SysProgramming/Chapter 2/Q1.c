// 문제 : 
// 저수준 파일 입출력으로 mycat 작성. 행 번호 붙여서 출력

#include<fcntl.h>
#include<unistd.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[]){
	int rfd, n;
	int count = 1;
	char buf[2];
	char cbuf[4];
	
	if(argc != 2) {
		perror("argc");
		exit(1);
	} 

	rfd = open(argv[1], O_RDONLY);
	if(rfd == -1){
		perror("open");
		exit(1);
	}

	sprintf(cbuf, "%d ", count);
	write(1, cbuf, strlen(cbuf));

	while((n = read(rfd, buf, 1)) > 0) {
		if(buf[0] == '\n') {
			if((n = read(rfd, buf, 1)) == 0) { break; }
			else {
				lseek(rfd, -1, SEEK_CUR);
				count++;
				printf("\n");
				sprintf(cbuf, "%d ", count);
				write(1, cbuf, strlen(cbuf));
			}
		else { write(1, buf, 1) }
		}
	}
	
	print("\n");
	close(rfd);
}