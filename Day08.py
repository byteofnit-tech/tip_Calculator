
# def greet():
#     print("Hello")
#     print("How do you do")
#     print("Isn't the weather is nice?")
# greet()

# # Functions that allows for inputs
# # name is called as parameter while Quack will called as argument.
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are u beta {name} ?")
# greet_with_name("Quack")

# #Functions with more than 1 input
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"Are u in {location}")
# # greet_with("Quack","Nowwhere")
# # greet_with("Nowwhere","Quack")

# greet_with(name="Angela",location="Delhi")




# # Caesar Cipher
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
# text = input("Type you message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# # TODO-1: Create a function called 'encrypt()' that takes 'original_text' and shifts_amount as 2 inputs
# # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards the alphabet by the shift_amount and print the encypted text.

# # hello 2
# def encrypt(original_text , shift_amount):
#     cipher_text = "" #j

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount # 7-> 9
#         cipher_text += alphabet[shifted_position] #j
#     print(f"Here is the encoded result: {cipher_text}")
# # TODO-4: What happens if u try to shift z forwards by 9? Can you fix the code?
# # TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be 
# encrypt(original_text = text, shift_amount = shift)





# Caesar Cipher
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
text = input("Type you message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and shifts_amount as 2 inputs
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards the alphabet by the shift_amount and print the encypted text.

# hello 2
def encrypt(original_text , shift_amount):
    cipher_text = "" #j

    # TODO-4: What happens if u try to shift z forwards by 9? Can you fix the code?
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount # 7-> 9
        shifted_position %= len(alphabet) #0-25 
        cipher_text += alphabet[shifted_position] #j
    print(f"Here is the encoded result: {cipher_text}")
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be 
encrypt(original_text = text, shift_amount = shift)




# Caesar Cipher
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
text = input("Type you message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text , shift_amount):
    cipher_text = "" 

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount # 7-> 9
        shifted_position %= len(alphabet) #0-25 
        cipher_text += alphabet[shifted_position] #j
    print(f"Here is the encoded result: {cipher_text}")


# TODO-01: Create a function called 'decrypt()' that takes 'original_text' and shifts amount by 2 inouts.
# TODO-02: Inside the 'decrypt()' function, shift each letter of the 'orignal_text' forwars the alphabet backwards  by the shift_amount and print the decrypted text.
def decrypt(original_text , shift_amount):
    output_text = "" 
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount # 7-> 9
        shifted_position %= len(alphabet) #0-25 
        output_text += alphabet[shifted_position] #j
    print(f"Here is the encoded result: {output_text}")


# TODO-03: Combine the 'encrypt()' and 'decrypt()' functions into one function called caesar().
# Use the value of the user chosen 'direction' variable to determine which functionality to use.
# Call the caeser function instead of encrypt/decrypt and pass in all three variables direction/text/shift.

def caesar(original_text ,shift_amount ,encode_or_decode):
    output_text = "" 
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        shifted_position = alphabet.index(letter) + shift_amount # 7-> 9
        shifted_position %= len(alphabet) #0-25 
        output_text += alphabet[shifted_position] #j
    print(f"Here is the encoded_or_decoded  result: {output_text}")

# decrypt(original_text = text , shift_amount = shift)
caeser(original_text = text , shift_amount = shift , encode_or_decode = direction)
