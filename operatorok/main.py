with open('kifejezesek.txt', 'r', encoding='latin2') as f:
    adatok = []
    for line in f.read().strip().split('\n'):
        ld = line.split()
        ld[0] = int(ld[0])
        ld[2] = int(ld[2])
        adatok.append(ld)
print(f'2. feladat: Kifejezesek szama: {len(adatok)}')

maradekos = list(filter(lambda x: x[1] == 'mod', adatok))
print(f'3. feladat: Kifejezesek maradekos osztassal: {len(maradekos)}')

tizzel = False
for line in adatok:
    if line[0] % 10 == 0 and line[2] % 10 == 0:
        tizzel = True
        break
if tizzel:
    print('4. feladat: Van ilyen kifejezes!')
else:
    print('4. feladat: Nincs ilyen kifejezes!')

stat = {}
for line in adatok:
    if line[1] in ['mod', '/', 'div', '-', '*', '+']:
        stat[line[1]] = stat.get(line[1], 0) + 1

print('5. feladat: Statisztika')
for operator in stat:
    print(f'{operator:>8} -> {stat[operator]} db')

muvelet = {
    'mod': lambda x, y: x %  y,
    'div': lambda x, y: x // y,
    '/':   lambda x, y: x /  y,
    '*':   lambda x, y: x *  y,
    '+':   lambda x, y: x +  y,
    '-':   lambda x, y: x -  y
}

def elvegez(x, operator, y):
    if operator not in muvelet:
        return 'Hibas operator'
    try:
        return str(muvelet[operator](int(x), int(y)))
    except:
        return 'Egyeb hiba!'
p = ' ' * 8
while True:
    be = input('7. feladat: Kerek egy kifejezest (pl.: 1 + 1): ')
    if be == 'vege':
        break

    print(f'{p}{be} = {elvegez(*be.split())}')

with open('eredmenyek.txt', 'w') as f:
    for line in adatok:
        muv = f'{str(line[0])} {line[1]} {str(line[2])}'
        f.write(f'{muv} = {elvegez(*line)}' + '\n')
print('8. feladat: eredmenyek.txt')
