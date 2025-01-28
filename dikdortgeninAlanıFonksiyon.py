# Egede denize sıfır (daha ilk cümlede yüzünün sekli değişti, hayırdır?)
# bir bahçe almak için uzunluk ve genişlik değerlerini verdiginde
# sana alan ve cevresini hesaplayan fonksiyonu oluştur.

def dikdortgeninAlani(u,g):
    a=u*g
    return a

def dikdortgeninCevresi(u,g):
    c=2*(u+g)
    return c

u=int(input("Dikdortgenin uzum kenarı : "))
g=int(input("Dikdortgenin genisligi : "))
print("Alani : ",dikdortgeninAlani(u,g),"m^2")
print("Cevresi : ",dikdortgeninCevresi(u,g),"m")
