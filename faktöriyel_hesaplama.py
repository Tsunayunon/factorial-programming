def faktoriyel_hesaplama():
    x = int(input("Bir sayı giriniz: "))
    y = 1

    while x > 0:
        y *= x
        x -= 1
    
    print(y)  # Faktöriyel hesaplamanın sonucunu yazdır

faktoriyel_hesaplama()
