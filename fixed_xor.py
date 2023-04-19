#Leonardo Seishi Yamazaki
#Challenge 2

def fixedXor(str_hex1, str_hex2):
    hex1 = int(str_hex1, 16)        #transformando as strings hexadecimais em "inteiros" de base 16
    hex2 = int(str_hex2, 16)        #para possibilitar a operação ^ (xor) do python 
    xor = str(hex(hex1^hex2))            #voltando o valor para hexadecimal
    return xor

print(fixedXor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))