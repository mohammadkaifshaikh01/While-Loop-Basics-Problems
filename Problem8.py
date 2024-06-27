def oddCount(N):
   count  = 0
   i = 1
   while i <= N:
      if i % 2 != 0:
         count += i
      i += 1
   print(count)





N = 7
oddCount(N)