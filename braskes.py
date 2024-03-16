# Doumenys
b = input("b: ")# Prinoko b braskiu pirmaja diena.
d = input("d: ")# Kiekviena kita diena prinoksta d braskiu daugiau, negu pries tai buvusia.
n = input("n: ")# kiek is viso dienu.

count = 0
suma = 0

count = int(b)
for i in range(int(n)):
    suma = suma + count
    count = count + int(d)
print(suma)