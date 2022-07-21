import rsa


# def tst_rsa_lib():
(pubkey, privkey) = rsa.newkeys(512)
a = pubkey.save_pkcs1(format='DER')
# print(a)
b = rsa.key.PublicKey.load_pkcs1(a, format='DER')
message = b'Hello Blablacode.ru!'
crypto = rsa.encrypt(message, b)
message = rsa.decrypt(crypto, privkey)
print(message.decode())


# if __name__ == "__main__":
#     tst_rsa_lib()
