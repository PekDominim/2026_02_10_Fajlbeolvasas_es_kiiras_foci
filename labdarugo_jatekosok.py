import statistics
import os

jatekosok = []

# Beolvasás (R betű az elérési út elé a \ karakterek miatt)
with open(r"beolvasando_adatok\labdarugok.txt", "r", encoding="utf-8") as f:
    fejlec = f.readline()
    for sor in f:
        adatok = sor.strip().split(";")
        jatekosok.append({
            "nev": adatok[0],
            "csapat": adatok[1],
            "golt": int(adatok[2]),
            "merkozes": int(adatok[3])
        })

# 1. Hány játékos szerepel a fájlban?
letszam = len(jatekosok)

# 2. Melyik játékos szerezte a legkevesebb gólt?
# Megkeressük a legkisebb gólszámot, majd azt a játékost, akinek ennyi van
min_gol_ertek = min(j["golt"] for j in jatekosok)
legkevesebb_golos = next(j["nev"] for j in jatekosok if j["golt"] == min_gol_ertek)

# 3. Melyik játékos szerzett a legtöbb gólt?
max_gol_ertek = max(j["golt"] for j in jatekosok)
legtobb_golos = next(j["nev"] for j in jatekosok if j["golt"] == max_gol_ertek)

# 4. Ki játszott a legtöbb mérkőzést?
max_meccs_ertek = max(j["merkozes"] for j in jatekosok)
legtobb_meccses = next(j["nev"] for j in jatekosok if j["merkozes"] == max_meccs_ertek)

# 5. Átlagosan hány gólt szerzett egy játékos?
avgol = statistics.mean(j["golt"] for j in jatekosok)

# 6. EXTRA - Melyik csapat szerzett a legtöbb gólt?
csapatok_goljai = {}
for j in jatekosok:
    csap = j["csapat"]
    csapatok_goljai[csap] = csapatok_goljai.get(csap, 0) + j["golt"]
legjobb_csapat = max(csapatok_goljai, key=csapatok_goljai.get)

# KIÍRÁS ÉS MENTÉS
if not os.path.exists("kiirt_adatok"):
    os.makedirs("kiirt_adatok")

with open(r"kiirt_adatok\statisztika.txt", "w", encoding="utf-8") as f:
    f.write(f"1. Játékosok száma: {letszam}\n")
    f.write(f"2. Legkevesebb gól ({min_gol_ertek}): {legkevesebb_golos}\n")
    f.write(f"3. Legtöbb gól ({max_gol_ertek}): {legtobb_golos}\n")
    f.write(f"4. Legtöbb mérkőzés ({max_meccs_ertek}): {legtobb_meccses}\n")
    f.write(f"5. Átlagos gólszám: {avgol:.2f}\n")
    f.write(f"6. Legeredményesebb csapat: {legjobb_csapat}\n")

print("A statisztika elkészült a kiirt_adatok mappába!")