
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
vke=round((kg/(boymt**2)),2)               # round (,2) virgülden sonra 2 değer vermek için.
                                           # **2 karesini almanın pratik yolu
if vke < 20:
    print(f"Vücut kitle endeksiniz {vke} İdeal kilonun altındasınız.")
elif vke < 25:
    print(f"Vücut kitle endeksiniz {vke} ideal kilodasınız")
elif vke < 30:
    print(f"Vücut kitle endeksiniz {vke} Fazla Kilolusunuz")
else:
    print(f"Vücut kitle endeksiniz {vke} Obezsiniz")