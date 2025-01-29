
Bilgi={
    "Ad":"Serdar",
    "Soyad":"Pythonzade",
    "TCno":123456,
    "D.Yeri":"SilikonVadisi"
}
print(Bilgi.keys()) # Sadece keyleri döndürür.
print(Bilgi.values()) # Sadece value'leri döndürür.
print(Bilgi.items()) #  key ve value ları eşleşmeleri ile beraber döndürür.
print(Bilgi.get("Soyad"))  # getirmesi istenen parametreyi çekmek için kullanılır
Bilgi.update({"Cinsiyet":"Erkek"})
print(Bilgi)  # update kullanarak yeni bir key ve value eklemiş oluyoruz.
Bilgi2=Bilgi.copy()  # kopyalama işlemi yapıyor.
print(Bilgi2,"***")
print(Bilgi.__len__())  # kaç dictionary var sayısını veriyor
Bilgi.pop("Cinsiyet")  # key ve karşılıgındaki value ' yu siler.
print(Bilgi)
Bilgi.clear() # siler
print(Bilgi)