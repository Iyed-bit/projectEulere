def fact(x):
  res = 1
  for i in range (2, x +1):
    res *= i 
  return res
def permutationsNumber(gridValue):
  return int(fact(gridValue*2)/(fact(gridValue)*fact(gridValue)))

print(permutationsNumber(20))