######################### .append() ##################################
Liste=[1,2,3,7,89,"merhaba",5.8]
Liste.append("SERDAR")
print(Liste)   # Listeye güncelleme yapar, verdiğimiz parametreyi listenin sonuna ekler.
######################### .append() ###################################
bilgiler=[1,4,7,"Serdar",888,"TR"]
bilgiler.insert(3,"Super")  # 3. indexe "super" ekle şeklinde kullanılır.
print(bilgiler)
######################### .remove() ###################################
siraNo=[1524,1525,1526,1527,1528,1529]
siraNo.remove(1526)  # parametrede liste içerisinden verilen değeri siler
print(siraNo)
######################### .pop() #######################################
musteriSiraNo=[15,16,17,18,19,20,21,22,23,24]
musteriSiraNo.pop()   # parametresiz olarak kullanılırsa listedin en sonundan veri siler.
musteriSiraNo.pop(0)   # parametre olarak index değeri vererek silme de yapabiliriz.
print(musteriSiraNo)
######################### .copy() ######################################
Liste=["Ali","Veli",49,50]
Liste2=Liste.copy()   # listenin kopyasını almak için kullanılır.
print(Liste2)
######################### .extend() ####################################
liste33=[1,2,3,4,5,6]
liste44=["a","e","z","b","t"]
liste33.extend(liste44) # extend methodu birinci listenin bitiminden itibaren verdiğimiz listenin eklenmesini sağlar.
print(liste33)

liste88=[1,2,3,4]
liste99=["x","y","z"]   # method kullanmaksızın aşağıdaki şekilde de listeleri birbirleri üzerine ekleyebiliriz
liste88+=liste99
print(liste88)
######################### .count() ######################################
yas=[15,23,16,18,17,15,22,23,24,25,26,25,24,18,19,26,19,14,21,24,26,35,26,24,25,27,28]
print(yas.count(35)) # 35 yaşında olup sistemimize kayıtlı kac kişi var?
######################### .sort() #######################################
yaslar=[15,23,16,18,17,15,22,23,24,25,26,25,24,18,19,26,19,14,21,24,26,35,26,24,25,27,28]
yaslar.sort()  # küçükten büyüğe sıraladı.
print(yaslar)
# yaslar.sort(reverse=True) ile istersek büyükten küçüğe de sıralayabiliriz.
######################### .reverse() #####################################
isListesi=["a","k","j","n","p","b","x","i"]
isListesi.reverse()   # indexlere göre sondan başa doğru sıralıyor.
print(isListesi)
######################### .clear() #######################################
alist=[1,2,5,"Mert","Can"]
alist.clear()   # Listenin içindeki değerleri siler.
print(alist)