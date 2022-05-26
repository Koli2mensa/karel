import time

pc = int(input("prvni cislo: "))
dc = int(input("druhe cislo: "))

End = True
vysledek = ''
zbytek = 0
delitel = 0
pc = str(pc)
i = 0
Zbytek = []
konec = 0
perioda = ''
Per = 0


while End:
    delitel = str(delitel)

    if len(pc)>i:
        delitel = delitel + pc[i]
    else:
        if konec == 0:
            vysledek = vysledek + '.'
        konec = 1
        delitel = delitel + '0'

    delitel = int(delitel)

    zbytek = delitel%dc
    
    vysledek = vysledek + str(int((delitel-zbytek)/dc))

    delitel = 0
    delitel = zbytek

    if konec == 1:
        Zbytek.append(zbytek)

        for i in range(len(Zbytek)-2):
            if Zbytek[-1] == Zbytek[i] != 0 and Per == 0 and Zbytek[-2] == Zbytek[i-1]:
                vysledek = vysledek + 'P' 
                Per = 1
                End = False
                perioda ='-'
            elif Per == 1:
                perioda = perioda + '-'
            else:
                perioda = perioda + ' '
    else:
        perioda = perioda + ' '

    if delitel == 0 and i >= len(pc)-1:
        End = False

    i+=1   

Vysledek = []

for i in range(len(vysledek)):
    Vysledek.append(vysledek[i])

Ano = 1

for i in range(len(Vysledek)-1):
    if Vysledek[i] == '0':
        if Vysledek[i+1] != '.' and Ano == 1:
            Vysledek.pop(i)
        else:
            Ano = 0
    else:
        Ano = 0

vysledek = ''

for i in range(len(Vysledek)):
    vysledek = vysledek + Vysledek[i]

perioda = '---'+perioda
for i in range(len(vysledek)-len(perioda)-1):
    perioda = ' '+perioda

print(perioda)
print(vysledek)
   
   
