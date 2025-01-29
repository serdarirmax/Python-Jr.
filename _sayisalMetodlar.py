#####################  .__abs__()  ##############################
x=-2
print(x.__abs__())  # mutlak değer
#####################     pow()    ##############################
x=3
print(pow(x,3)) # 27 döndürür. x'in 3üncü kuvvetini aldı.
print(x.__pow__(3)) # şeklilde metod olarakta kullanılır.
#####################  .__divmod__()  ###########################
x=15
print(x.__divmod__(2))  # (7,1)  Bölüm ve kalanı bize demet olarak döndürür.
##################### .as_integer_ratio() #######################
x=5.2
print(x.as_integer_ratio())  # 5.2 sayısını yakalayabilmek için hangi sayının hangi
                             # sayıya bölünmesi gerektiğini döndürür. (5854679515581645, 1125899906842624)
#####################  .is_integer()  ###########################
x=5.0
print(x.is_integer())  # sayısal yapı float ise ve , den sonrası 0 ise True döndürür.








