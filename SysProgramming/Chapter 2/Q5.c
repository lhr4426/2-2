// 문제 :
// 고수준 파일 입출력으로 파일명 변경. 명령행 인자 사용

#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[]) {
        FILE *rfp, *wfp;
        int n;
        char buf[BUFSIZ];

        if(argc != 3) {
                perror("argv");
                exit(1);
        }

        if((rfp = fopen(argv[1], "r")) == NULL) {
                perror("fopen");
                exit(1);
        }

        if((wfp = fopen(argv[2], "w")) == NULL) {
                perror("fopen");
                exit(1);
        }

        while((n = fread(buf, sizeof(char), BUFSIZ, rfp)) > 0) {
                fwrite(buf, sizeof(char), n, wfp);
        }

        fclose(rfp);
        fclose(wfp);

        unlink(argv[1]);

}