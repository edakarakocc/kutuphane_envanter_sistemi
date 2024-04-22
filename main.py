import uye_ekleme
import deneme
import uyekontrol
def main():
    while True:
        deneme.kullanici()
        yetkilendirme = input("Bir seçenek giriniz: ")
        
        if yetkilendirme=='1':
            while True:
                deneme.kayit_sorgulama()
                kayit = input("Bir seçenek giriniz: ")
                
                if kayit=='1':
                    if uyekontrol.personel_kontrol():
                        print("\nAsağida menu ekrani bulunmaktadir")
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
                        print("Kayıtlı Personel bulunamadı.")
                        break
                                
                elif kayit=='2':
                    uye_ekleme.personel_ekle()
                    print("\n\n\nBaşarili bir sekilde kayıt tamamlandi.\n\nAsagıda menu ekrani bulunmaktadir.")
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
                    if uyekontrol.ogrenci_kontrol():
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
                    uye_ekleme.ogrenci_ekle()
                    print("Başarıyla kayıt olundu.\n\nAsagıda menu ekrani bulunmaktadir.")
                            
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
