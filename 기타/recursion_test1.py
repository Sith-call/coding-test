import time
import sys
sys.setrecursionlimit(10**8)

cache = dict()

def factorial(n):
    if n in cache:
        return cache[n]
    elif n <= 1:
        cache[n] = 1
        return 1
    else:
        result = n * factorial(n - 1)
        cache[n] = result
        return result

def main():
    test_values = [10, 50, 100, 500, 1000, 2000]  # decrease this number if you get recursion error

    for n in test_values:
        cache.clear()  # Clear cache

        start_no_cache = time.time()
        result_no_cache = factorial(n)
        end_no_cache = time.time()

        print(f"Without cache, factorial({n}) took {end_no_cache - start_no_cache:.5f} sec")

        start_with_cache = time.time()
        result_with_cache = factorial(n)
        end_with_cache = time.time()

        print(f"With cache, factorial({n}) repeated took {end_with_cache - start_with_cache:.5f} sec\n")


if __name__ == "__main__":
    main()

"""
    Without cache, factorial(10) took 0.00000 sec
    With cache, factorial(10) repeated took 0.00000 sec
    
    Without cache, factorial(50) took 0.00001 sec
    With cache, factorial(50) repeated took 0.00000 sec
    
    Without cache, factorial(100) took 0.00002 sec
    With cache, factorial(100) repeated took 0.00000 sec
    
    Without cache, factorial(500) took 0.00017 sec
    With cache, factorial(500) repeated took 0.00000 sec
    
    Without cache, factorial(1000) took 0.00056 sec
    With cache, factorial(1000) repeated took 0.00000 sec
    
    Without cache, factorial(2000) took 0.00206 sec
    With cache, factorial(2000) repeated took 0.00000 sec
"""
