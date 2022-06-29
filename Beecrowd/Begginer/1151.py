cache = {0:0,1:1}


def fibonacci(n):
    if n in cache:
      return cache[n]
    else:
        cache[n] = (fibonacci(n-1)+fibonacci(n-2))
        return cache[n]

n = int(input())

fibonacci(n)

for i in range(n):
  if i == n-1:
    print(cache[i])
  else:
    print(cache[i],end=" ")