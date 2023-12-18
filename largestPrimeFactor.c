#include <stdio.h>
#include <math.h>

int isPrime(int x){
  for (int i = 2; i <= sqrt(x); i+=1){
    if (x % i == 0)
      return 0;
  }
  return 1;
}

long long biggestPrimeFactor(long long x){
    int max;
    for(int i = 1; i <= sqrt(x); i+=2){
      if (isPrime(i) && (x % i == 0))
        max = i;
    }
    return max;
}

int main(){
  long long bgf13195 = biggestPrimeFactor(600851475143);
  printf("BGF131195 = %lld", bgf13195);
  


  
  return 0;
}