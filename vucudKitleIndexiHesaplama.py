
  # Vucut kitle indeksi, vucut agirliginin boy uzunlugunun karesine bolunmesiyle (gr./cm*cm) hesaplanır.
  # islemi gercekleştirip sonucu konsola yazan programi yaziniz
  # vke>30 "Obezsiniz"
  # vke>25 "Kilolusunuz"
  # vke>20 "Ideal kilodasiniz"
  # vke<20 "Zayifsiniz"


print("Vücud kitle endeksinizi ögrenmek için sırasıyla boy ve kilonuzu giriniz.")
boy=float(input("Boyunuz(cm)..:"))
boymt=(boy/100)
kg=int(input("Kilonuz(kg)..:"))
vke=kg/(boymt*boymt)
print("Vücud Kitle Indexiniz:",vke)
if vke < 20:
    print("Zayıfsınız")
elif vke < 25:
    print("ideal kilodasınız")
elif vke < 30:
    print("Fazla Kilolusunuz")
else:
    print("Obezsiniz")