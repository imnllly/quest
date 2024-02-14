def encode(word, shift):
    encoded_word = ''
    for i in range(0, len(word)):
        encoded_word = encoded_word + chr(ord(word[i]) + shift + i)
    return encoded_word

def decode(encoded_word, shift):
    decoded_word = ''
    for i in range(0, len(encoded_word)):
        decoded_word = decoded_word + chr(ord(encoded_word[i]) - i - shift)
    return decoded_word