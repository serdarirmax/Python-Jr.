# Kullanicidan aldiginiz sayinin 3e ve 5e tam bolunup bolunmedigini hesaplayan
# 3e bolunuyorsa "uc ile bolunebilen bir tam sayi"
# 5e bolunuyorsa "5 ile bolunebilen bir tam sayi"
# her ikisinede bolunebiliyorsa "SUPER SAYI" diye konsola yazdiran bir program yaziniz.

sayi=int(input("Bir sayı giriniz :"))
if sayi%3==0 and sayi%5==0:
    print("süper sayi")
elif sayi%3==0:
    print("3 ile bölünebilen bir tam sayi")
elif sayi%5==0:
    print("5 ile bölünebilen bir sayi")
else:
    print("3 e veya 5 e bölünebilen bir sayi değil")

    # Sayı girmezsek sıcıyor güncelleme gerekli!!!