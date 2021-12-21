adatok = []
with open('pilotak.csv', 'r', encoding='utf-8-sig') as f:
    f.readline()
    for line in f.read().strip().split('\n'):
        # ld = line data = sorban levo adatok
        ld = line.split(';')
        # Ha nincs rajtszam, akkor -1 legyen, egyebkent meg alakitsuk int-e
        ld[-1] = -1 if ld[-1] == '' else int(ld[-1])
        adatok.append(ld)

print(f'3. feladat: {len(adatok)}')
print(f'4. feladat: {adatok[-1][0]}')

# 19. szazad elott szuletett pilotak
pilotak = filter(lambda x: int(x[1][0:4]) < 1901, adatok)

# ures hely
hely = ' '*8
for pilota in pilotak:
    nev = pilota[0]
    szuletes = pilota[1]
    print(f'{hely}{nev} ({szuletes})')

pilotak = sorted(list(filter(lambda x: x[-1] != -1, adatok)), key=lambda x: x[-1])
print(f'6. feladat: {pilotak[0][2]}')

# Keszitunk egy szotarat, amiben a kulcs a rajtszam,
# es az hogy hanyszor hasznaljak az elem
stat = {}
for sor in adatok:
    # A rajtszam nelkuli rekordokat figyelmen kivul hagyjuk
    if sor[-1] == -1:
        continue
    stat[sor[-1]] = stat.get(sor[-1], 0) + 1

# atalakitjuk listava
# pelda: [(rajtszam, hasznalatszam), (rajtszam, hasznalatszam)]
stat = stat.items()

# csak akkor maradjon benne, ha a rajtszamot tobb alkalommal hasznaljak
stat = filter(lambda x: x[1] > 1, stat)
stat = map(lambda x: str(x[0]), stat)

print('7. feladat:', ', '.join(stat))