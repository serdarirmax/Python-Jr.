# tc no ya göre yeni gelenlere sıra no veren 0 ile doktora yönlendiren istenirse tc no ile
# kacıncı sırada oldugunu ögrenebileceğin bir proram yazalım.
sira=[]
while True:
    tc=int(input("TC No giriniz:"))
    if tc in sira:
        i=sira.index(tc)
        print("Bekleyen kişiler arasında ",i+1+". sıradasınız.")
    elif tc==0:
        print(sira[0],"TC Nolu hasta Doktor görüşmesi için içeri giriniz")
        sira.pop(0)
    else:
        sira.append(tc)
        print(tc, "numaralı hasta sıraya alındı.")

# aynı tc yi girince hata veriyor. üzerinde calışmak lazım.
