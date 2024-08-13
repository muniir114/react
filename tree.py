import random
tiedosto = open("nimet.txt", "r")
 
rivit = tiedosto.readlines()


valinta = input("(s)atunnainen rivi vai (i)käkysely? i)Tänä vuonna täysi-ikäiset: ")
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
  





