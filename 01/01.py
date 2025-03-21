from typing import Callable

# Caching fibonacci that generates a fibonacci function that uses cache 
def caching_fibonacci() -> Callable[[int], list[int]]:
  fibonacci_cache = []

  # Fibonacci function that uses cache created in the generator
  def fibonacci(n: int) -> int:
    nonlocal fibonacci_cache

    # Adding the first two fibonacci elelemts as a starter for the generator
    if len(fibonacci_cache) <= 1:
      if len(fibonacci_cache) == 0:
        fibonacci_cache.append(0)
      fibonacci_cache.append(1)

    # Checks if the instance requested is in the cache otherwise populates cache and returns the required instance
    if n < len(fibonacci_cache):
      return fibonacci_cache[n]
    else:
      while len(fibonacci_cache) <= n:
        fibonacci_cache.append(fibonacci_cache[len(fibonacci_cache) - 1] + fibonacci_cache[len(fibonacci_cache) - 2])
      return fibonacci_cache[n]

  return fibonacci

fibonacci_gen = caching_fibonacci()

print(fibonacci_gen(0))
print(fibonacci_gen(1))
print(fibonacci_gen(2))
print(fibonacci_gen(10))
print(fibonacci_gen(15))

