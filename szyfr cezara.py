
     
def encrypt(message, key):
    encrypted = " "
    for letter in message:
        if letter.isalpha():  
            if letter.islower():
                if ord(letter) + key > ord('z'):
                    encrypted += chr(ord(letter) + key - 26)
                else:
                    encrypted += chr(ord(letter) + key)
            elif letter.isupper():
                if ord(letter) + key > ord('Z'):
                    encrypted += chr(ord(letter) + key - 26)
                else:
                    encrypted += chr(ord(letter) + key)
        else:
            encrypted += letter
    return encrypted
 
def main():
    print("Program do szyfrowania tekstu za pomocą szyfru Cezara")
    message = input("Podaj wiadomość do zaszyfrowania : ")
    key = int(input("Podaj klucz szyfrujący : "))
    encrypted_message = encrypt(message, key)
    print("Zaszyfrowana wiadomość:", encrypted_message)
 
if __name__ == "__main__":
    main()               