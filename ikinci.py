# control flow
# akışı kontrol et!

# a =3
# b =5

a , b= 3 , 5

# code block

# mesela C dillerinde kod blokları{ }
# if a > b { print....}
a , b=b , a
a=b
# if a > b:
#     print("a b'den büyük")
#     print("a:",  a ,"b:" ,b) 
#     # else
 # else :
#      print("a b'den büyük değil...")
# elif a < b :
#     print("a b'den küçük")
# #  elif a==b:
# else:
#     print("a b'ye eşit") 

# pass


# blok nesnesi başladı ise kesinlikle altında girinti bekler.
# if 4 < 1 :

# pass
# if 4>1 :
    # print("bu doğru bir durum!")

# değişken_adı = 5
# print ( type( değişken_adı) )

# kesir=3 / 7
# float kesir tipli değişken.
# ondalık olarak nokta (.) işareti kullanılır!
# kesir =3.14159265
# print( type(kesir) ,kesir)

# metin = "metin tipinde"
# #  str - string metin tipinde bir değişken.
# print ( type( metin) )
# x ="5" #str
# y = 5 #int
# z=5.0 # float

# print(x==y)
# x==y ? eşit değildir. print (type(x) == type(y))
# y==z ? eşit


# t =False 
# t =True 
#  bool -Boolean /Doğru -Yanlış tipli değişken
#  Doğru True
#  Yanlış False
# print( type( t ))

# Doğru yanlış tipi değeri ilk harfi büyük yazılır.
# True =5 anahtar kelime olduğu için değişken olamaz.
#  true= 5 değişken  olabilir

# a = 4
# b=" bir daha yaramazlık yapmayacağım! \n"
# print  ( a * b )

# a = 5
# b = "dünya"
# c= str(a) + b

# print(c)

# z ="55.2"
# x ="23"

# print( int(X)+ float(z) )
# t = "False"
# print( bool(t))

# t=0
# print (t==False)
# t= 1
# print ( t==True)

# import random

# rasgele = random.randrange(1,10)

# kul_veri = input("1 ve 10 arası rasgele sayı giriniz:")
# if kul_veri==rasgele:
#     print("Tebrikler Sayıyı Buldunuz!!!!")
# else:
#     print("Bilgisayarın tuttuğu sayı:",rasgele)
#     print("Sizin girdiğiniz sayı:", kul_veri)
#     print("Lütfen yeniden deneyin!")

# iç içe if durumları 
# a , b ,c = 1 , 2, 3

# if 3>1:
#     print("3 bir rakamından  büyük")
#     if 3 > 2:
#     print("2 rakamından da büyük")
#     if 3==3:
#         print("bu değerler birbirine eşit")
#         else:
#             print("eşit değil")
#         print("Bu kimin altında?")
#    print("Bu kimin altında?")
# else:
#     print("3 rakamından büyük değil.")

# bir den fazla şart bulunduran durumlar

if 3 >2 and 2>1 :
        print("iki şart da doğru")
# bazı eşit değildir operatörü" <>

if 3>=2 and 3 <=4 and 3<4 and 3!=4:
        print ("tüm şartlar doğru.")

# print (True and True)
# print (1 and 1)
# print (False and False)
# print (0 and 0)
# print (True and False)
# print (1 and 0)
# print(False and True)
# print (0 and 1)

# print (True or False)
# print(False or False)
# print(False or False)

# if (True and False) or (False or True):
# if ((True and False) or False) or True:
# if True and (False or (False or True)): 
    # print("çalışır mı?")

import math
print("Çıkmak için -1 yazınız")

vize=int ( input("Vize sonucunu giriniz:"))
if vize<50:
    final_için_gerekli_not=( 50-0.4*vize)/0.6
    print ("Final için almanız gereken not :" , math.ceil(final_icin_gerekli_not))

if final_icin_gerekli_not >=50:
    print("final için almanız gereken not:50")


