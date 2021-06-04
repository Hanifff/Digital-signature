from key_exchange import KeyExchanger
from global_paramters import public_numbers

# Generate the prime nr q and the generator g
q, g = public_numbers(1000)
# Generate dynimaically a private key, a public key for each user as a DHKeyexchange algorithm. 
ALICE = KeyExchanger('Alice', g=g, q=q)
BOB = KeyExchanger('Bob', g=g, q=q)
