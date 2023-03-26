# Добавлена функция счета комплексных чисел

def calc(my_list):

    while '*' in my_list or '/' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '*':
                result = my_list.pop(i+1) * my_list.pop(i-1)
                my_list[i-1] = result
                break
            elif my_list[i] == '/':
                result = my_list.pop(i-1) / my_list.pop(i)
                my_list[i-1] = result
                break

    while '+' in my_list or '-' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '-':
                result = my_list.pop(i-1) - my_list.pop(i)
                my_list[i-1] = result
                break
            elif my_list[i] == '+':
                result = my_list.pop(i+1) + my_list.pop(i-1)
                my_list[i-1] = result
                break

    return my_list

# s = '(5*2+(2+5j))+(((5+5)*2+5)*2)'
s = '(5+5/2)*3+(10-5)'

text = s.replace('+', ' + ')\
    .replace('-', ' - ')\
    .replace('*', ' * ')\
    .replace('/', ' / ')\
    .replace('(', ' ( ')\
    .replace(')', ' ) ').split()

print(text)

new_text = []
flag = True
count = 0

for i, el in enumerate(text):
    if text[0].isdigit() or '(' in text[0]: 
        if el.isdigit():
            new_text.append(int(el))
        elif 'j' in el:
            new_text.append(complex(el))
        elif (("+" in el or "-" in el or "*" in el or "/" in el) and (str(new_text[i-1])).isdigit()) \
            or (("+" in el or "-" in el or "*" in el or "/" in el) and ')' in new_text[i-1]):
            new_text.append(el)
        elif "(" in el or ")" in el:
            new_text.append(el)
            count += 1
        else:
            flag = False
            break
    else:
        flag = False
        break

if count%2:
    flag = False

if flag:
    # old_list = [int(elem) if elem.isdigit() else elem for elem in old_list]
    # old_list = [complex(el) if 'j' in str(el)  else el for el in old_list]

    print(new_text)
    print('перевернутый список', new_text[::-1])

    while '(' in new_text:
        first_i = len(new_text) - new_text[::-1].index('(') - 1
        second_i = first_i + new_text[first_i:].index(')')

        new_text = new_text[:first_i] + calc(new_text[first_i + 1:second_i]) + new_text[second_i+1:]
        print('текущее состояние выражения:', new_text)

    new_text = calc(new_text)
    print(str(new_text[0]))

else:
    print('Не могём такое решать.')