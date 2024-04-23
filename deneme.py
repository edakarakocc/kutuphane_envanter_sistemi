def kullanici():
    print( '''
        1-Personel
        2-Öğrenci
        3-Çıkış
        ''')
def kayit_sorgulama():
    print( '''
        1-Kayıtlı kişi
        2-Yeni kayıt
        3-Çıkış
        ''')  
def menu_goruntule():
    print('''
        1-Kitap ekle
        2-Kitap güncelle
        3-Kitap sil
        4-Çıkış
          ''')
def menu_goruntule2():
     print('''
        1-Ödünç al
        2-İade et
        3-Mevcut kitapları görüntüle
        4-Çıkış
          ''') 

def kitapekle():
    kitaplar = open('kitaplar.txt','a')
    
    kitap_adi = input("Eklemek istediğiniz kitabın adını girin: ")
    yazar_adi = input("Yazarın adını giriniz: ")
    ISBN = input("Kitabın ISBN numarasını giriniz: ")
    yayin_evi = input("Kitabın yayınevini girin: ")
    yayin_yili = input("Kitabın yayın yılını girin: ")
    kitap_turu = input("Kitabın türünü girin: ")
    kitaplar.write(f"{kitap_adi},{yazar_adi},{ISBN},{yayin_evi},{yayin_yili},{kitap_turu},mevcut\n")
    print("Kitap başarıyla eklendi")

def kitap_guncelle():
    with open('kitaplar.txt','r') as dosya:
        icerik = dosya.readlines()
    kitap_adi = input("Güncellemek istediğiniz kitabın adını girin: ").lower()
    
    print('''
        1- Kitap Adı
        2- Yazar Adı
        3- ISBN Numarası
        4- Yayınevi
        5- Yayın Yılı
        6- Kitap Türü
        ''')
    
    secim = input("Hangi bilgiyi güncellemek istediğinizi seçin:")
    
    with open('kitaplar.txt','w') as dosya:
        kitap_bulundu = False
        for satir in icerik:
            satir_bolumleri = satir.strip().split(",")
            
            if kitap_adi == satir_bolumleri[0].lower():
                kitap_bulundu = True
                if secim == '1':
                    guncel_bilgi= input("Güncel kitap adını giriniz: ")
                elif secim == '2':
                    guncel_bilgi = input("Güncel yazar adını giriniz:")
                elif secim == '3':
                    guncel_bilgi = input("Güncel ISBN numarasını giriniz:")
                elif secim == '4':
                    guncel_bilgi = input("Güncel yayınevini giriniz: ")
                elif secim == '5':
                    guncel_bilgi = input("Guncel yayın yılını giriniz: ")
                elif secim == '6':
                    guncel_bilgi = input("Guncel kitap türünü giriniz: ")
                else:
                    print("Yanlış tercihte bulundunuz.")
                    break
                
                satir_bolumleri[int(secim)-1] = guncel_bilgi        
                dosya.write(",".join(satir_bolumleri)+ "\n")
                print("Kitap başarıyla güncellendi.")
                
            else:
                dosya.write(satir)
        
        if not kitap_bulundu:
            print("Güncellenecek kitap bulunamadı.")


def kitapsil():
    with open('kitaplar.txt','r') as dosya:
        icerik = dosya.readlines()
    kitap_adi = input("Silmek istediğiniz kitabın adını girin: ")
    with open('kitaplar.txt','w') as dosya:
            for satir in icerik:
                satir_bolumleri = satir.strip().split(",")
                
                if kitap_adi != satir_bolumleri[0].lower():
                    dosya.write(satir)

    print("Kitap başarıyla silindi")
    
def mevcut_kitaplar():
    with open('kitaplar.txt', 'r') as dosya:
            icerik = dosya.readlines()
        
    kitap_turu = input("Aradığınız kitap türünü girin: ")
    mevcut_kitaplar = []
    for satir in icerik:
        kitap_bilgileri = satir.strip().split(",")
        if len(kitap_bilgileri)>=6 and kitap_turu.lower() in kitap_bilgileri[5].lower():
                mevcut_kitaplar.append(kitap_bilgileri[0])   
        
    if mevcut_kitaplar:
        print("Mevcut Kitaplar:")
        print("\n".join(mevcut_kitaplar)) 
        return mevcut_kitaplar
    else:
        print("Aradığınız türde bir kitap bulunamadı.")
        return None

        
def odunc_alma():
    with open('kitaplar.txt','r') as dosya:
        icerik=dosya.readlines()
    secilen_kitap=input("Ödünç almak istediğiniz kitabın adını giriniz: ")
    
    kitap_bulundu = False
    for satir in icerik:
        mevcutluk= satir.strip().split(",")
        if mevcutluk[0] == secilen_kitap and mevcutluk[6] == 'mevcut':
            kitap_bulundu = True
            break
    if kitap_bulundu:
            print("Kitap ödünç alınabilir.")
            with open('ogrenciler.txt','r') as ogrenciler:
                ogrenci=ogrenciler.readlines()
                
            alici=input("Alıcı öğrencinin adını giriniz: ")
            
            ogrenci_bulundu = False
            for satir in ogrenci:
                if alici in satir:
                    ogrenci_bulundu = True
                    alici_bilgileri=satir.strip()
                    break
            
            if ogrenci_bulundu:
                with open('odunc.txt','a') as odunc_dosya:
                    odunc_dosya.write(f"{alici_bilgileri},{secilen_kitap}\n")
                    
                with open('kitaplar.txt','w') as kitap_dosya:
                    for satir in icerik:
                        satir_bolumleri = satir.strip().split(",")
                        if satir_bolumleri[0]==secilen_kitap:
                            satir_bolumleri[6]='alındı'
                            print("Kitap 15 gün içerisinde kütüphaneye teslim edilmelidir.")

                        kitap_dosya.write(",".join(satir_bolumleri)+ "\n")
            else:
                print("Öğrenci bulunamadı.")
    else:
        print("Kitap bulunmuyor veya ödünç alınmış.")

def kitap_iade():
    with open('odunc.txt', 'r') as dosya:
        icerik = dosya.readlines()

    kitap_adi = input("İade edilecek kitabın adını giriniz: ")
    
    kitap_bulundu = False
    for i, satir in enumerate(icerik):
        if kitap_adi in satir and 'iade edildi' not in satir:
            kitap_bulundu = True
            icerik[i] = satir.strip()+",iade edildi\n"
            break
    
    if kitap_bulundu:
        print("Kitap başarıyla iade edildi.")
        with open('odunc.txt', 'w') as dosya:
            dosya.writelines(icerik)
        with open('kitaplar.txt', 'r') as kitap_dosya:
            kitaplar = kitap_dosya.readlines()
        with open('kitaplar.txt', 'w') as kitap_dosya:
            for satir in kitaplar:
                kitap_bilgileri = satir.strip().split(",")
                if kitap_bilgileri[0] == kitap_adi:
                    kitap_bilgileri[6] = 'mevcut'
                kitap_dosya.write(",".join(kitap_bilgileri) + "\n")
    else:
        print("İade edilen kitap bulunamadı.") 
