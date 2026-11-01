def harf_notu_hesaplama():
    a = float(input("Vize notunuzu giriniz: "))
    b = float(input("Final notunuzu giriniz: "))
    ortalama = a * 0.4 + b * 0.6

    if ortalama >= 90:
        harf = "AA"
    elif ortalama >= 85:
        harf = "BA"
    elif ortalama >= 80:
        harf = "BB"
    elif ortalama >= 75:
        harf = "CB"
    elif ortalama >= 70:
        harf = "CC"
    elif ortalama >= 65:
        harf = "DC"
    elif ortalama >= 60:
        harf = "DD"
    elif ortalama >= 50:
        harf = "FD"
    else:
        harf = "FF"

   
    print("Ortalamanız:", ortalama)
    print("Harf notunuz:", harf)
harf_notu_hesaplama()
