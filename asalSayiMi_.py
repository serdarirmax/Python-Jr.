# Kullanıcıdan alınan sayinin asal olup olmadığı bilgisini döndüren kodu yazınız.

print("Aklından geçen sayının asal olup olmadıgını mı merak ediyorsun?")
sayi=int(input("Cevabı öğrenmek için sayiyi gir : "))
if sayi<=1:
    print("sayi 1 ve 1den küçükse asal sayı değildir.")
elif sayi==2:
    print("2 en küçük asal sayıdır.")
else:
    sayac = 0
    for i in range(2,sayi):  # range(2, int(sayi ** 0.5) + 1) => hızlı işlem
        if sayi%i==0:
            sayac+=1
            break
    if sayac==0:
        print(f"{sayi}, asal sayıdır.")
    else:
        print(f"{sayi} asal sayı değildir.")
