in_L = [10, 3, 3, 3, 1, 4, 3, 3, 10, 3, 7, 3, 5, 5]

temp = []

i = 0
while i < len(in_L)-1:
    if in_L[i] in in_L[i+1:]:
        temp.append(in_L[i])
    i=i+1

print(in_L)

Fin = list(set(in_L) - set(temp))

print(Fin)

