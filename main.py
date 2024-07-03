alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        pos = alphabet.index(letter)
        n_pos = pos + shift_amount
        cipher_text+=alphabet[n_pos]
    print(f"The encoded text is {cipher_text}")
        

def decrypt(cipher_text, shift_amount):
    plain_t = ""
    for letter in cipher_text:
        pos = alphabet.index(letter)
        n_pos = pos - shift_amount
        plain_t+=alphabet[n_pos]
    print(f"The decoded text is{plain_t}")
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
      decrypt(cipher_text=text, shift_amount=shift)
    
  