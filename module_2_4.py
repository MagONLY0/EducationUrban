numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
is_prime = True
for i in range (2,len(numbers)+1):
    for j in range (2, i):
        if i % j == 0:
            not_primes.append(i)
            break
        else:
            primes.append(i)
            break

print ("Primes: ", set(primes))
print("Not_primes: ", set(not_primes))