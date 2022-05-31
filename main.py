def encoder(string, key, number):
    key = list(map(int, key))
    lenstr = len(string)
    lenkey = len(key)
    if number == 1:
        string = string.ljust(lenstr + (lenkey - lenstr % lenkey) % lenkey, "\0")
        lenstr = len(string)
    count = int(lenstr / lenkey)
    a = 0
    b = lenkey
    string_two = ''
    if number == 2:
        for i in range(count):
            c = 0
            helper = list(string[a:b])
            helper_two = list(string[a:b])
            for j in key:
                helper[j] = helper_two[c]
                c+=1
            a = b
            b = b + lenkey
            string_two += ''.join(helper)
        while string_two[-1] == ' ':
            string_two = string_two[:-1]
    else:
        for i in range(count):
            helper = string[a:b]
            for j in key:
                string_two += str(helper[j])
            a = b
            b = b + lenkey
    return string_two


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
    a = 0
    b = lenkey
    string_two = []
    string_three = ''
    print(string)
    if number == 2:
        for i in range(count):
            c = 0
            helper = list(string[a:b])
            helper_two = list(string[a:b])
            for j in key:
                helper[j] = helper_two[c]
                c += 1
            a = b
            b = b + lenkey
            string_two+=helper
        string_three += ' '.join(string_two)
        while string_three[-1] == ' ':
            string_three = string_three[:-1]
    else:
        for i in range(count):
            helper = string[a:b]
            for j in key:
                string_two.append(str(helper[j]))
            a = b
            b = b + lenkey
        string_three = ' '.join(string_two)
    return string_three


def encoder_three(string, key, number, lenb_1):
    key = list(map(int, key))
    lenkey = len(key)
    lenstr = len(string)
    count_symbols = (lenb_1 - lenstr % lenb_1) % lenb_1 + ((lenkey - lenstr % lenkey) % lenkey)
    string += '\0' * count_symbols
    lenstr = len(string)
    block = ''
    temporary = lenb_1
    string_two = []
    for i in range(lenstr):
        if temporary == 0:
            string_two.append(block)
            block = ''
            temporary = lenb_1
        block += string[i]
        temporary -= 1
    string_two.append(block)
    lenstr = len(string_two)
    count = int(lenstr / lenkey)
    a = 0
    b = lenkey
    string_three = ''
    string_4 = []
    if number == 2:
        for i in range(count):
            c = 0
            helper = list(string_two[a:b])
            helper_two = list(string_two[a:b])
            for j in key:
                helper[j] = helper_two[c]
                c += 1
            a = b
            b = b + lenkey
            string_4+=helper
        string_three += ''.join(string_4)
        while string_three[-1] == ' ':
            string_three = string_three[:-1]
    else:
        for i in range(count):
            helper = string_two[a:b]
            for j in key:
                string_three += str(helper[j])
            a = b
            b = b + lenkey
    return string_three

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
        maxkey = max(key)
        if len(set(key)) != maxkey + 1:
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


print('Расшифровка и зашифровка сообщений без смс и регистрации, бесплатно, офлайн.')
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


