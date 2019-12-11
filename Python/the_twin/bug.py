import codecs

big, little = b'', b''
number = 0x486f727374


big += number.to_bytes(8, "big")
little += number.to_bytes(8, "little")

print(big, little)