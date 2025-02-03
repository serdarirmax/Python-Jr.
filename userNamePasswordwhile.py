# Sisteme giriş yapmak isteyen kullanıcını için kullanıcı adı ve parola bilgilerini girmesini isteyim
# bilgiler dogruysa hoşgeldiniz yanlışsa kalan hakkınınz acıklaması verin.

sayac=2
for i in range(0,3):
    userName=input("Kullanıcı Adınız: ")
    Password=input("Parolanız: ")

    if userName=="Serdar Bey" and Password=="P@ssw0rd1":
        print("Hoşgeldiniz!")
        break
    elif (userName!="Serdar Bey" or Password!="P@ssw0rd1") and sayac!=0:
        print(f"""Hatalı giriş
Lütfen tekrar deneyiniz
kalan hakkınız {sayac}""")
        sayac-=1
    else:
        print("Giriş başarısız! Sistem kapatılıyor.")