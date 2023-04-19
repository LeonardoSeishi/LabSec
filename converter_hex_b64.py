#Leonardo Seishi Yamazaki
#Challenge 1

#biblioteca python que manipula strings base64 e hex codificando e decodificando em raw bytes
#native python library that manipulates base64 and hex coding and decoding into raw bytes
from base64 import b64encode, b16decode

def convert(string_hexadecimal):
    raw_bytes = b16decode(string_hexadecimal, casefold=True)    #reading the string as a hexadecimal variable and transforming into raw bytes
    base_64 = b64encode(raw_bytes)                               #transforming raw bytes in base64
    return base_64


print(convert("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))