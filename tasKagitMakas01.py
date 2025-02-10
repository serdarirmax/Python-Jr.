import random
oyun=["TAS","KAGIT","MAKAS"]
bilgisayar=random.choice(oyun)
oyuncu=input("Seçiminizi giriniz: TAS, KAGIT, MAKAS")
if bilgisayar == "KAGIT" and oyuncu == "MAKAS":
    print("Kazandınız")
elif bilgisayar == "KAGIT" and oyuncu == "TAS":
    print("Kaybettiniz")
elif bilgisayar == "MAKAS" and oyuncu == "TAS":
    print("Kazandınız")
elif bilgisayar == "MAKAS" and oyuncu == "KAGIT":
    print("Kaybettiniz")
elif bilgisayar == "TAS" and oyuncu == "KAGIT":
    print("Kazandınız")
elif bilgisayar == "TAS" and oyuncu == "MAKAS":
    print("Kaybettiniz")
else:
    print("Berabere")