#include <stdio.h>
#include <string.h>

int main(void){
  char name[64] = {0};
  fgets(name, sizeof(name), stdin);
  if (strlen(name) > 1) {
    printf("Hello, %s", name);
  } else {
    printf("Hello, world!\\n");
  }
  return 0;
}
