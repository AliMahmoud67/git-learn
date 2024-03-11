def isValidMsg(msg):
    
    while True:
        if len(msg) <= 80:
            return msg
        else:
            msg = input("Please enter a messsage that doesn't exceeds 80 characters: ")

def isValidKey(msg):
    
    while True:
        if len(msg) <= 8 and msg.isalpha():
            return msg
        else:
            msg = input("Please enter a messsage that doesn't exceeds 8 characters and only alphabetic characters: ")

def isValidChoice(choice):
    
    while True:
        if choice == "1" or choice == "2" or choice == "3":
            return choice
        else:
            choice = input("Please choose a number from the menu: ")

def getFullKey(msg, key, temp):
    while True:
        if len(temp) > len(msg):
            temp = temp[:len(temp)-1]
        else:
            return temp


def encryption():
    print("---Welcome to our encryption program---")

    new_message = "" 

    message = isValidMsg(input("Enter the message you want to encrypt: ")).upper()

    keyword = isValidKey(input("Enter the keyword: ")).upper()

    tempKey = keyword*(((len(message))//(len(keyword)) + 1)) #message repeated

    fullKey = getFullKey(message, keyword, tempKey)

    for i in range(len(message)): #Due November 4
        asc_mes = ord(message[i])
        asc_key = ord(fullKey[i])
        new_asc = ((asc_key + asc_mes)%26) + 65
        
        if (asc_mes >= 65 and asc_mes <= 90):
            new_message += chr(new_asc)
        else:
            new_message += message[i]
    print(f"Your message after encryption is: {new_message}")



def decryption():
    print("---Welcome to our decryption program---")
    new_message = "" 

    message = isValidMsg(input("Enter the message you want to decrypt: ")).upper()

    keyword = isValidKey(input("Enter the keyword: ")).upper()

    tempKey = keyword*(((len(message))//(len(keyword)) + 1)) #message repeated

    fullKey = getFullKey(message, keyword, tempKey)

    for i in range(len(message)): #Due November 4
        asc_mes = ord(message[i])
        asc_key = ord(fullKey[i])
        new_asc = ((asc_mes - asc_key)%26) 
        
        if (asc_mes >= 65 and asc_mes <= 90):
            new_message += chr(new_asc + 65)
        else:
            new_message += message[i]
    print(f"Your original message is: {new_message}")



def main():
    print("-----Welcome to vigenere cipher program-----")
    while True:
        print("Choose What you want")
        print("1 -Encrypt a message\n2 -Decrypt a message\n3- Exit")
        choice = isValidChoice(input("Please choose a number from the menu: "))
        if choice == "1":
            encryption()
        elif choice == "2":
            decryption()
        elif choice == "3":
            exit()


main()




