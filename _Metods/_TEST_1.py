st = '26*x**27 + 17*x**26 + 20*x**25 + 9*x**24 + 30*x**23 + 60*x**22 = 0' 
n_st = ''
for el in st:
    if el.isdigit():
        n_st += el
    else:
        n_st += ' '
        # print(el)

n_st = n_st.split()
# print(n_st)
n_st = list(map(int, n_st))
print(n_st)

n_st = list(filter(lambda e: not e % 2, n_st))
print(n_st)