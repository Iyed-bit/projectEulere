#make function that converts numbers to letters:
#               1)takes a list that goes from zero to nine l1| a list that goes from #                                                            ten l2
#               to ninety | one hundred to nine hundred l3
#               2)loops from 0 to length of a string of that number - 1
#               3)if i == length - 1:
#                     *)s = l1[i]
#                 else if i == length - 2:
#                    *)s = l2[i] +"-" s
#                 else 
#                    *)s = l3[i] +" and "
#                 return s
#make function that counts number of letters in each number
#make main function that takes a starting and ending numbers as parameters and:
#                 1-loops through the numbers in range of ending and starting       #                  parameters
#                 2-checks to see if that number is inside a list already:
#                       *)if its already there:
#                             .) it takes the value from list[number]
#                      **)else 
#                               .)it converts it 
#                               ..)it counts the number of letters 
#                              ...)puts the value inside the list 
#                 3-adds the number to a result variable
l1 = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
l2 = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
l3 = [f"{number} hundred" for number in l1]
l4 = [f"{number} thousand" for number in l1]
ls = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
def convertNumberToLetters (number):
  s = str(number)
  i = 0
  lg = len(s)
  if (lg > 1 and s[-2] == "1"):
    if lg == 2:
      sc = ls[int(s[1])]
    elif lg == 3:
      sc = l3[int(s[0])] + " and " + ls[int(s[2])]
    elif lg == 4:
      sc = l4[int(s[0])] + " and " + l3[int(s[1])] + ls[int(s[2])]
  else:
    for i in range (lg-1,-1,-1):
      if i == lg-1:
        sc = l1[int(s[i])]
      elif i == lg-2:
        if sc == "zero" and s[-2] != "0":
            sc = l2[int(s[i])-1]
        elif s[-2]!="0":
            sc = l2[int(s[i])-1] + "-" + sc
      elif i == lg-3:
        if sc == "zero" and s[-3] != "0":
            sc = l3[int(s[i])]
        elif s[-3]!="0":
          sc =  l3[int(s[i])] + " and " + sc
      elif i == lg-4:
        if sc == "zero":
          sc = l4[int(s[i])]
        else:
          sc = l4[int(s[i])] + " and " + sc
  return sc

def countNumberOfLetters(numberString):
  s = 0
  for i in numberString:
    if i != " " and i!="-":
      s+=1
  return s 

def countTotalNumberOfLetters(l,h):
  total = 0
  for i in range (l, h+1):
    s = convertNumberToLetters(i)
    print(s);print(countNumberOfLetters(s))
    total += countNumberOfLetters(s)
  return total

l = int(input("Low: "))
h = int(input("High: "))
t = countTotalNumberOfLetters(l, h)
print(t) 

