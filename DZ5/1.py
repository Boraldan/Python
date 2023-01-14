# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".

st = 'лдофы  фдылабв  аБв дловфы абвыдфлоф'.split()
print(st)
st = list(filter(lambda x: not 'абв' in x.lower(), st))
print(st)