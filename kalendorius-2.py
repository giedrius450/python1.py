intervalas_pradzia = 9
intervalas_pabaiga = 17
einamoji_diena = 4
kalendorius = []

for i in range(31+1):
    if einamoji_diena > 4:
        einamoji_diena = 1
    kalendorius.append(einamoji_diena)
    einamoji_diena += 1

for i in range(intervalas_pradzia, intervalas_pabaiga + 1):
    print(str(i) + "-oji diena: " + str(kalendorius[i - 1]))
