# Sıfırdan farklı oldugu sürece klavyeden girilen sayilarin karesini alan programı yaziniz.
# 0 ile programdan cikilsin.

while True:
    sayi=int(input("Karesini almak istediğiniz sayiyi yaziniz"))
    print("girilen sayinin karesi : ",sayi*sayi)
    if (sayi==0):
        break
