"""
To use the python script in Command Prompt:
Write 'python your_file_name.py'
Example: 'python challenge201.py'
"""
# list containing the prime numbers 2 - 97
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# function that takes a list and a number
def isPrime(numbers, n):
    # the first index (0)
    first = 0
    # the last index (24)
    last = len(numbers)-1
    # variable set to False
    found = False
    # searches through the list from each end
    # while 0 is less-or-equal to 24 and not False
    while(first <= last and not found):
        # assigns the middle of the indexed value
        mid = (first + last)//2
        # if number from the list is equal to mid
        # it have found the number
        if numbers[mid] == n:
            # the number has been found
            found = True
        else:
            # if number is less than mid,
            if n < numbers[mid]:
                # subtract 1 from last (24-1 = 23)
                last = mid - 1
            else:
                # or add 1 to first (0+1 = 1)
                first = mid + 1
    # if not found
    if(found == False):
        found = "no"
    # if found
    else:
        found = "yes"
    print(found)

# function calls with arguments list and number
isPrime(primes, 3) # → "yes"
isPrime(primes, 4) # → "no"
isPrime(primes, 67) # → "yes"
isPrime(primes, 36) # → "no"