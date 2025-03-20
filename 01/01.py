from typing import Callable

# Caching fibonacci that generates a fibonacci function that uses cache 
def caching_fibonacci() -> Callable[[int], list[int]]:
  fibonacci_cache = []

  # Fibonacci function that uses cache created in the generator
  def fibonacci(n: int) -> int:
    nonlocal fibonacci_cache

    # Checks if the passed instance is 0 or 1 and respectively populates the cache and returns the required value
    if n <= 0:
      if len(fibonacci_cache) <= n:
        fibonacci_cache.append(0)
      return fibonacci_cache[n]
    elif n == 1:
      if len(fibonacci_cache) <= 1:
        if len(fibonacci_cache) == 0:
          fibonacci_cache.append(0)
        fibonacci_cache.append(1)
      return fibonacci_cache[n]

    # Checks if the instance requested is in the cache otherwise populates cache and returns the required instance
    if n < len(fibonacci_cache):
      return fibonacci_cache[n]
    else:
      while len(fibonacci_cache) <= n:
        if len(fibonacci_cache) <= 1:
          if len(fibonacci_cache) == 0:
            fibonacci_cache.append(0)
          fibonacci_cache.append(1)
        fibonacci_cache.append(fibonacci_cache[len(fibonacci_cache) - 1] + fibonacci_cache[len(fibonacci_cache) - 2])
      return fibonacci_cache[n]

  return fibonacci

fibonacci_gen = caching_fibonacci()

print(fibonacci_gen(10))
print(fibonacci_gen(15))

