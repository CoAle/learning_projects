def encrypt_decrypt_choice():
  choice = (input("Enter 'E' to encrypt or 'D' to decrypt:\n"))
  if choice == 'E' or choice == 'e':
    input_text = input('Please enter the text you want to encrypt:\n')
    shift = int(input('By how many letters do you want to shift it?\n'))
    encrypt_text(input_text, shift)
  elif choice == 'D' or choice == 'd':
    input_text = input('Please enter the text you want to decrypt:\n')
    shift = int(input('Please enter the key:\n'))
    decrypt_text(input_text, shift)
  else:
    print('Please enter a valid choice\n')
    encrypt_decrypt_choice()

def encrypt_text(input_text, shift):
  encrypted_text = ""
  new_c = ''
  for c in input_text:
    if c.isupper():
      new_index = ((ord(c) - ord('A')) + shift) % 26
      new_c = chr(new_index + ord('A'))
      encrypted_text += new_c
    elif c.islower():
      new_index = ((ord(c) - ord('a')) + shift) % 26
      new_c = chr(new_index + ord('a'))
      encrypted_text += new_c
    else:
      encrypted_text += c
  print(encrypted_text)

def decrypt_text(input_text, shift):
  decrypted_text = ""
  new_c = ''
  for c in input_text:
    if c.isupper():
      new_index = ((ord(c) - ord('A')) - shift) % 26
      new_c = chr(new_index + ord('A'))
      decrypted_text += new_c
    elif c.islower():
      new_index = ((ord(c) - ord('a')) - shift) % 26
      new_c = chr(new_index + ord('a'))
      decrypted_text += new_c
    else:
      decrypted_text += c
  print(decrypted_text)

encrypt_decrypt_choice()