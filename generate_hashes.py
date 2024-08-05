import hashlib

password = "rabia_please_mujay_chordo"
hash = hashlib.sha256(password.encode('utf-8'))
print(hash.hexdigest())


# this code is used to convert Passwords into Hashes