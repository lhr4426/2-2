// 문제 :
// lseek 함수 사용해 한 칸씩 띄어서 출력

#include<fcntl.h>
#include<stdlib.h>
#include<stdio.h>

int main(void) {
        int rfd, n;
        char buf[3];

        rfd = open("a.dat", O_RDONLY);
        if(rfd == -1) {
                perror("open");
                exit(1);
        }

        while((n = read(rfd, buf, 2)) > 0) {
                write(1, buf, 1);
        }

        close(rfd);

}