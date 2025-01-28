# 2nin üssel olarak istenilen parametreyi verilerek
# çalışacak fonksiyonu olusturunuz?


def ikiussu(b):
    if b==0:
        return 1
    else:
        return (2*ikiussu(b-1))

print(ikiussu(8))