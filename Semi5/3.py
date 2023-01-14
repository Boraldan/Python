# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".

st = 'лдофы  фдылабв  аБв дловфы абвыдфлоф'.split()
print(st)
st = list(filter(lambda x: not 'абв' in x.lower(), st))
print(st)

# \

# text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'

# text = list(filter(lambda  el: 'абв' not in  el.lower(), text.split()))
# print(' '.join(text))
