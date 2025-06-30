import random
import string
import time
key_list = []
a = 0

def gen_key():
    global a
    key = a + 1
    a+=1
    return str(key)+random.choice(string.ascii_letters)

while 1 :
    print("\n------------------ 💀 ZeeCoDe 💀 -----------------\n")
    print(f" 💠 For Encryption press e\n 💠 For Decryption press d\n 💠 For {"exit".center(10)} press q \n")
    user_choice = input("↪️ What you want Encryption  or Decryption data : ").lower()
    if user_choice == 'e':
        user_input_string = input('↪️ Enter data which you want to encrypt : ')
        encode_list = []
        if len(user_input_string)>3:
            words = user_input_string.split()

            for word in words :
                x = random.choice(string.digits)
                y = random.choice(string.ascii_letters)
                z = random.choice(string.punctuation)
                new_str  = y + x + z + word[-1] + word[1:-1] + word[0] +x+y+z
                encode_list.append(new_str)
        else :
            x = random.choice(string.digits)
            y = random.choice(string.ascii_letters)
            z = random.choice(string.punctuation)
            new_str =x+z+y + user_input_string[::-1]+z+y+x
            encode_list.append(new_str)
        print(' '.join(encode_list))
        key = gen_key()
        key_list.append(key)
        print(f'-- > Note  the generated key 🔑 : {key} ')
    elif user_choice == 'd':
        user_input_string = input('↪️ Enter data which you want to decrypt : ')
        user_input_key = input('↪️ Enter corresponing key to decode : ')
        if user_input_key in key_list:
            decode_list = []
            if len(user_input_string) > 8 :
                words = user_input_string.split()
                for word in words:
                    new_str = word[3:-3]
                    new_str = new_str[-1]+new_str[1:-1] + new_str[0]
                    decode_list.append(new_str)
            else:
                new_str = user_input_string[3:-3][::-1]
                decode_list.append(new_str)
            print("Decoding..",end='')
            for i in range(2):
                time.sleep(1)
                print('.',end='')
            print('\nMessage : ', ' '.join(decode_list))
        else :
            print("Incorrect key or Invalid data to decrypt :<\n")
    elif user_choice == 'q':
        break
    else:
        print("Oops, You entered invalid option. Try again")

