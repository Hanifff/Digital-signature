from key_exchange import KeyExchanger
from global_paramters import public_numbers
import hashlib
import math


def fixed_hash(message, q):
    """ Fixed sized Hash value m for the elgamal DSS."""
    try:
        q =  q -1
        h = hashlib.sha3_256(message.encode("utf-8"))
        m = int(h.hexdigest(), 16) % q
        return m
    except Exception as e:
        print("Something went wrong: ",e.__str__())  
        return

def K(q):
    """ Compute the K for the elgamal DSS.
    Where,  1 =< K <= q-1, and gcd(K, q-1) = 1
    """
    try:
        reliatve_primes = []
        q = q-1
        K = 0
        for i in range(2,q):
            if q % i != 0:
                reliatve_primes.append(i)
        if len(reliatve_primes) > 0:
            K = reliatve_primes.pop() # take the last element as the number K
        return K
    except Exception as e:
        print("Something went wrong: ",e.__str__())  
        return

def S_1(g,k,q):
    """ Compute S1 for the elgamal DSS """
    try:
        s_1 = pow(g, k, q)
        return s_1
    except Exception as e:
        print("Something went wrong: ",e.__str__())  
        return

def k_invers( k,q):
    """ Compute the K invers mod q-1."""
    q = q-1
    k = k % q
    try:
        for i in range(1,q):
            if ((k * i) % q == 1): 
                return i 
        return 1
    except Exception as e:
        print("Something went wrong: ",e.__str__())  
        return 
    

def S_2(k_inv, m, private_key, s_1, q):
    """ Compute S1 for the elgamal DSS """ 
    try:
        q = q-1
        s_2 = (k_inv * (m - (private_key * s_1))) % q
        return s_2
    except Exception as e:
        print("Something went wrong: ",e.__str__())  
        return


def sign_message(g, q, private_key, message):
    """ Sign a messsage using the Elgamal DSS algorithm."""
    try:
        m = fixed_hash(message,q)
        k = K(q)
        s1 = S_1(g,k,q)
        k_inv = k_invers(k,q)
        s2 = S_2(k_inv, m, private_key, s1, q)
        signed = [s1,s2]
        print("\nThe hash value for this message is: {}, and the signature is: {}\n".format(m,signed))
        return signed
    except Exception as e:
        print("Something went wrong while signing the message, ",e.__str__())  
        return


def verify_signature(g, q, pu_Y, message, signature):
    """ Verify the signed message by comparing the original message's hash value and the recieved signed message.
        This function Returns True, Message if valid signature, otherwise it returns False,"". """
    try:
        m = fixed_hash(message,q)
        v_1 = pow(g ,m ,q)
        v_2 = (pow(pu_Y, int(signature[0])) * pow(int(signature[0]), int(signature[1]))) % q
        if v_1 == v_2:
            print("\nThe message with the signature: {}, is valid!\nV1 is {}, and V2 is {}\n".format(signature,v_1, v_2))
            return True
        else:
            print("\nNot valid for v1 {}, and v2 {}\n".format(v_1, v_2))
            return False
    except Exception as e:
        print("Something went wrong while verifying the signature, ",e.__str__())  
        return


# The sign_mes and verify_sign functions are used to test the Elgamal implementation
def sign_mes(g, q, private_key, m):
    k = K(q)
    s1 = S_1(g,k,q)
    k_inv = k_invers(k,q)
    s2 = S_2(k_inv, m, private_key, s1, q)
    signed = [s1,s2]
    return signed

def verify_sign(g, q, pu_Y, m, signature):
    v_1 = pow(g ,m ,q)
    v_2 = (pow(pu_Y, int(signature[0])) * pow(int(signature[0]), int(signature[1]))) % q
    if v_1 == v_2:
        print("validatian v1 is {}, and v2 is {}".format(v_1, v_2))
        return True
    else:
        print("Not valid for v1 {}, and v2 {}".format(v_1, v_2))
        return False
    