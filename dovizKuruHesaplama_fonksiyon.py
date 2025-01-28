#def kac_dolar(TL):
#    return (TL/35)

#Yukarıdaki fonksiyonu lambda ile buradaki gibi kısayoldan yapmakta ta mümkün.
kac_dolar=lambda TL: TL/35
TL=int(input("Dolar karsiligini ogrenmek istediginiz Turk Lirasini giriniz:"))
print(TL,"Türk Lirası=",kac_dolar(TL),"Dolardır.")

# tarihe not:  22.01.2025 dolar 35,65