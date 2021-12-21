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
pilotak = [i for i in adatok if int(i[1][0:4]) < 1901]
# p = padding = ures hely
p = ' '*8
[print(f'{p}{i[0]} ({i[1]})') for i in pilotak]

pilotak = sorted(list(filter(lambda x: x[-1] != -1, adatok)), key=lambda x: x[-1])
print(f'6. feladat: {pilotak[0][2]}')

stat = {}
for sor in adatok:
    # A sorszam nelkuli rekordokat figyelmen kivul hagyjuk
    if sor[-1] == -1:
        continue
    stat[sor[-1]] = stat.get(sor[-1], 0) + 1

stat = stat.items()

stat = filter(lambda x: x[1] > 1, stat)
stat = map(lambda x: str(x[0]), stat)
print('7. feladat: ', end='')
print(', '.join(stat))