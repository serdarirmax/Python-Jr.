# Kullanicidan iki sayi girmesini isteyin. Kullaniciya dort islem menusunu
# gosterin ve birini secmeleri isteyin.
# Kulanicinin secimine gore girilen sayilarin islem sonucu yazdirin

sayi1=int(input("Hesaplamak için kullanacağınız birinci sayıyı giriniz :"))
sayi2=int(input("Hesaplamak için kullanacağınız ikinci sayıyı giriniz :"))
islem=input("""Lütfen yapmak istedğiniz işlemi seçiniz :"
Toplama (+) Çıkartma (-)  Çarpma (*)Bölme (/)
Seçiminiz :""")
if islem=="+":
    print("toplama işleminin sonucu :",sayi2+sayi1)
elif islem=="-":
    print("çıkartma işleminin sonucu :",sayi1-sayi2)
elif islem=="*":
    print("çarpma işleminin sonucu :",sayi2*sayi1)
elif islem=="/":
    print("bölme işleminin sonucu :",sayi1/sayi2)
else:
    print("Yanlış/hatalı paramete girdiniz!")