def naturals(n):
	yield n
	yield from naturals(n+1)

nat = naturals(541)
primes = []
def sieve(nat):
	n = next(nat)
	yield n 
	yield from sieve(i for i in nat if i%n!=0)

p = sieve(nat)
for i in range(100):
	primes.append(next(p))
print(primes)