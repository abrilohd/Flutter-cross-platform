cipher = 0x664181e200f0
key = 0xfffffffffffff000

decoded = cipher ^ key

print(hex(decoded))
print(decoded.to_bytes((decoded.bit_length() + 7) // 8, "big"))