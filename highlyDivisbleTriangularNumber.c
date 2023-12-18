#include <stdio.h>

long long triangularNumber (long long x){
  long long sum = 0;
  for (int i = 1; i <= x; i++)
    sum += i;
  return sum;
}

int countFactors(long long x){
  int c = 0;
  for (int i = 1; i <= x; i++){
    if (x % i == 0)
      c++;
  }
  return c;
}

long long HighestTriangularNumberDivisors (int n){
  long long x;
  int c = 1;
  int i = 1;
  while (c <= n){
    x = triangularNumber(i);
    c = countFactors(x);
    i++;
  }
  return x;
}


int main(){
  long long hdtn = HighestTriangularNumberDivisors(500);
  printf("hdtn = %lld",hdtn);
  return 0;
}