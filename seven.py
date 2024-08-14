import random
tiedosto = open("nimet.txt", "r")
 
rivit = tiedosto.readlines()


valinta = input("(s)atunnainen rivi, (i)käkysely, (p)oiminta, (n)imikysely vai (k)irjainkysely ? ")
if valinta == "s":
    print("Tulostetaan satunnaine ")    
    satrivi = random.choice(rivit)
    print(satrivi)
elif valinta == "i":  
    for rivi in rivit:
       rivinOsat = rivi.split()
       rivinVuosi = int(rivinOsat[1])
       if rivinVuosi >= 2006:
            print(rivi)
elif valinta == "p":  
    numero = int(input("anna numero"))
    k = 0
    for rivi in rivit:
       k += 1
       if k % numero == 0:
           print(rivi)

elif valinta == "n":
    nimi = input("Änna nimi")

    for rivi in rivit:
        if nimi in rivi:
            print(rivi)


elif valinta == "k":
    later = input("Änna irjainkysely")

    for rivi in rivit:
        if later in rivi:
            print(rivi)