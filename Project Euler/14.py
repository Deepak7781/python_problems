'''
Max_N = 5*(10**6)

def collatz(n):
    seq = [n]
    if n ==1:
        return seq
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = (3*n)+1
        seq.append(n)
    return seq

def longest_seq(n):
    maxi = 0
    num = None
    i = 1
    while i<=n:
        a = collatz(i)
        #print(a)
        if len(a) >= maxi:
            #print(len(a))
            maxi = len(a)
            num = i
        i += 1
    
    return num

'''
'''
def collatz_length(n, cache):
    original_n = n
    length = 0

    # Generate the sequence and use the cache for memoization
    while n != 1:
        if n < len(cache) and cache[n] != 0:
            length += cache[n]
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    
    # Store the computed sequence length in cache
    if original_n < len(cache):
        cache[original_n] = length + 1  # Add 1 for the starting number itself
    
    return length + 1

def longest_seq(limit):
    # Initialize a cache for memoization
    cache = [0] * (limit + 1)
    cache[1] = 1  # Base case: the sequence for 1 is of length 1

    max_length = 0
    num_with_max_seq = 1

    # Loop through all numbers up to the limit
    for i in range(2, limit):
        length = collatz_length(i, cache)

        if length > max_length:
            max_length = length
            num_with_max_seq = i

    return num_with_max_seq

# Find the number under 1,000,000 that produces the longest Collatz sequence
print(longest_seq(1000000))

'''
'''
def collatz_length(n):
    length = 1  # Start with 1 to count the initial number itself

    while n != 1:
        if n & 1:  # If n is odd (same as n % 2 != 0)
            n = 3 * n + 1
        else:  # If n is even (same as n % 2 == 0)
            n = n // 2
        length += 1
    
    return length

def longest_seq(limit):
    max_length = 0
    num_with_max_seq = 1

    # Loop through all numbers up to the limit
    for i in range(1, limit):
        length = collatz_length(i)

        if length > max_length:
            max_length = length
            num_with_max_seq = i

    return num_with_max_seq

# Find the number under 1,000,000 that produces the longest Collatz sequence
print(longest_seq(1000000))
'''
'''def collatz_length(n, cache):
    original_n = n
    length = 0

    # Compute the length of the Collatz sequence, using cache to store results
    while n != 1:
        if n in cache:
            length += cache[n]
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1

    # Cache the result for the original number
    cache[original_n] = length + 1  # Add 1 to count the starting number

    return length + 1

def longest_seq(limit):
    cache = {1: 1}  # Initialize cache with base case for 1
    max_length = 0
    num_with_max_seq = 1

    # Loop through all numbers up to the limit
    for i in range(1, limit):
        length = collatz_length(i, cache)

        if length > max_length:
            max_length = length
            num_with_max_seq = i

    return num_with_max_seq

# Find the number under 1,000,000 that produces the longest Collatz sequence
print(longest_seq(5000000))'''


'''
def countChain(n, values):
    if n in values:
        return values[n]
    if n % 2 == 0:
        values[n] = 1 + countChain(n//2,values)
    else:
        values[n] = 2 + countChain((3*n+1)//2, values)
    return values[n]

longest_chain = 0
answer = -1

values = {1:1}

for num in range(1, 5*10**6):
    if countChain(num, values) > longest_chain:
        longest_chain = countChain(num, values)
        answer = num

print(answer)

def collatz_sequence(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        result = 1 + collatz_sequence(n // 2, memo)
    else:
        result = 1 + collatz_sequence(3 * n + 1, memo)
    memo[n] = result
    return result

def longest_collatz_sequence(limit):
    longest_sequence = 0
    longest_sequence_start = 0
    for i in range(1, limit):
        sequence_length = collatz_sequence(i)
        if sequence_length > longest_sequence:
            longest_sequence = sequence_length
            longest_sequence_start = i
    return longest_sequence_start

print(longest_collatz_sequence(1000000))

'''
'''
def collatz_length(n, cache):
    original_n = n
    length = 0

    # Iterate through the sequence, using cache for memoization
    while n != 1:
        if n < len(cache) and cache[n] != 0:  # Check if already in cache
            length += cache[n]
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1

    # Cache the length for the original number
    if original_n < len(cache):
        cache[original_n] = length + 1

    return length + 1

def longest_seq(limit):
    # Initialize cache for memoization
    cache = [0] * (limit + 1)
    cache[1] = 1  # Base case: 1 has a Collatz sequence of length 1

    max_length = 0
    num_with_max_seq = 1

    # Loop through only odd numbers (skip even numbers as their sequences are covered)
    for i in range(1, limit, 2):  # Skip even numbers
        length = collatz_length(i, cache)

        if length > max_length:
            max_length = length
            num_with_max_seq = i

    return num_with_max_seq

# Set the limit to 5 million and compute the result
print(longest_seq(5000000))
'''

