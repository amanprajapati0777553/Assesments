import math


def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
   return  n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def mod(n1, n2):
    return n1 % n2
def power(n1, n2):
    return n1 ** n2
def sqrt(n1):
    return n1 ** 0.5
def log(n1, base):
    return math.log(n1, base)
def sin(n1):
    return math.sin(n1)
def cos(n1):
    return math.cos(n1)
def tan(n1):
    return math.tan(n1)
def factorial(n1):
    return math.factorial(n1)
def radians(n1):
    return math.radians(n1)
def degrees(n1):
    return math.degrees(n1)
def exp(n1):
    return math.exp(n1)
def ceil(n1):
    return math.ceil(n1)
def floor(n1):
    return math.floor(n1)
def gcd(n1, n2):
    return math.gcd(n1, n2)
def lcm(n1, n2):
    return abs(n1 * n2) // math.gcd(n1, n2)
def is_prime(n1):
    if n1 <= 1:
        return False
    for i in range(2, int(math.sqrt(n1)) + 1):
        if n1 % i == 0:
            return False
    return True
def fibonacci(n1):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n1:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n1]
def is_even(n1):
    return n1 % 2 == 0
def is_odd(n1):
    return n1 % 2 != 0
def absolute(n1):
    return abs(n1)
# def round_number(n1):
#     return round(n1)
# def max_number(n1, n2):
#     return max(n1, n2)
# def min_number(n1, n2):
#     return min(n1, n2)
# def average(numbers):
#     return sum(numbers) / len(numbers)
# def variance(numbers):
#     mean = average(numbers)
#     return sum((x - mean) ** 2 for x in numbers) / len(numbers)
# def standard_deviation(numbers):
#     return math.sqrt(variance(numbers))
# def median(numbers):
#     sorted_numbers = sorted(numbers)
#     n = len(sorted_numbers)
#     mid = n // 2
#     if n % 2 == 0:
#         return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
#     else:
#         return sorted_numbers[mid]
# def mode(numbers):
#     frequency = {}
#     for num in numbers:
#         frequency[num] = frequency.get(num, 0) + 1
#     max_freq = max(frequency.values())
#     modes = [num for num, freq in frequency.items() if freq == max_freq]
#     return modes
# def percentile(numbers, percent):
#     sorted_numbers = sorted(numbers)
#     index = (len(sorted_numbers) - 1) * percent / 100
#     lower = math.floor(index)
#     upper = math.ceil(index)
#     if lower == upper:
#         return sorted_numbers[int(index)]
#     else:
#         return (sorted_numbers[lower] + sorted_numbers[upper]) / 2

# def combinations(n1, n2):
#     if n2 > n1:
#         return 0
#     return math.factorial(n1) // (math.factorial(n2) * math.factorial(n1 - n2))
# def permutations(n1, n2):
#     if n2 > n1:
#         return 0
#     return math.factorial(n1) // math.factorial(n1 - n2)
# def fibonacci_recursive(n1):
#     if n1 <= 0:
#         return []
#     elif n1 == 1:
#         return [0]
#     elif n1 == 2:
#         return [0, 1]
#     else:
#         fib_sequence = fibonacci_recursive(n1 - 1)
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#         return fib_sequence
# def is_palindrome(n1):
#     return str(n1) == str(n1)[::-1]
# def collatz_sequence(n1):
#     sequence = [n1]
#     while n1 != 1:
#         if n1 % 2 == 0:
#             n1 //= 2
#         else:
#             n1 = 3 * n1 + 1
#         sequence.append(n1)
#     return sequence
# def sum_of_digits(n1):
#     return sum(int(digit) for digit in str(n1))
# def reverse_number(n1):
#     return int(str(n1)[::-1])
# def is_perfect_square(n1):
#     return int(math.sqrt(n1)) ** 2 == n1
# def is_perfect_cube(n1):
#     return int(round(n1 ** (1/3))) ** 3 == n1
# def is_armstrong(n1):
#     num_str = str(n1)
#     num_len = len(num_str)
#     return n1 == sum(int(digit) ** num_len for digit in num_str)
# def is_leap_year(n1):
#     return (n1 % 4 == 0 and n1 % 100 != 0) or (n1 % 400 == 0)
# def is_palindrome_string(s):
#     return s == s[::-1]
# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)
# def is_substring(s1, s2):
#     return s1 in s2
