def main():
    
    n = int(input())
    print(get_sieve(n))
    
def get_sieve(n):
    no_primes = []
    
    n_arr = list(range(2,n+1))
    for i in range(int(len(n_arr)**0.5)):
        for j in range(i + 1, len(n_arr)):
            if n_arr[j] % n_arr[i] == 0 and n_arr[j] not in no_primes:
                no_primes.append(n_arr[j])
    print(no_primes)
    return [x for x in n_arr if x not in no_primes]
main()