'''
import sys

cache_limit = 5000001
results = [0] * cache_limit  
longest_number = [0] * cache_limit  
results[0] = 1 

def create_sequence(starting_number):
    if starting_number < cache_limit and results[starting_number] != 0:
        return results[starting_number]
    else:
        result = 0
        if starting_number % 2 == 0:
            result = 1 + create_sequence(starting_number >> 1)
        else:
            result = 1 + create_sequence(3 * starting_number + 1)

        if starting_number < cache_limit:
            results[starting_number] = result

        return result

max_length = 1 
for i in range(1, cache_limit):
    sequence_length = create_sequence(i)
    
   
    if sequence_length >= max_length:
        max_length = sequence_length
        longest_number[i] = i
    else:
        longest_number[i] = longest_number[i - 1]

# Read input
t = int(input("Enter test cases").strip())  # Number of test cases
for a0 in range(t):
    n = int(input("Enter n").strip())
    
    # Output the number that generates the longest Collatz sequence up to n
    print(longest_number[n])
'''
'''
cache_limit = 5000001
results = [0] * cache_limit  # To store the Collatz sequence lengths
longest_number = [0] * cache_limit  # To store the number with the longest sequence
results[1] = 1  # Base case: sequence length of 1 for number 1

def create_sequence(starting_number):
    original_number = starting_number
    length = 0
    sequence = []

    # Iterate until we find a number already in cache
    while starting_number >= cache_limit or results[starting_number] == 0:
        sequence.append(starting_number)
        if starting_number % 2 == 0:
            starting_number //= 2
        else:
            starting_number = 3 * starting_number + 1
        length += 1

    # The length of the Collatz sequence for the current number is the cached value plus the number of steps
    length += results[starting_number]

    # Store the results in the cache for each number in the sequence
    for idx, num in enumerate(reversed(sequence)):
        if num < cache_limit:
            results[num] = length - idx

    return length

# Precompute the Collatz sequence lengths and the number with the longest sequence
max_length = 1  # Max length starts at 1 for number 1
longest_number[1] = 1  # For number 1, the longest number is 1
for i in range(2, cache_limit):
    sequence_length = create_sequence(i)
    
    # Update the number that gives the longest sequence for each `i`
    if sequence_length > max_length:
        max_length = sequence_length
        longest_number[i] = i
    else:
        longest_number[i] = longest_number[i - 1]

# Read input
t = int(input().strip())  # Number of test cases
for a0 in range(t):
    n = int(input().strip())
    
    # Output the number that generates the longest Collatz sequence up to n
    print(longest_number[n])
'''
'''
Max_N = 5*(10**6)
longest_num = [0] * Max_N
longest_num[1] = 1

def collatz(n):
    seq = [n]
    if n ==1:
        return seq
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = (3*n)+1
        seq.append(n)
    return seq

def longest_seq(n):
    maxi = 0
    num = None
    i = 1
    while i<=n:
        a = collatz(i)
        #print(a)
        if len(a) >= maxi:
            #print(len(a))
            maxi = len(a)
            num = i
        i += 1
    
    return num

for i in range(2, Max_N):
    longest_num[i] = longest_seq(i)

print(longest_num[10])
'''
cache_limit = 5000001
results = [0] * cache_limit  
longest_number = [0] * cache_limit
results[1] = 1 

def create_sequence(starting_number):
    original_number = starting_number
    sequence = []  

    while starting_number >= cache_limit or results[starting_number] == 0:
        sequence.append(starting_number)
        if starting_number % 2 == 0:
            starting_number //= 2
        else:
            starting_number = 3 * starting_number + 1

    
    length = results[starting_number]

    
    for i, num in enumerate(reversed(sequence)):
        if num < cache_limit:
            results[num] = length + i + 1  
    return length + len(sequence)  


max_length = 1 
longest_number[1] = 1  
for i in range(2, cache_limit):
    sequence_length = create_sequence(i)
    
    
    if sequence_length >= max_length:
        max_length = sequence_length
        longest_number[i] = i
    else:
        longest_number[i] = longest_number[i - 1]


n = int(input("Enter the num :"))
print(longest_number[n])