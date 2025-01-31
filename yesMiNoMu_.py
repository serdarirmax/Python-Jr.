
# Kullanicidan Y/N ikilisinden birisini girdiginde girdigi degeri ekrana yazdiran java kodunu yaziniz.
# INPUT : Y ,  N   OUTPUT : YES ; NO

x=(input("Y/N karakterlerinden dilediğiniz birini giriniz: "))
x2=x.lower().strip(" ")

if x2=="y":
    print("YES")
elif x2=="n":
    print("NO")
else:
    print("Girilen karakter hatalıdır.")

