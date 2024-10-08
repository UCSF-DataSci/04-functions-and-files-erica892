#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

import argparse
from fibonacci import fibonacci

# First create a function to check if a number is prime.
def prime(n):
	if n <= 1:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

# Next step up the agument parser.
def main():
	parser = argparse.ArgumentParser(description = "Find the largest prime Fibonacci number less than the limit.")
	parser.add_argument("limit", type=int, help="Upper limit for Fibonacci numbers.")

	args = parser.parse_args()
	limit = args.limit

# Next generate the Fibonacci numbers less than the limit.
	fibonacci_numbers = fibonacci(limit)

# Next find the prime numbers from the sequence generated above.
	prime_fib = [num for num in fibonacci_numbers if prime(num)]

# Next find the largest prime number.
	if prime_fib:
		largest_prime = max(prime_fib)
		print(f"The largest prime Fibonacci number below {limit} is: {largest_prime}.")
	else:
		print(f"There are no prime Fibonacci numbers below {limit}.")

if __name__ == "__main__":
	main()