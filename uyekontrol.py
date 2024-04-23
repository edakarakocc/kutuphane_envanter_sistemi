def personel_kontrol():
    global kontrol
    x = False
    ad = input("Adınızı girin:")
    soyad = input("Soyadınızı girin:")
    sifre = input("Şifrenizi girin:")
    
    with open("personeller.txt", "r") as dosya:
        for satir in dosya:
            icerik = satir.strip().split(",")
            if len(icerik) == 3: 
                if icerik[0] == ad and icerik[1] == soyad and icerik[2] == sifre:
                    print("\nDoğrulama başarılı")
                    x = True
                    break             
    kontrol = x
    return kontrol

def ogrenci_kontrol():
    global dogrumu
    x = False
    ad = input("Adınızı girin:")
    soyad = input("Soyadınızı girin:")
    sifre = input("Şifrenizi girin:")
    
    with open("ogrenciler.txt", "r") as dosya:
        for satir in dosya:
            icerik = satir.strip().split(",")
            if len(icerik) == 3:  
                if icerik[0] == ad and icerik[1] == soyad and icerik[2] == sifre:
                    print("\nDoğrulama başarılı")
                    x = True
                    break              
    dogrumu = x
    return dogrumu
