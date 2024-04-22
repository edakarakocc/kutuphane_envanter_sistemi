def personel_kontrol():
    global kontrol
    x=False
    ad=input("Adinizi girin:")
    soyad=input("Sayadinizi girin:")
    sifre=input("Sifrenizi girin:")
    with open("personeller.txt","r") as dosya:
        liste=[]
        for satir in dosya:
            icerik=satir.strip().split(",")
            liste.append(icerik)
        personelmi=[]
        personelmi.append(ad)
        personelmi.append(soyad)
        personelmi.append(sifre)
    for i in range(len(liste)):
        if liste[i][2]==personelmi[2] and liste[i][1]==personelmi[1]:
            if liste[i][0]==personelmi[0]:
                print("\nDogrulama basarili")
                x=True
            else:
                x=False
    if x:
        kontrol=True
    else:
        kontrol=False
    personelmi=[]
    return kontrol
def ogrenci_kontrol():
    global dogrumu
    x=False
    ad=input("Adinizi girin:")
    soyad=input("Sayadinizi girin:")
    sifre=input("Sifrenizi girin:")
    with open("ogrenciler.txt","r") as file:
        liste=[]
        for satir in file:
            icerik=satir.strip().split(",")
            liste.append(icerik)
    ogrencimi=[]
    ogrencimi.append(ad)
    ogrencimi.append(soyad)
    ogrencimi.append(sifre)
    for i in range(len(liste)):
        if liste[i][2]==ogrencimi[2] and liste[i][1]==ogrencimi[1]:
            if liste[i][0]==ogrencimi[0]:
                print("\nDogrulama basarili")
                x=True
            else:
                x=False
    if x:
        dogrumu=True
    else:
        dogrumu=False 
    ogrencimi=[]
    return dogrumu