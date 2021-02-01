bos_liste = []
top_sayi = int(input('Toplam kaç sayı olsun ? :: '))
for n in range(top_sayi):
    sayilar = int(input('Sayi Gir '))
    bos_liste.append(sayilar)


for j in bos_liste:
    if j % 2 == 0:
        continue
    else:
        print("Listedeki En Yüksek Tek Sayı :", max(bos_liste))
        break
