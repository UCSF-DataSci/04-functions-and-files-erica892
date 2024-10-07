#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def generate_fib_sequence(limit):
    fib_sequence = []
	a, b = 0, 1
	while a < limit:
		fib_sequence.append(a)
		a, b = b, a + b

    return fib_sequence

def main():
	parser = argparse.ArgumentParser(description = "Generate the Fibonacci numbers less than a limit and write them to a file.")
	parser.add_argument("limit", type = int, help = "Upper limit for Fibonacci numbers.")
	parser.add_argument("output_file", type = str, help = "Output file name.")

	args = parser.parse_args()
	limit = args.limit
	output_file = args.output_file

fibonacci_numbers = generate_fib_sequence(limit)

try:
        with open(output_file, 'w') as file:
            for num in fibonacci_numbers:
                file.write(f"{num}\n")
        print(f"Fibonacci numbers below {limit} have been written to {output_file}.")
    
    except IOError as e:
        print(f"Error occurred while writing to the file: {e}")


if __name__ == "__main__":
    main()