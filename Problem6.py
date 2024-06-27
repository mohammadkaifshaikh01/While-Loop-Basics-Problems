def FizzBuzz(N):
   i = 1
   while i <= N:
         if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
         elif i % 3 == 0:
            print("Fizz")
         elif i % 5 == 0:
            print("Buzz")
         else:
            print(i)
         i+=1
    

test = int(input())
for _ in range(test):
   N = int(input())
   FizzBuzz(N)