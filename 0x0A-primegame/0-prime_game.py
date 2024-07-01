#!/usr/bin/python3
def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


def play_game(n, primes):
    moves = 0
    available = [True] * (n + 1)

    for prime in primes:
        if prime > n:
            break
        if available[prime]:
            moves += 1
            for multiple in range(prime, n + 1, prime):
                available[multiple] = False

    return moves % 2 == 1


# Example usage:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
