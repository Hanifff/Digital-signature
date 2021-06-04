from helpers import binaryToDecimal
import random
class KeyExchanger:
    """ KeyExchanger assigns the name of user, the gobal parameters g 
        and prime number q, the private, public, and shared key to each
        user that want to communicate though the channel. """
    def __init__(self ,name, g, q):
        self.name = name
        self.g = g # primitive root of the q
        self.q = q # large prime number
        self.private_key = self.set_private_key()

    def public_key(self):
        p_k = int(pow(self.g, self.private_key) % self.q)
        return p_k

    def set_private_key(self):
        """ Randomly set the private key."""
        self.private_key = random.randint(2,(self.q)-1)
        return self.private_key
    
    def __str__(self):
        return "\nThe global paramter g is {}, and the prime number p is {}.\n The  private key of {} is: {}, and his public key is: {}.\n"\
            .format(self.g, self.q ,self.name, self.private_key, self.public_key(), 
            self.name)

