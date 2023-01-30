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
s= '5+5'
old_list = s.replace('+', ' + ')\
    .replace('-', ' - ')\
    .replace('*', ' * ')\
    .replace('/', ' / ')\
    .replace('(', '( ')\
    .replace(')', ' )').split()

old_list = [int(elem) if elem.isdigit() else elem for elem in old_list]
old_list = [complex(el) if 'j' in str(el)  else el for el in old_list]

print(old_list)
print('перевернутый список', old_list[::-1])

while '(' in old_list:
    first_i = len(old_list) - old_list[::-1].index('(') - 1
    second_i = first_i + old_list[first_i:].index(')')

    old_list = old_list[:first_i] + calc(old_list[first_i + 1:second_i]) + old_list[second_i+1:]
    print('текущее состояние выражения:', old_list)

old_list = calc(old_list)
print(str(old_list[0]))