# UTF8 BOM enkodolasu a szoveg, ebben az esetben utf-8-sig enkodolast hasznalunk
with open('jackie.txt', 'r', encoding='utf-8-sig') as f:
    # Beolvassuk az adatokat es matrixba tesszuk, majd az elso sort ami a cimeket
    # tartalmazza, kivagjuk. Ezen felul, az adatokat int-e alakitjuk, es levagjuk a fejlecet.
    adatok = [[int(j) for j in i.split()] for ind, i in enumerate(f.read().split('\n')) if ind != 0]
    
    # Komprehenziv lista nelkul:
    # adatok = []
    # for index, line in enumerate(f.read().split('\n')):
    #     # A fejlecet eldobjuk
    #     if index == 0:
    #         continue
    #     # Hozzadunk az adatokhoz egy listat, hogy {index} hozzaferheto legyen
    #     adatok.append([])
    #     for adat in line.split():
    #         # Indexbol levonunk 1-et, mert a fejlecet eldobtuk,
    #         # es nem adtunk hozza listat az adatok tombhoz az elso iteracioban.
    #         adatok[index-1].append(int(adat))
    
    f.close()
# year	races	wins	podiums	poles	fastests
#  0      1      2         3      4         5




# 3. feladat
print(f'3. feladat: {len(adatok)}')

# 4. feladat
stat = sorted(adatok, key=lambda x: x[1], reverse=True)

# Alternativ megoldas szotarral:
# stat = {}
# for ev in adatok:
#     stat[ev[0]] = stat.get(ev[0], 0) + ev[1]
# stat = list(stat.items())
# stat.sort(key = lambda x: x[1], reverse=True)

print(f'4. feladat: {stat[0][0]}')


# 5. feladat
evtizedek = {}
for ev in adatok:
    evtized = str(ev[0])[2]
    
    evtizedek[evtized] = evtizedek.get(evtized, 0) + ev[2]

print('5. feladat:')
# padding (helykihagyas, 8 space)
p = ' '*8
for evtized in evtizedek:
    # megnyert versenyek szama
    v = evtizedek[evtized]
    print(f'{p}{evtized}0-es evek: {v} megnyert verseny')

# 6. feladat
f = open('jackie.html', 'w')

kezdet = """<!DOCTYPE html>
<html>
<head></head>
<style>td { border: 1px solid black; }</style>
<body>
<h1>Jackie Stewart</h1>
<table>"""

veg = """</table>
</body>
</html>"""

only_show = range(3)

f.write(kezdet + '\n')
for sor in adatok:
    f.write('<tr>')

    for ind, adat in enumerate(sor):
        if ind in only_show:
            f.write(f'<td>{adat}</td>')

    f.write('</tr>\n')

f.write(veg)
f.close()