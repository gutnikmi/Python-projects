import random


def randprime():
    p = 1
    q = 500
    primes = [i for i in range(p, q) if is_prime(i)]
    # print(primes)
    n = random.choice(primes)
    return n


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, r):
    for i in range(r):
        if (e * i) % r == 1:
            return i


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


def keygen():
    p = randprime()
    q = randprime()
    public, private = generate_keypair(p, q)
    return public, private


def rsa(msg, private):
    message = msg
    encrypted_msg = encrypt(private, message)
    emsg = ','.join(map(lambda x: str(x), encrypted_msg))
    emsg = emsg.encode()
    return emsg


def rsa_dec(pub, emsg):
    emsg = emsg.decode()
    emsg = emsg.split(",")
    emsg = list(map(int, emsg))
    res = decrypt(pub, emsg)
    return res


pub, pri = keygen()
emsg = rsa(input("say something \n"), pri)
dec = rsa_dec(pub, emsg)
print(dec)
