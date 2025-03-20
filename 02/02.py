from typing import Callable
import re

# Parsing the numbers from the string using regex
def generator_numbers(text: str):
  pattern = r'\b(\d+(\.\d+)?)\b'
  for num in re.findall(pattern, text):
    yield num[0]

# Obtaining each element from the string using 
def sum_profit(text: str, func: Callable) -> int:
  total = 0

  for num in func(text):
    total += float(num)

  return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів. "
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")