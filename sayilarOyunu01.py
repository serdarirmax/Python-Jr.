# 0dan 100'e kadar yazan ama 7 ve katları olunca yazmayan bir döngü oluştıralım

#for i in range(101):
#    if (i%7==0):
#        continue
#    print(i)

i=0
while i <= 100:
    if (i%7!=0):
       print(i)
    i+=1
