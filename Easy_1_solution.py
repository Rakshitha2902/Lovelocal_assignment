s = input()
cont = 0
len_s = len(s)

for i in range(len_s - 1, -1, -1):
    if s[i] != ' ':
        cont += 1
    else:
        break

print(cont)