def personel_ekle():
    try:
          global personel_ad
          personel_ad=input("Adınızı girin:")
          global personel_soyad
          personel_soyad=input("Soyadınızı girin:")
    except:
        print("!!!Hatali tipte giriş yaptınız girdiğiniz bilgileri tekrar kontrol edin.!!!")
    global personel_sifre
    personel_sifre=(len(personel_ad)+len(personel_soyad))*3
    print("Şifreniz:",personel_sifre,"kimseyle paylaşmayınız")
    with open("personeller.txt","a") as f:
        f.write(f"{personel_ad},{personel_soyad},{str(personel_sifre)}\n")
def ogrenci_ekle():
    try:
        global ogrenciAd
        ogrenciAd=input("Adınızı girin:")   #kullanicidan bilgiler isteniyor
        global ogrenciSoyad
        ogrenciSoyad=input("Soyadınızı girin:")
    except:
        print("!!!Hatali tipte giriş yaptınız girdiğiniz bilgileri tekrar kontrol edin.!!!")
    global ogrenci_sifre
    ogrenci_sifre=(len(ogrenciAd)+len(ogrenciSoyad))*11
    print("Şifreniz:",ogrenci_sifre,"kimseyle paylaşmayınız")
    with open("ogrenciler.txt","a") as file:
        file.write(f"{ogrenciAd},{ogrenciSoyad},{str(ogrenci_sifre)}\n")
