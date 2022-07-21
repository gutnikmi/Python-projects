import random


# def randprime():
#     p = 500
#     q = 1000
#     primes = [i for i in range(p, q) if is_prime(i)]
#     n = random.choice(primes)
#     return n


def randprime():
    ss = 35
    maxx = 1000
    rb = random.randrange(ss, maxx)
    lb = rb - 50
    primes = [i for i in range(lb, rb) if is_prime(i)]
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
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


def keygen():
    p = randprime()
    q = randprime()
    public, private = generate_keypair(p, q)
    return public, private


def rsa(msg, public):
    message = msg
    encrypted_msg = encrypt(public, message)
    emsg = ','.join(map(lambda x: str(x), encrypted_msg))
    emsg = emsg.encode()
    return emsg


def rsa_dec(private, emsg):
    emsg = emsg.decode()
    emsg = emsg.split(",")
    emsg = list(map(int, emsg))
    res = decrypt(private, emsg)
    return res


def test_rsa():
    pub, pri = keygen()
    print(pub, pri)
    emsg = rsa("test", pub)
    dec = rsa_dec(pri, emsg)
    print(dec)


if __name__ == "__main__":
    test_rsa()
