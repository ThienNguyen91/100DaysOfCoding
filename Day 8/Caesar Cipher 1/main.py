alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encypt(original_text, shift_amount):
    encrypted_text = ""
    for c in original_text:
        if c in alphabet:
            index = (alphabet.index(c) + shift_amount) % 26
            if c.isupper():
                encrypted_text += alphabet[index].upper()
            else:
                encrypted_text += alphabet[index]
        else:
            encrypted_text += c
    print(encrypted_text)



# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to temp the code and encrypt a
#  message.

encypt(text, shift)