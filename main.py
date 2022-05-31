def encoder(string, key, number):
    key = list(map(int, key))
    lenstr = len(string)
    lenkey = len(key)
    if number == 1:
        string = string.ljust(lenstr + (lenkey - lenstr % lenkey) % lenkey, "\0")
        lenstr = len(string)
    count = int(lenstr / lenkey)
    p1 = 0
    p2 = lenkey
    string_2 = ''
    if number == 2:
        for i in range(count):
            c = 0
            helpstr_1 = list(string[p1:p2])
            helpstr_2 = list(string[p1:p2])
            for j in key:
                helpstr_1[j] = helpstr_2[c]
                c+=1
            p1 = p2
            p2 = p2 + lenkey
            string_2 += ''.join(helpstr_1)
        while string_2[-1] == ' ':
            string_2 = string_2[:-1]
    else:
        for i in range(count):
            helpstr = string[p1:p2]
            for j in key:
                string_2 += str(helpstr[j])
            p1 = p2
            p2 = p2 + lenkey
    return string_2


def encoder_two(string, key, number):
    key = list(map(int, key))
    lenkey = len(key)
    if number == 1:
        string = string.split()
        lenstr = len(string)
        while len(string) != lenstr + (lenkey - lenstr % lenkey) % lenkey:
            string.append('\0')
    elif number == 2:
        string = list(string.replace('  ',' ').split(' '))
    lenstr = len(string)
    count = int(lenstr / lenkey)
    p1 = 0
    p2 = lenkey
    string_2 = []
    string_3 = ''
    print(string)
    if number == 2:
        for i in range(count):
            c = 0
            helpstr_1 = list(string[p1:p2])
            helpstr_2 = list(string[p1:p2])
            for j in key:
                helpstr_1[j] = helpstr_2[c]
                c += 1
            p1 = p2
            p2 = p2 + lenkey
            string_2+=helpstr_1
        string_3 += ' '.join(string_2)
        while string_3[-1] == ' ':
            string_3 = string_3[:-1]
    else:
        for i in range(count):
            helpstr = string[p1:p2]
            for j in key:
                string_2.append(str(helpstr[j]))
            p1 = p2
            p2 = p2 + lenkey
        string_3 = ' '.join(string_2)
    return string_3


def encoder_three(string, key, number, lenb_1):
    key = list(map(int, key))
    lenkey = len(key)
    lenstr = len(string)
    count_symbols = (lenb_1 - lenstr % lenb_1) % lenb_1 + ((lenkey - lenstr % lenkey) % lenkey)
    string += '\0' * count_symbols
    lenstr = len(string)
    block = ''
    temporary = lenb_1
    string_2 = []
    for i in range(lenstr):
        if temporary == 0:
            string_2.append(block)
            block = ''
            temporary = lenb_1
        block += string[i]
        temporary -= 1
    string_2.append(block)
    lenstr = len(string_2)
    count = int(lenstr / lenkey)
    p1 = 0
    p2 = lenkey
    string_3 = ''
    string_4 = []
    if number == 2:
        for i in range(count):
            c = 0
            helpstr_1 = list(string_2[p1:p2])
            helpstr_2 = list(string_2[p1:p2])
            for j in key:
                helpstr_1[j] = helpstr_2[c]
                c += 1
            p1 = p2
            p2 = p2 + lenkey
            string_4+=helpstr_1
        string_3 += ''.join(string_4)
        while string_3[-1] == ' ':
            string_3 = string_3[:-1]
    else:
        for i in range(count):
            helpstr = string_2[p1:p2]
            for j in key:
                string_3 += str(helpstr[j])
            p1 = p2
            p2 = p2 + lenkey
    return string_3

def check_key(key):
    if len(key) == 0:
        print('Нужно что нибудь ввести.')
        return False
    else:
        try:
            key = list(map(int, key))
        except ValueError:
            print('Данные неккоректны. Ключ = числа.')
            return False
        maxc = max(key)
        if len(set(key)) != maxc + 1:
            print('Данные неккоректны. Возможно вы ввели числа не по порядку или пропустили число.')
            return False
        return True


def check_num(number):
    if len(number) == 0:
        print('Нужно что нибудь ввести.')
        return False
    else:
        try:
            number = int(number)
        except ValueError:
            print('Данные неккоректны. Попробуем снова.')
            return False
    if number != 0 and number != 1 and number != 2:
        return False
    return True


def check_string(string):
    if len(string) == 0:
        print('Нужно что нибудь ввести.')
        return False
    return True


def check_z(z_1):
    if len(z_1) == 0:
        print('Нужно что нибудь ввести.')
        return False
    else:
        try:
            z_1 = int(z_1)
        except ValueError:
            print('Данные неккоректны. Попробуем снова.')
            return False
    if z_1 != 1 and z_1 != 2 and z_1 != 3:
        return False
    return True


def len_checker(lenb_1):
    if len(lenb_1) == 0:
        print('Нужно что нибудь ввести.')
        return False
    else:
        try:
            lenb_1 = int(lenb_1)
        except ValueError:
            print('Данные неккоректны. Попробуем снова.')
            return False
    return True


print('Расшифровка и зашифровка сообщений без смс и ррегистрации.')
while True:
    print('1) - зашифровать\n2) - расшифровать \n0) - выйти')
    num = input()
    if check_num(num):
        num = int(num)
        if num == 1 or num == 2:
            string = input('Введите сообщение\n')
            if check_string(string):
                if num == 1:
                    print('Каким образом вы хотите зашифровать сообщение?\n1) - посимвольно \n2) - по словам \n3) - по блокам')
                else:
                    print('Каким образом сообщение было зашифровано?\n1) - посимвольно \n2) - по словам \n3) - по блокам')
                z = input()
                if check_z(z):
                    z = int(z)
                    code = input('Нужен ключ вида (3 0 2 1)\n').split()
                    if check_key(code):
                        if z == 1:
                            print(encoder(string, code, num))
                        elif z == 2:
                            print(encoder_two(string, code, num))
                        else:
                            lenb = input('Введите длину блока\n')
                            if len_checker(lenb):
                                lenb = int(lenb)
                                print(encoder_three(string, code, num, lenb))
        else:
            exit()


