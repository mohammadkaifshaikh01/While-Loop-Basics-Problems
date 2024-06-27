def EvenCount(num):
   count = 0
   i = 1
   while i <= num:
         if i % 2 == 0:
            count += i
         i += 1
   print(count)


num = 6
EvenCount(num)