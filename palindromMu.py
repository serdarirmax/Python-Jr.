
# Bir String‘in palindrom olup olmadığını kontrol etmek icin kod yaziniz.
# palindrom: Bir kelime, cumle veya rakamlar dizisinin tersten okunusunun aynı şeyi vermesi.
#########################################################
str="ey edip adanada pide ye"
str2= str[::-1]
if str==str2:
    print('"'+str2+'"'+" BİR PALİNDROMDUR.")
#########################################################
str3="ey edip adanada pide ye"
str4=str3[::-1]
print("Palindrom mudur? >> ",str3==str4)
#########################################################
str5="ey edip adanada pide ye"
str6=''.join(str5)
print("Palindrom mudur? >> ",str5==str6)
#########################################################
str7="ey edip adanada pide ye"
print(len(str7)-1)
str8=""
#if x in range(0,len(str7)-1):
#    str8+=str7[:-1]
#    print(str8)
#    str8+=str8.append(str7[len(str7):])
#    print(str8)
