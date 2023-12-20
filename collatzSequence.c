#include <stdio.h>
#define MAX_SIZE 1000000


int collatzResults[MAX_SIZE];

int collatzSequence(int x){
  int c = 1;
  long long int n = x;
  
  if (n < MAX_SIZE && collatzResults[n] != 0)
    return collatzResults[n-1];
  do{
    if (n % 2 == 0)
      n = n / 2;
    else
      n = 3*n + 1;
    c++;  
  }while (n != 1);
  if (n < MAX_SIZE)
    collatzResults[n - 1] = n;
  return c;
}
int largestCollatzSequence(int x){
  int max = collatzSequence(1);
  int currentCollatz;
  int i = 2;
  while (i < x){
    currentCollatz = collatzSequence(i);
    if (currentCollatz > max)
      max = currentCollatz;  
    i++;
  }
  return max;
}
int main(){
  printf("%d",largestCollatzSequence(1000000));
  return 0;
}