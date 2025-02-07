# Ornek 1
# istediğimiz kadar argüman girebileceğimiz,
# girdiğimiz tüm sayiların ortalamasını alan bir fonksiyon oluşturalım.
def ortalama(*sayilar):
    sonuc=0
    for i in sayilar:
        sonuc=sonuc+i                   # girilen leri üst üste topla
        sonuc2=sonuc/len(sayilar)       # girilen argümanların adedini alıp böl.
    return round(sonuc2,3)              # çıktıda virgülden sonra 3 basamak versin.
print(ortalama(5,10.47,14,85.4))


# Ornek 2
# istediğimiz kadar argüman girebileceğiz ve sonrasında buldugumuz ortalama değerin
# belirlediğimiz bir rakamdan büyük mü / küçük mü oldugunu belirleyeceğimiz bir kod yazalım.
#
def ortalama(x,*sayi):
    toplam=0
    for i in sayi:
        toplam=toplam+i                   # girilen leri üst üste topla
    sonuc=toplam/len(sayi)            # girilen argümanların adedini alıp böl.
    if sonuc>x:
        print(f"Girilen sayiların ortalaması:{sonuc}\nBelirlemis olduğunuz değer olan {x}'den/dan büyüktür.")
    elif sonuc<x:
        print(f"Girilen sayiların ortalaması:{sonuc}\nBelirlemis olduğunuz değer olan {x}'den/dan küçüktür.")
    else:
        print(f"Girilen sayiların ortalaması:{sonuc}\nBelirlemis olduğunuz değer olan {x}'ile eşittir.")
    return sonuc             # çıktıda virgülden sonra 3 basamak versin.

ortalama(10,15,5,10)