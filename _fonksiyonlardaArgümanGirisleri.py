#
#    * ifadesi ile data tipini demet olarak alacak ve aşagıdaki for ile kaç
#      adet sayı girersem gireyim toplama işlemi yapacak.
#      bu yapıya *args (isteğe bağlı) olarak adlandırırlan yapı. istediğimiz argünamı bu şekilde kullanabiliyoruz.

def toplam(*x):
    sayac=0
    for i in x:
        sayac=sayac+i
    return sayac
print(toplam(5,8,79,75,88))


def isim(*x):
    #return "Merhaba benim adım {}, soyadım {}".format(x[0],x[1])
    return f"Merhaba benim adım {x[0]}, soyadım {x[1]}." # python3 syntax
print(isim("serdar","bey"))

#      Anahtar sözlük argüman yapısı  **kwarg
#    ** ifadesi ile data tipini dict olarak alacak ve aşagıdaki for ile bilgi verisinden ister keyleri istersede
#      value ları çakabileceğim. bu yapı **kwarg olarak adlandırırlan yapı. istediğimiz argünamı bu şekilde kullanabiliyoruz.

def kimlik(**bilgi):
    for i in bilgi.keys():              # keyleri çekiyoruz.
        print(i)
kimlik(Ad="Serdar",Soyad="Bey",Yas=24)

def kimlik(**bilgi):
    for i in bilgi.values():             # value ları çekiyoruz.
        print(i)
kimlik(Ad="Serdar",Soyad="Bey",Yas=24)


def kalori(**meyve):
    return meyve
print(kalori(elma=45,armut=55))




print(kalori(elma=45,armut=55))
