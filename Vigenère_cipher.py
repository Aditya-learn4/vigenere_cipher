
text1 = 'Python is awesome'
text2 = 'wyiwmp wv ijkzobt'

#custom_key = 'python'
#custom_key = 'gnidocyppah'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
            
            #Append any non-letter character to the message
            if not char.isalpha():
                final_message += char
            #print(encrypted_text)
            else:
                # Find the right key character to encode
                    #print('key_index:', key_index, 'length:', len(key))
                key_char = key[key_index % len(key)]
                    #print('key_char:', key_char)
                key_index += 1

                # Define the offset and the encrypted letter
                offset = alphabet.index(key_char)
                    #print('offset:', offset)
                    #print('ori:', char)
                index = alphabet.find(char)
                    #print('index:', index)
                new_index = (index + offset * direction) % len(alphabet)
                    #print('new_index:', new_index)
                    #print('encrypt:', alphabet[new_index])
                final_message += alphabet[new_index] 

    return final_message

    #print('encrypted text:', encrypted_text)

def encrypt(message, key):
     return vigenere(message, key)

def decrypt(message, key):
     return vigenere(message, custom_key, -1)

print('1st encryption:', text1, '\n')
print('2nd encryption:', text2, '\n')
print(f'Key: {custom_key}')

encryption = encrypt(text1, custom_key)
print('\nencrypted text:', encryption)

decryption = decrypt(text2, custom_key)
print(f'decrypt: {decryption}\n')