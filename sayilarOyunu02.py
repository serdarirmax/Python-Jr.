# Kullanıcıdan bir sayıyı bulmasını istiyoruz
# daha büyük veya daha küçük diye yönlendiriyoruz

sayi=25
hak=5
while hak>0:
    Tahmin = int(input("Lütfen pozitif bir tam sayı giriniz: "))

    if Tahmin<0:
        print("Girilen sayı pozitif tam sayı değildir!")
        hak-=1
        continue

    if Tahmin==sayi:
        print("Tebrikler! İyi sallıyosun.")
        break

    hak-=1

    if hak==0:
        print("Tüm haklarınızı kullandınız. Game Over!")
        break

    if Tahmin>sayi:
        print("DAHA KÜÇÜK bir sayı olmalı!")

    elif Tahmin<sayi:
        print("DAHA BÜYÜK bir sayı olmalı!")