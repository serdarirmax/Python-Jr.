# Kürenin hacmini ve yüzey alanini hesaplayan kodu yazınız
import math
r=int(input("yarıcapı gir: "))
Hacim=(4/3)*math.pi * pow(r,3)
Alan=4*math.pi*pow(r,2)
print("Kürenin Hacmi : ",Hacim,"m^3\nKürenin Yüzey Alanı : ",Alan,"m^2")
