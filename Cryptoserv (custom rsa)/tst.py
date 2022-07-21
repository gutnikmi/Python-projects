import rsa


def tst_rsa_lib():
    (pubkey, privkey) = rsa.newkeys(512)
    message = b'Hello Blablacode.ru!'
    crypto = rsa.encrypt(message, pubkey)
    message = rsa.decrypt(crypto, privkey)
    print(message)

if __name__ == "__main__":
    tst_rsa_lib()