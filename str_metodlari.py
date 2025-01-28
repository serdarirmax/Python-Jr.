########################## .lower() ###################################
x="1- Python ögrenmesi çok eğlenceli ve BEYİN gıdıklayıcı bir aktivite."
x2=x.lower() # tüm string ifadeleri lowercase e dönüştürür.
print(x2)
########################## .upper() ###################################
x3="1- Python ögrenmesi çok eğlenceli ve BEYİN gıdıklayıcı bir aktivite."
x4=x3.upper() # tüm string ifadeleri uppercase e dönüştürür.
print(x4)
######################### .islower() ##################################
x5="1- python ögrenmesi çok eğlenceli ve beyin gıdıklayıcı bir aktivite."
x6=x5.islower() # tüm string küçük harflerden mi olusuyor? True & False
print(x6)
######################### .isupper() ##################################
x7="1- Python ögrenmesi çok eğlenceli ve beyin gıdıklayıcı bir aktivite."
x8=x7.isupper() # tüm string büyük harflerden mi olusuyor? True & False
print(x8)
######################### .isnumeric() ################################
x9="1996"
x10=x9.isnumeric() # numerik karakterlerden mi oluşuyor? True & False
print(x10)
######################### .isalnum() ##################################
x11="1994GeorgeOrwel"
x12=x11.isalnum() # tüm string harfler ve rakamlardan mi olusuyor? True & False
print(x12)        # arada space varsa false olur dikkat et!!
######################### .capitalize() ###############################
x13="cemal süreyya"
x14=x13.capitalize() # String başındaki harfi büyük yapar
print(x14)
######################### .title()  ###################################
x15="""İyiki bimiyor kalabalıklar 
Yağmura bakmayı cam arkasından.
Şükürki insandan insan fark var, 
İyiki bilmiyor kalabalıklar."""
x16=x15.title() # Stringteki tüm cümlelerin ilk harfini büyük yapar.
print(x16)
######################### .swapcase() #################################
x17="cemal süreyya"
x18=x17.swapcase() # büyük harfleri küçük, küçük harfleride büyük yapar.
print(x18)
######################### .count("s") #################################
x19="şemsi paşa pasajında sesi büzüşeseciler"
x20=x19.count("s") # saymak istediğin harfi veya metni parametre olarak girmelisin
print(x20)
######################### .strip(" ") #################################
x21=" bastan ve sondan boşluk bıraktım      "
x22=x21.strip(" ") # Alacagı parametreyi bastan ve sondan arar bulursa kesip atar.
print(x22)         # Bosluklar için kullanılır genelde
                   # .rstrip(" ") right ve .lstrip(" ") left şeklinde de kullanılır.
############## .split(" ")  #######  " ".join()    ####################
x23="şemsi paşa pasajında sesi büzüşeseciler"
x24=x23.split(" ") # alınan parametreye göre parçalama yapar.
print(x24)
x25=" ".join(x24) # split in tersdir, parçalananları birleştirebilirsin.
print(x25)
######################### .find() ######################################
x26="I love python"
print(x26.find("love")) # alınan parametreye göre indeks araması yapar ve döndürür.
######################### .find() ######################################


######################### .find() ######################################

######################### .find() ######################################

######################### .find() ######################################