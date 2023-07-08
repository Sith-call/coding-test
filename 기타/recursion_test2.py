import time


cache = {}


def fib_without_cache(n):
    if n <= 1:
        return n
    else:
        return fib_without_cache(n - 1) + fib_without_cache(n - 2)


def fib_with_cache(n):
    if n in cache:
        return cache[n]
    elif n <= 1:
        result = n
    else:
        result = fib_with_cache(n - 1) + fib_with_cache(n - 2)

    cache[n] = result
    return result


def main():
    start_with_cache = time.time()
    print(fib_with_cache(30))  # Adjust this number if it takes too long
    end_with_cache = time.time()
    print(f"With cache, fib(30) took {end_with_cache - start_with_cache:.5f} sec")

    start_without_cache = time.time()
    print(fib_without_cache(30))  # Adjust this number if it takes too long
    end_without_cache = time.time()
    print(f"Without cache, fib(30) took {end_without_cache - start_without_cache:.5f} sec\n")


if __name__ == "__main__":
    main()

"""
    832040
    With cache, fib(30) took 0.00002 sec
    832040
    Without cache, fib(30) took 0.09575 sec
"""
