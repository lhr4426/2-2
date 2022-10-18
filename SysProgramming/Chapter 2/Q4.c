// 문제 :
// 3번 문제를 fread와 fwrite로 동일 결과 출력

#include<stdlib.h>
#include<stdio.h>

int main(void){
	FILE *rfp;
	char buf[3];
	int n;

	if((rfp = fopen("a.dat", "r")) == NULL) {
		perror("fopen");
		exit(1);
	}

	while((n = fread(buf, sizeof(char), 2, rfp)) > 0){
		fwrite(buf, sizeof(char), 1, stdout);
	}

	fclose(rfp);

}