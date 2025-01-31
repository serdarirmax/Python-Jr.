# Kullanicinin vermis oldugu character buyuk harf ise ekrana "Buyuk Harf",
# kucuk harf ise ekrana "Kucuk Harf" yazdiran kodu olusturunuz.

x=input("Bir harf giriniz :")
x2=x[0]
if   ord(x2) >= 65 and ord(x2) <= 90:
    print("Buyuk harf")
elif   ord(x2) >= 97 and ord(x2) <= 122:
    print("Kucuk harf")
else:
    print("Yanlış giriş")
