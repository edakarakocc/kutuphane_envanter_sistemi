import deneme
def main():
    while True:
        deneme.kullanici()
        yetkilendirme = input("Bir seçenek giriniz: ")
        
        if yetkilendirme=='1':
            while True:
                deneme.kayit_sorgulama()
                kayit = input("Bir seçenek giriniz: ")
                
                if kayit=='1':
                    ad=input("Personel adı: ")
                    soyad=input("Personel soyadı: ")
                    id=input("Personel ID: ")
                    
                    with open('personeller.txt','r') as calisan:
                        icerik=calisan.readlines()
                        for satir in icerik:
                            personel_bilgileri = satir.strip().split(",")
                            if ad in personel_bilgileri and soyad in personel_bilgileri and id in personel_bilgileri:
                                print("..Giriş başarılı..")
                                
                                while True:
                                    deneme.menu_goruntule()
                                    tercih=input("Bir seçenek girin: ")
                                    if tercih == '4':
                                        return
                                    elif tercih=='1':
                                        deneme.kitapekle()
                                    elif tercih=='2':
                                        deneme.kitap_guncelle()
                                    elif tercih=='3':
                                        deneme.kitapsil()
                                    else:
                                        print("Yanlış tercihte bulundunuz.")
                                    
                                    devam=input("Devam etmek istiyor musunuz? (evet/'e', hayır/'h'): ")
                                    if devam=='h' or devam=='H':
                                        return            
                        else:
                            print("Kayıtlı kullanıcı bulunamadı.")
                            break
                                
                elif kayit=='2':
                    with open('personeller.txt','a') as calisan:
                        ad=input("Personel adı: ")
                        soyad=input("Personel soyadı: ")
                        id=input("Personel ID: ")
                        calisan.write(f"{ad},{soyad},{id}\n")
                        print("Başarıyla kayıt olundu.")   
                        
                        while True:
                            deneme.menu_goruntule()
                            tercih=input("Bir seçenek girin: ")
                            if tercih == '4':
                                return
                            elif tercih=='1':           
                                deneme.kitapekle()
                            elif tercih=='2':
                                deneme.kitap_guncelle()
                            elif tercih=='3':
                                deneme.kitapsil()
                            else:
                                print("Yanlış tercihte bulundunuz.")
                            devam=input("Devam etmek istiyor musunuz? (evet/'e' , hayır/'h'): ")
                            if devam == 'h' or devam =='H':
                                return
                elif kayit=='3':   
                    break
                break    
                
        elif yetkilendirme=='2':
            while True:
                deneme.kayit_sorgulama()
                kayit = input("Bir seçenek giriniz: ")
                
                if kayit=='1':
                    ad=input("Öğrencinin Adı: ")
                    soyad=input("Öğrencinin Soyadı: ")
                    no=input("Öğrencinin Numarası: ")
                    
                    with open('ogrenciler.txt','r') as ogrenciler:
                        kisiler=ogrenciler.readlines()
                        for satir in kisiler:
                            ogrenci_bilgileri=satir.strip().split(",")
                            if ad in ogrenci_bilgileri and soyad in ogrenci_bilgileri and no in ogrenci_bilgileri:
                                while True:
                                    deneme.menu_goruntule2()
                                    tercih=input("Bir seçenek girin: ")
                                    if tercih=='4':
                                        return
                                    elif tercih=='1':
                                        deneme.odunc_alma()
                                    elif tercih=='2':
                                        deneme.kitap_iade()
                                    elif tercih=='3':
                                        deneme.mevcut_kitaplar()
                                    else:
                                        print("Yanlış tercihte bulundunuz")
                                                
                                    devam=input("Devam etmek istiyor musunuz? (evet/'e', hayır/'h'): ")
                                    if devam=='h' or devam=='H':
                                        return
                        else:
                            print("Kayıtlı öğrenci bulunamadı.")
                            break
                
                elif kayit=='2':
                    with open('ogrenciler.txt','a') as ogrenciler:
                            ad=input("Öğrencinin Adı: ")
                            soyad=input("Öğrencinin Soyadı: ")
                            no=input("Öğrencinin Numarası: ")
                            
                            ogrenciler.write(f"{ad},{soyad},{no}\n")
                            print("Başarıyla kayıt olundu.")
                            
                            while True:
                                deneme.menu_goruntule2()
                                tercih=input("Bir seçenek girin: ")
                                if tercih=='4':
                                    return
                                elif tercih=='1':
                                    deneme.odunc_alma()
                                elif tercih=='2':
                                    deneme.kitap_iade()
                                elif tercih=='3':
                                    deneme.mevcut_kitaplar()
                                else:
                                    print("Yanlış tercihte bulundunuz")
                                                
                                devam=input("Devam etmek istiyor musunuz? (evet/'e', hayır/'h'): ")
                                if devam=='h' or devam=='H':
                                    return
                elif kayit=='3':
                    break
                break
                
        elif yetkilendirme=='3':
            break
        else:
            print("Yanlış seçimde bulundunuz.")
            break
            
if __name__ == "__main__":
    main()
