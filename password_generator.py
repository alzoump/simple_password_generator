import random
# import string

ext = 'n'
symbols = [chr(i) for i in range(33, 127) if chr(i) not in ['<', '>', '/', '[', ']', '{', '}', '.', ',', '', '|', '(',
                                                            ')', '*', '~', ' ', '"', '-']]

while ext == 'n':
    size = input("size of password")
    password = [size]

    for i in range(0, size):
        password.append(random.choice(symbols))

    print(password)
    ext = raw_input("is that good (y/n) ? ")
