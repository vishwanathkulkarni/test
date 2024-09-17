for i in range(10):
  print("hello")

def fib(n):
  if n==0:
    return 0
  if n==1 or n==2:
    return 1
  return fib(n-1)+fib(n-2)

print(fib(5))
print(fib(6))
print(fib(1))
