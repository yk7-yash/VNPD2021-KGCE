def print_factors(x):
   print("The factors of",x,"are:")
   arr=[]
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           if (i % 2==0):
             arr.append(i)
   print(arr)
   result=1
   for a in arr:
         result = result * a
   print(result)
   
num = int(input())
if (num<10):
  print("Invalid Number")
else:
  print_factors(num)
