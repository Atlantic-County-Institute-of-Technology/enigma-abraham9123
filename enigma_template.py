# author: Quinn Abraham
# created: 11-20-24
# last update:  11-25-24
import random

#were gonna use this translation
alphabet = "abcdefghijklmnopqrstuvwxyz"

# user puts in a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    message = (input("put in the stupid message you want me to encode bc u cant do it urself dummy"))
    key = int(input("input the key netta(leave blank for random)"))
    if key == "":
        key = random.randint(0,26)
    print(key)
    for x in range(len(message)):
        ordmessage = ord(message[x])
        ordmessage = ordmessage + key
        print(chr(ordmessage))
    # encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    pass

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
   pass


# main method declaration
def main():
    while True:
        print(f"welcome to the machine that encodes stuff\n"
              f"select a option before i 808:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode a file.\n"
              f"[3]: Decode a file.\n"
              f"[4]: exit(please pick this I dont wanna do this)")

        selection = input("pick an option bubba")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("peace slime")
            exit()
        else:
            print("ur choice is stupid do it until its not")

# runs on program start
if __name__ == "__main__":
    main()