pwd = b"password"
pwd_b_array = bytearray(pwd)

key = 5

for i, b in enumerate(pwd_b_array):
    pwd_b_array[i] = b + key

print(pwd_b_array)  # bytearray(b'ufxx|twi')

encrypted_pwd = bytes(pwd_b_array)
print(encrypted_pwd)  # b'ufxx|twi'


def encrypt(b_obj, key):
    b_obj_array = bytearray(b_obj)
    for i, b in enumerate(b_obj_array):
        n = b + key
        if n > 255:
            n -= 255
        b_obj_array[i] = n

    return bytes(b_obj_array)


result = encrypt(b"password", 5)
print(result)  # b'ufxx|twi'


def decrypt(b_obj, key):
    b_obj_array = bytearray(b_obj)
    for i, b in enumerate(b_obj_array):
        n = b - key
        if n < 0:
            n += 255
        b_obj_array[i] = n

    return bytes(b_obj_array)


result = encrypt(b"password", 200)
print(result)  # b'9*<<@8;-'
pwd = decrypt(result, 200)
print(pwd)  # b'password'

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    pwd_bytes = pwd.encode()
    encrypted_pwd = encrypt(pwd_bytes, 200)

    with open("password.txt", "wb") as file:
        file.write(encrypted_pwd)
    with open("password.txt", "rb") as file:
        encrypted_pwd = file.read()
        print(encrypted_pwd)
    print(decrypt(encrypted_pwd, 200))
