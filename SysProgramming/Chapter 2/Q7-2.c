// 문제 :
// 임시파일 생성 후 파일 명 출력, 학번과 이름 출력
// tempnam 사용

#include <stdio.h>

int main(void) {
        char *fname1;
        FILE *fp;

        fname1 = tempnam("/tmp","LHR");

        printf("%s\n",fname1);

        fp = fopen(fname1, "w");
        fputs("Lee Hyerim\n", fp);
        fputs("20211924\n", fp);
        fclose(fp);

}