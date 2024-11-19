a = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = bytes("python", "ascii")
print(type(a))  # <class 'bytes'>
print(type(b))  # <class 'bytes'>
print(a)  # b'\x01\x02\x03\x04\x05\x06\x07\x08\t'
print(b)  # b'python'
