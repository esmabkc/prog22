
# print("merhaba \n yakın kampüs")
# print("benim adım \tesma")

# print("benim adım {}" .format('esma'))

# print("benim adım {} , yaşım {}" .format('mesut ', 32))
# print("benim adım {0} , yaşım {1}" .format('mesut ', 32))
# print("benim adım {ad} , yaşım {yaş}" .format(ad='mesut ',yaş= 32))




# sayi=10
# print(sayi)
# sayi=11
# print(sayi)

# sayi= sayi+1
# print(sayi)

# sayi_ilk=10
# print(sayi_ilk)

# print(5)

# print(3.0*5)

# strvar="python"
# print(strvar)

# []tek bir eleman alınır
# [:]baslangıc ve bitis arasındakı elemanlar alinir
# [::]baslangıc ve bitis arasındakı elemanlar ucuncu kısımdaki degere gore atlayarak alinir






# if True:
#     print("koşul doğru")
#     print("hala if bloğunun içindeyiz")

# if ile kullanılabilecek operatörler
# eşittir"==" , eşit değildir"!=" , büyüktür ">" , küçüktür"<"  büyük veya eşittir ">=" küüçük veya eşittir "<="

# in anahtar kelimesi
# not anahtar kelimesi
# and ve or bağlaçları
# is anahtar kelimesi (hafızada aynı nesne olmalı)

# renk ="Sarı"
# if renk == "Beyaz":
#     print("Beyaz")
# elif renk == "Sarı":
#     print("Sarı") 
# elif renk =="Mavi":
#     print("Mavi")
# else:
#     print("Hiçbiri") 

# a = 5
# b = 8
# c = 10
# if a < b or c > a :
#     print ("koşul doğru")
# else:
#     print("koşul yanlış")


# liste:[1,2,3,4,5,6,7,8,9]

# a = 4
# if a in liste:
#     print("listede var")
# else:
#     print("listede yok")

# print("next")



# listeler ile for döngüsü 
# range fonksiyonu ile for döngüsü
# iç içe for döngüleri
# break ve continue anahtar kelimeleri
# while döngüsü


# liste = [1,2,3,4,5,6]

# print(liste[0])
# print(liste[1])
# print(liste[2])
# print(liste[3])

# for rakam in liste:
#     print(rakam)

# isim="esma"

# for harf in isim:
#     print(harf)

# demet=(1,2,3,4)
# for i  in demet:
#     print(i)

# for i in range(0,10):
#     print(i)   

# for i in range (2,20,3):
#     print(i)    

# sonuc=1
# for i in range(0,10):
#     sonuc *=2

# print(sonuc)

# sonuc=2
# for i in range (0,12):
#     sonuc *=3

# print(sonuc)

# liste1=["a","b","c"]
# liste2=[1,2,3,]

# for harf in  liste1:
#     for rakam in liste2:
#         print(harf,rakam)

# liste = [1,2,3,4,5,6,7,8,9]

# for i in liste:
#     if i == 3:
#         continue
#     print(i)

# liste = [1,2,3,4,5,6,7,8,9]

# for i in liste:
#     if i ==3:
#         continue
#     print(i)

# liste= range (100)

# for i in liste:
#     if i %3 !=0:
#         continue
#     print(i)

# liste= range (100)

# for i in liste:
#     if i %3 !=0:
#         continue
#     if i ==81:
#         break
#     print(i)

# x = 2

# while x < 10 :
#     print(x)
#     x += 1

# x = 10

# while x < 36 :
#     print(x)  
#     x += 5  

# x = 2

# while x < 10:
#     print(x)
#     x += 1
#     print("x=",x)


# x = 2
# y = 3

# while x*y < 1000:
#     print(x,y)
#     x += 2
#     y += 2

# i=1
# while True:
#     print(i)
#     i +=1
#     if i ==10000:
#         break

# i=1
# while True:
#     if i %2==0:
#         i+=1
#         continue
#     print(i)
#     i +=1
#     if i ==1000:
#         break


# sayi=int(input("Bir sayı giriniz:"))

# faktoriyel=1

# i=2
# while i <= sayi:
#     i *=1
    
# print(f"{sayi}!={faktoriyel}")

sayi=int(input("Bir sayı giriniz:"))

prime=True

for i in range (2,sayi):
    if sayi %i==0:
        prime=False
        break
if prime==True:
    print(f"{sayi}sayısı asaldır")
else:
    print(f"{sayı} sayısı asal değildir")
