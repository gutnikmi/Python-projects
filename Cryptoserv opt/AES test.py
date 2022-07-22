from Crypto.Cipher import AES


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]
key = 'abcdefghijklmnop'
cipher = AES.new(key.encode(), AES.MODE_ECB)
msg = 'test'
msg = pad(msg)
msg = cipher.encrypt(msg.encode())
print(msg)

decipher = AES.new(key.encode(), AES.MODE_ECB)
print(unpad(decipher.decrypt(msg).decode()))



