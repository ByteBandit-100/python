import string as st
import random
psd_list = st.ascii_letters+st.punctuation
def password_generator(length,lst):
    generated_psd = ''
    if length<4:
        length = 4
    for i in range(length):
        generated_psd = generated_psd + random.choice(lst)
    return generated_psd
while True:
    print("""\n------------------ Password Generator ------------------\n
    --> By Default password length is 8 characters.
    --> If no length is given by default length is set.
    --> Password length no less than <4 by user. ❌
    """)
    psd_length  = input("Enter length of password >4 (q for quit) : ")
    if psd_length.lower() == 'q':
        break
    try:
        print('\nGenerated Password is : \n',password_generator(int(psd_length), psd_list))
    except:
        print("Invalid input.")