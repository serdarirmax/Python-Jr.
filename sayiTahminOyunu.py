import random
sayi=random.randint(1,10)
tahmin=int(input("Bakalım aklımdan geçen sayıyı bulabilecekmisin? :)"))
sayac=4
while True:
    if sayac==0:
        print("Hakkınız kalmadı! Cacık oldunuz.")
        break
    elif sayi==tahmin:
        print("Bravo doğru tahminde bulundunuz!")
        break
    else:
        print(f"Olmadı paşam, Kalan hakkın:{sayac} Tekrar dene!")
        sayac-=1
        tahmin=int(input("Tekrak denemelisin!"))