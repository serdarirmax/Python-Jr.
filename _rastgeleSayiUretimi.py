import random

x=random.random()
print(x)

xy=random.randint(0,999999)   # verilen iki değer arasında int bir sayı üretir.
print(xy)

xyz=random.randrange(1,13,2)  # verilen iki değer arasında (1.değer ve 2.değer)
print(xyz)                                    # 3. değerle belirlenmiş kurala uyarak int bir sayı üretir.

a=random.uniform(10,11)      # verilen iki değer arasında float bir sayı üretir.
print(a)

b=random.choice(["2","a","G","45","re",5,6])   # verilen listen,in içerisinden rasgele seçimler yapmak
print(b)
blist=["ali","veli","orhan","levent","demir","tunahan"]
print(random.choice(blist))

print(random.shuffle(blist))   # Listedeki değerleri başka bir index ile değiştiriyor.
print(blist)

print(random.sample(blist,2))  # Listeden rasgele 2 eleman secmek için.


