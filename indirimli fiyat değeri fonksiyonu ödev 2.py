a=float(input("Fiyat girin: "))
b=float(input("İndirim yüzdesi girin (%): "))

def indirim_hesapla():
    fiyat = a
    yuzde = b

    indirim = fiyat * (yuzde / 100)
    son_fiyat = fiyat - indirim

    print("İndirim Tutarı:", indirim)
    print("Son Fiyat:", son_fiyat)


indirim_hesapla()
