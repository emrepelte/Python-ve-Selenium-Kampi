liste = []

def ekleOgrenci():
    liste.append(input("Lütfen kaydetmek istediğiniz öğrencinin adı ve soyadını giriniz: "))
    print("Öğrenci listeye eklendi.")
    print(liste)

    i = 120
    print("*"*i)

def silOgrenci():
    liste.remove(input("Lütfen listeden silmek istediğiniz öğrencininin adı ve soyadını giriniz: "))
    print("Öğrenci listeden çıkarılmıştır.")
    print(liste)

    i = 120
    print("*"*i)

def ekleBirdenCok():
    while True:
        ogrenci = input("Lütfen kaydetmek istediğiniz öğrencinin adı ve soyadını giriniz(Ekleyeceğiniz öğrenci bittiğinde 0 yazarak ekleme işlemini bitirebilirsiniz): ")
        if ogrenci == str(0):
            break
        liste.append(ogrenci)
    print("Yazdığınız öğrenci isimleri listeye eklenmiştir. '0' a bastığınız için ekleme işlemi bitirilmiştir. Yazdığınız isimlerin listesi şu şekildedir: ")
    print(liste)

    i = 120
    print("*"*i)

def tektekYazdir():
    for i in range(len(liste)):
        print(liste[i])

    i = 120
    print("*"*i)

def ogrenciNumaraOgren():
    print(liste)
    ogr = input("Lütfen numarasını öğrenmek istediğiniz öğrencinin listedeki şekilde adını ve soyadını giriniz: ")
    i = 0
    while i <= len(liste):
        if liste[i] == ogr:
            print(i)
            break
        i += 1

    i = 120
    print("*"*i)


liste2 = []

def silOgrenciBirdenCok():
    while True:
        ogr2 = input("Lütfen kaydını silmek istediğiniz öğrencinin adı ve soyadını giriniz(Kayıt listesinden silmek istediğiniz öğrenciler bittiğinde 0 yazarak silme işlemini bitirebilirsiniz): ")
        if ogr2 == str(0):
            print("Kayıt silme işlemi bitmiştir. Listenin son hali aşağıdaki gibidir.")
            print(liste)
            break
        liste.remove(ogr2)
        liste2.append(ogr2)
        print("Kaydını sildiğiniz öğrenci listesi şu şekildedir: ")
        print(liste2)

    i = 120
    print("*"*i)

ekleOgrenci()
silOgrenci()
ekleBirdenCok()
tektekYazdir()
ogrenciNumaraOgren()
silOgrenciBirdenCok()
