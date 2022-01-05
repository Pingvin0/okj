f = open('eredmenyek.csv', 'r', encoding='latin2')
adat = [i.split(';') for i in f.read().strip().split('\n')]
#hazai;idegen;hazai_pont;idegen_pont;helysz�n;id�pont
# 0.      1.    2.          3.          4.       5. 

#3. feladat
hazai = sum([True for i in adat if i[0] == 'Real Madrid'])
idegen = sum([True for i in adat if i[1] == 'Real Madrid'])
print(f'3. feladat: Real Madrid: Hazai: {hazai}, Idegen: {idegen}')

#4. feladat
volt = 'nem'
if len(list(filter(lambda x: x[2] == x[3], adat))) > 0:
  volt = 'igen'
print(f'4. feladat: Volt dontetlen? {volt}')

#5. feladat
csapatnev = [i for i in adat if 'Barcelona' in i[0]][0][0]
print(f'5. feladat: barcelonai csapat neve: {csapatnev}')

#6. feladat
meccsek = [i for i in adat if i[5].strip() == '2004-11-21']
print('6. feladat:')

for i in meccsek:
  print('\t %s-%s (%s:%s)' % (i[0], i[1], i[2], i[3]) )

#7. feladat
stat = {}
for i in adat:
  stat[i[4]] = stat.get(i[4], 0) + 1

stat = sorted(stat.items(), key=lambda x: x[1], reverse=True)
print('7. feladat:')
for i in stat:
  if i[1] < 21:
    break
  print('\t%s: %i' % i)