from math import pi, pow

class Kup:
    def __init__(self, a):
        self.a = a

    def yAlan(self):
        return 6 * pow(self.a, 2)

    def hacim(self):
        return pow(self.a, 3)

class Kure:
    def __init__(self, r):
        self.r = r

    def yAlan(self):
        return f"Yüzey alanı: {4 * pi * pow(self.r, 2):.2f} cm²"

    def hacim(self):
        return f"Hacim: {(4/3) * pi * pow(self.r, 3):.2f} cm³"

class Silindir:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def yAlan(self):
        return f"Yüzey alanı: {2 * pi * self.r * (self.r + self.h):.2f} cm²"

    def hacim(self):
        return f"Hacim: {pi * pow(self.r, 2) * self.h:.2f} cm³"

# Nesneler oluşturuluyor
futbolTopu = Kure(10)
pinponTopu = Kure(3)

kupSeker = Kup(2)
koli = Kup(50)

merdane = Silindir(3, 30)
tencere = Silindir(15, 20)

# Test edelim
print(futbolTopu.yAlan())
print(pinponTopu.hacim())

print(kupSeker.yAlan())
print(koli.hacim())

print(merdane.yAlan())
print(tencere.hacim())
