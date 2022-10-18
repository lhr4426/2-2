// 문제 :
// 데이터 파일 읽어 학번과 성적 평균 출력. 저수준 파일 입출력 사용

#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#define PEOPLE 2
#define COURSE 3

int main(void) {
        int rfd, n,i, j, hakbun;
        int sum = 0;
        char buf1[8];
        char buf2[3];

        rfd = open("b.dat", O_RDONLY);
        if(rfd == -1) {
                perror("open");
                exit(1);
        }

        for(i = 0; i < PEOPLE; i++){
                n = read(rfd, buf1, 7);
                buf1[n] = '\0';
                printf("%s :", buf1);
                for(j = 0; j < COURSE; j++){
                        lseek(rfd, 1, SEEK_CUR);
                        n = read(rfd, buf2, 2);
                        sum += atoi(buf2);
                }
                printf("%.2f\n", sum/3.);
                lseek(rfd, 1, SEEK_CUR);
                sum = 0;
        }

        close(rfd);
}