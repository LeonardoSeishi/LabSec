#Leonardo Seishi Yamazaki
#Challenge 3
#inspired by the article https://www.codementor.io/@arpitbhayani/deciphering-single-byte-xor-ciphertext-17mtwlzh30


#ghatered data from the Wikipedia version of frequency table 
#ETAOIN SHRDLU
frequencies = {
    'a': 0.08170, 'b': 0.01490, 'c': 0.02780, 'd': 0.04250, 'e': 0.12700, 
    'f': 0.02230, 'g': 0.02020, 'h': 0.06090, 'i': 0.06970, 'j': 0.00150,
    'k': 0.00770, 'l': 0.04020, 'm': 0.02410, 'n': 0.06750, 'o': 0.07510,
    'p': 0.01930, 'q': 0.00095, 'r': 0.05990, 's': 0.06330, 't': 0.09060,
    'u': 0.02760, 'v': 0.00980, 'w': 0.02360, 'x': 0.00150, 'y': 0.01970,
    'z': 0.00074,
}

scores = []

"""calculate the score by summing the differences between the frequencies in the frequency table 
and the frequency of the xored text characters, making the highest score the worst one"""
def scoring(xored_text):
    score = 0

    text = str(xored_text)
    text_size = len(text)

    for character, table_frequency in frequencies.items():
        """counting the amount of times each character appears
        to divide and findig the frequency of each letter of every "xored text" """

        true_frequency = text.count(character) / text_size

        difference = abs(table_frequency - true_frequency) #the lower the difference the more accurate to the "ETAOIN SHRDLU" frequency
        score += difference

    return score


#receive the text and the key and xor them byte to byte
def singlebyte_xor(bytes_text, key):
    xored_text = b""

    for byte in bytes_text:
        xored_text += bytes([byte ^ key])

    return xored_text


def testing_keys(text):

    bytes_text = bytes.fromhex(text)

    for key in range(256): #all the possibilities of keys
        xored_text = singlebyte_xor(bytes_text, key) #"xoring" the text with every key possible
        score = scoring(xored_text)                  
        scores.append(score)                         #putting the results in the list with all the scores

    return min(scores)

#getting the key of the lowest score in the list
def best_score_key(text):
    min_score = testing_keys(text) 
    for i, score in enumerate(scores):
        if score == min_score:
            text = singlebyte_xor(bytes.fromhex(text),i)
            return (f"key: {hex(i)}\nscore: {min_score:.5f}\ntext: {text}")



print(best_score_key("70656e61206465207068656f6e6978"))
print(best_score_key("7361627567756569726f"))
print(best_score_key("47656e65736973"))

print(testing_keys("7361627567756569726f"))
print(testing_keys("63617276616c686f"))

