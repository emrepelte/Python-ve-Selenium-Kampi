# Veri Tipleri:
# int: Tam sayıları ifade eder. 1845,  26  ...
# float: Ondalıklı sayıları gösterir. Örneğin; 3.14, 2.48 vs.
# str: Metinsel veri tipidir. "Merhaba" , "Hoşgeldin" vs.
# bool: Matıksal verileri ifade eder. True ya da False döndürülür.
# list: Aynı veri tipine sahip değerleri birarada bulundurur. Örneğin;[12,45,36 veya "Merhaba","Hoşgeldiniz"] vs.
# tuple: Aynı veri tipine sahip değerleri birarada bulundurur. Örneğin; (12,45,36,48,22,33) vs.
# set: Aynı veri tipine sahip değerleri birarada bulundurur. Örneğin; {12,45,36} vs.
# dict: Farklı veri tipine sahip değerleri birarada bulundurur. Örneğin; {"ad":"hilal", "yas" : 30, "memleket": "ankara"} vs.

kullaniciAdi="deneme123"
sifre="142536"

kullaniciAdi=input("Kullanıcı adınızı giriniz: ")
sifre1=input("Şifrenizi giriniz: ")

if kullaniciAdi==kullaniciAdi and sifre1==sifre:
    print("Giriş Yapıldı")
else:
    print("Kullanıcı adı veya şifre hatalı")