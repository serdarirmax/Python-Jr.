# Recursive fonksiyon= Özyinelemeli fonksiyonlar, kendilerini çağırarak
# belirli bir koşul gerçekleşene kadar çalışan fonksiyonlardır.

def ustel(a,b):
    if b==0:
        return 1
    else:
        return a*ustel(a,b-1)
a=int(input("taban sayiyi giriniz:"))
b=int(input("ussel değeri giriniz:"))
print(ustel(a,b))