n = int(input("Enter a number: "))
if n%2 == 0:
  print(n, "is even!")
  if n%4 == 0:
    print("And divisible by 4!")
  elif n%5 == 0:
    print("And multiple of 5!")
  elif n%10 == 0:
    print("And multiple of 10!")
else:
  print(n, "is odd!")
  if n > 1:
    for i in range(2,n):
      if (n % i) == 0:
        print(n,"is not a prime number")
        print(i,"times",n//i,"is",n)
        break
    else:
      print(n,"is a prime number")