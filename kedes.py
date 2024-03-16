n = 3 # Eiliu skaicius.
k = 8 # Kedziu eileje skaicius.
s=0 # Kiek kedziu reikia uzsakyti.

for i in range(n): # Einame per visas eiles.
    s = s + k # Pridedame eiles kedes prie bendro skaiciaus.
    k =k+2 # Kiekvienpje sekancioje eileje pridedame dvi papildomas kedes.

print(s)