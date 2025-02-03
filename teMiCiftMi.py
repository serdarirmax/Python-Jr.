# Kullanıcıdan aldığın sayinin çift mi tek mi olduğunu döndüren bir kod yazınız.

sayi=int(input("Lütfen bir sayıyı giriniz :"))
Kontrol=(sayi>0) and (sayi%2==1)

if Kontrol==True:
    print(f"{sayi} pozitif bir tek sayidir")
else:
    print(f"{sayi} pozitif bir tek sayı değildir.")