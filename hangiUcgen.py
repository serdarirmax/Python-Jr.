 # Aşağıdaki seçenekler doğrultusunda gereken kodu yazınız.
 # a) Bir üçgenin iki kenarının uzunluğu eşitse "İkizkenar Üçgen".
 # b) Bir üçgenin tüm kenarlarının uzunluğu eşitse "Eşkenar Üçgen".
 # c) a ve b koşulları sağlanmıyorsa "Çeşit Kenar Üçgen"

kenar1=int(input("ücgenin 1. kenar uzunlugunu giriniz : "))
kenar2=int(input("ücgenin 2. kenar uzunlugunu giriniz : "))
kenar3=int(input("ücgenin 3. kenar uzunlugunu giriniz : "))

if kenar1==kenar2==kenar3:
    print("Eşkenar üçgen")
elif kenar3==kenar1 or kenar2==kenar1 or kenar2==kenar3:
    print("İkizkenar üçgen")
else:
    print("Çeşitkenar üçgen")