import sys

def left_shift(bits, shift):
    return bits[shift:] + bits[:shift]

def xor_bit(c0,c1, block_length = 8):
    """ This function XOR the expansion permutated L-block with the sk."""
    xor_ep_sk = ""
    for i in range(block_length):
        if (c0[i] == c1[i]):  
            xor_ep_sk += "0"
        else:  
            xor_ep_sk += "1"
    return xor_ep_sk


def convert_to_txt(bits, encoding='utf-8', errors='surrogatepass'):
    """This function converts the decrypted messages from bits to bytes."""
    try:
        n = int(bits, 2)
        enc = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
        return True, enc
    except Exception as e:
        return False, e
        
def convert_txt_bits(txt):
    """ converts byte to bits """
    bits =  ''.join(bin(ord(c)) for c in txt).replace('b','')
    return bits

def read_f(file_name):
    """Read the file which contains the cipher text."""
    cipher_txt = ""
    try:
        with open(file_name, "r") as cipher:
            cipher_txt = cipher.read()
    except IOError:
        return "Could not find the file!"
    finally:
        cipher.close()
    return cipher_txt


def read_remove_spaces(filename):
    """This function removes spaces from the cipher text. """
    enciphered_txt = read_f(filename)
    enciphered_txt = enciphered_txt.replace(" ", "")
    return enciphered_txt

def write_file(file_name, txt):
    """This function writes the encypted text to a file """
    cipher_txt = ""
    try:
        with open(file_name, "a") as cipher: 
            cipher_txt = cipher.write(txt +'\n')
        if cipher_txt != len(txt):
            return "Something went wrong!"
    except IOError:
        return "Could not find the file!"
    finally:
        cipher.close()
    return "Successfully wrote the cipher text to the file"

  
def binaryToDecimal(b): 
    """ This function is only used to log the secret key in decimal format.""" 
    sec_dec = ""
    if b != None:
        sec_dec = int(str(b),2)
    else:
        sec_dec = "Not set yet!"
    return sec_dec