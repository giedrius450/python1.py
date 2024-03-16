intervalas_pradzia = 26
intervalas_pabaiga = 31
einamoji_diena = 7
kalendorius = []

for i in range(31+1):
    if einamoji_diena > 7:
        einamoji_diena = 1
    kalendorius.append(einamoji_diena)
    einamoji_diena += 1

for i in range(intervalas_pradzia, intervalas_pabaiga + 1):
    print(str(i) + "-oji diena: " + str(kalendorius[i - 1]))
