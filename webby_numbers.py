import pdb
from itertools import count, islice
import time


def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            if d  not in factors:
                factors.append(d)
            n /= d
        d = d + 1
    return factors


t1 = time.time()
def get_prime_by_index(index):
    req = [2, 3, 5]
    value_position = 0
    value = 1
    for i in islice(count(1), 10020200):
        if value_position < index:
            if i == 1 or i in req:
                value = i
                value_position += 1
            else:
                primes = prime_factors(i)
                #primes = get_primes(i)
                if primes:
                    temp = False
                    for ppp in primes:
                        if ppp not in req:
                            temp = False
                            break
                        else:
                            temp = True
                    if temp:
                        value = i
                        value_position += 1
        else:
            return value


if __name__ == "__main__":
    print(get_prime_by_index(500))


#def get_primes(counter):
#   #div = [ x for x in range(2,counter//2+1) if counter % x == 0 ]
#    div = [ x for x in islice(count(2),counter//2+1) if counter % x == 0 ]
#    primes = [ x1 for x1 in div if all( x1 % od != 0 for od in div if od != x1 )]
#    return primes


#def get_prime_by_index(index):
#    req = [2, 3, 5]
#    i = 1
#    value = 1
#    value_position = 0
#
#    while value_position < index:
#        if i == 1 or i in req:
#            value = i
#            value_position += 1
#        else:
#            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
#                pass
#            else:
#                primes = get_primes(i)
#                if primes:
#                    temp = False
#                    for ppp in primes:
#                        if ppp not in req:
#                            temp = False
#                            break
#                        else:
#                            temp = True
#                    if temp:
#                        value = i
#                        value_position += 1
#        i += 1
#    return value
#print (get_prime_by_index(200))

