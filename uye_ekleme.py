def personel_ekle():
    try:
          global personel_ad
          personel_ad=input("Adinizi girin:")
          global personel_soyad
          personel_soyad=input("Soyadinizi girin:")
    except:
        print("!!!Hatali tipte giris yaptiniz girdiğiniz bilgileri tekrar kontrol edin.!!!")
    global personel_sifre
    personel_sifre=(len(personel_ad)+len(personel_soyad))*3
    print("Sifreniz:",personel_sifre,"kimseyle paylaşmayiniz")
    with open("personeller.txt","a") as f:
        f.write(f"{personel_ad},{personel_soyad},{str(personel_sifre)}\n")
def ogrenci_ekle():
    try:
        global ogrenciAd
        ogrenciAd=input("Adinizi girin:")   #kullanicidan bilgiler isteniyor
        global ogrenciSoyad
        ogrenciSoyad=input("Soyadinizi girin:")
    except:
        print("!!!Hatali tipte giris yaptiniz girdiğiniz bilgileri tekrar kontrol edin.!!!")
    global ogrenci_sifre
    ogrenci_sifre=(len(ogrenciAd)+len(ogrenciSoyad))*11
    print("Sifreniz:",ogrenci_sifre,"kimseyle paylaşmayiniz")
    with open("ogrenciler.txt","a") as file:
        file.write(f"{ogrenciAd},{ogrenciSoyad},{str(ogrenci_sifre)}\n")