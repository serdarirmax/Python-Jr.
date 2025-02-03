print(abs(-5))  # Mutlak değer alma fonksiyonu .abs()
print(round(22/7,3)) # yuvarlama fonksiyonudur 3 => virgülden sonra 3 basamak anlamına gelir.
                     # virgül olmaksızında kullanılabilir
# all() fonksiyonu birden fazla true false yapılarda tüm boolean'ların true olması durumunda true döndürür.
# any() fonksiyonu all ın tersidir. tüm booleanların içinde bir tane true varsa bize true döndürür.
print(ascii("\n"))  # karakteri yazdırmak için.
print(bool("sdr"))   # kullanılan yapıların bool değerleri üzerinden işlemler için kullanılır.
                   # 0 => false | 1 => true | "" => false " " => true | "serdar" => true
print(chr(83))  # unicode karşılığını verir.

                # list => liste olusturmak için kullanılan fonksiyondur.
x="Serdar"
print(type(x))
z=list(x)
print(z)
print(type(z))

                # set => lste olusturmak için kullanılan fonksiyondur.
x="Serdar"
print(type(x))
z=set(x)
print(z)
print(type(z))

                # tuple => demet olusturmak için kullanılan fonksiyondur.
x="Serdar"
print(type(x))
z=tuple(x)
print(z)
print(type(z))

# dir => bir yapının içerisindeki fonksiyon ve nitelikleri görmek için kullandığımız fonksiyondur.
print(dir(list))
print(dir(int))

# divmod => bölme işleminden bölen ve kalan kısmını veren fonksiyodur.
print(divmod(81,4)) # (20, 1)

# enumerate => sıralama işlemi yapar.
xy="serdar ırmak"
print(*enumerate(xy)) # (0, 's') (1, 'e') (2, 'r') (3, 'd') (4, 'a') (5, 'r') (6, ' ') (7, 'ı') (8, 'r') (9, 'm') (10, 'a') (11, 'k')
for i in enumerate(xy): # döngüler içinde sıklıkla kullanılır.
    print(i)

# help() yardım fonksiyonu
help(str)

#id her bir nesnenin farklı bir ID değeri vardır. Bunları verir.
print(id(xy))  # 1496187135600

# len uzunluk ölcen fonksiyon
print(len(xy)) # 12 => "serdar ırmak" space dahildir 12ye

# max min
c=[18,2,3,5,6,7,15,23,75,13,9]
print(max(c))
print(min(c))
d=["serdar","can","hasan","abdullah","emre"]
print(max(d,key=len))  # d listesindeki içerikleri uzunluklarına göre değerlendirmesini istedik.

# pow(2,3) üssünü alır. 2 üssü 3
print(pow(2,5)) # 32

# sep karakter aralarına koyulmasını istediklerimiz
# end en sonuna eklenmesi istenileni ekler.
print("Ankara","İstanbul","Trakya",sep="*",end="///\n")

# range => belli bir aralık almak için kullanılan fonksiyon yapısıdır.
print(list(range(0,30,4))) # kactan baslayacak 0 kaca kadar gidecek 29 (30 dahil değil) kaçar kaçar gidecek 4er

d=["serdar","can","hasan","abdullah","emre"]
print(list(reversed(d))) # =>  ['emre', 'abdullah', 'hasan', 'can', 'serdar']

# sum => sayısal değerleri toplama işlemi yapan fonksiyondur.

# type => nesnedin türünü yapısını gösterir.

# zip 2 değişkeni birleştirir
print(*zip(c,d))