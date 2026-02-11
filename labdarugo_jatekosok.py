"""
Olvasd be a labdarugok.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány játékos szerepel a fájlban?
2. Melyik játékos szerezte a legkevesebb gólt?
3. Melyik játékos szerzett a legtöbb gólt?
4. Ki játszott a legtöbb mérkőzést?
5. Átlagosan hány gólt szerzett egy játékos?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerzett a legtöbb gólt? (feltételezve, hogy egy játékos csak egy csapatban játszott)


A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""
jatekosok = []

with open("beolvasando_adatok\labdarugok.txt", "r", encoding="utf-8") as f:
    fejlec = f.readline()
    for sor in f:
        adatok=sor.strip().split(";")
        jatekosok.append(adatok)
        jatekosok.append({
            "nev": adatok[0],
            "csapat": adatok[1],
            "golt": int(adatok[2]),
            "merkozes": int(adatok[3])
        })


        print(adatok)


print("A beolvasott fájlban összesen ____ játékos szerepel.")
print("A legkevesebb gólt szerző játékos: ____")
print("A legtöbb gólt szerző játékos: ____")
print("A legtöbb mérkőzést játszó játékos: ____")
print("Az átlagos gólszám: ____")
print("***A legtöbb gólt szerző csapat: ____")
