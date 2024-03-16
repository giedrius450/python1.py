n=12
m=5

visits=[1, 2, 3, 2, 3,]# Vizitai is veikeju: 1-Mazylis, 2- Karlsonas ir 3- Frekenbok.

eating_spoons = [2,5,3]# kiek saukstuku suvalgo kiekvienas veikejas: 2-Mazylis, 5- Karlsonas ir 3- Frekenbok.

for i in range(m):
    spoons = eating_spoons[visits[i]-1]# kiek saukstu suvalgo einamasis valgytojas.
    if n >=0:
        n = n-spoons
        print(spoons)
    else:
        if n<0:
            n=0
        break

print(n)