a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

direction= "Do you want to encode or decode the message? "
plain= input("Enter the text you want to encode: \n ").lower()
shift= int(input("Enter the shifting key: \n "))

def encrypt(text, key):
    cipher_text=""
    for i in text:
        position= a.index(i)
        new_position= (position+key)%26
        new_letter= a[new_position]
        cipher_text= cipher_text+new_letter
    print(cipher_text)
        
encrypt(plain,shift)