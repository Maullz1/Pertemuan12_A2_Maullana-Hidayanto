def persegi(): 
    print ("Menghitung Luas Persegi Panjang") 
    p = int(input("Masukkan Panjang : ")) 
    l = int(input("Masukkan Lebar : ")) 
    luas = p*l 
    print ("Luas Persegi Panjang adalah ",luas) 
    print ()
    print ("Coba lagi [Y/N]? ") 
    back = input().upper() 
    if back == "Y": 
        menu() 
    else: 
        exit()  
def lingkaran(): 
    print ("Menghitung Luas Lingkaran") 
    r = int(input("Masukkan Jari-Jari : ")) 
    luas = 3.14*(r**2) 
    print ("Luas Lingkaran adalah ",luas) 
    print ()
    print ("Coba lagi [Y/N]? ") 
    back = input().upper() 
    if back == "Y": 
        menu() 
    else: 
        exit()  
def segitiga(): 
    print ("Menghitung Luas Segitiga")
    a = int(input("Masukkan Alas : ")) 
    t = int(input("Masukkan Tinggi : ")) 
    luas = (a*t)/2 
    print ("Luas Segitiga adalah ",luas)
    print ()
    print ("Coba lagi [Y/N]? ")
    back = input().upper() 
    if back == "Y": 
        menu() 
    else: 
        exit()
def menu(): 
    print ("Pilih Bentuk 2D") 
    print ()
    print ("1. Persegi Panjang")
    print ("2. Lingkaran")
    print ("3. Segitiga") 
    print ("4. Keluar")
print("------------------------------------------------------------")
print("Selamat Datang di program untuk Menghitung Luas Bangun Datar")
print("------------------------------------------------------------")
print()
menu()
while 1:
    pilih = input("Masukkan pilihan : ")
    if pilih == "1":
        persegi()
    elif pilih == "2":
        lingkaran()
    elif pilih == "3":
        segitiga()
    else:
        print("Maaf, pilihan yang anda masukkan tidak terdaftar")
print("Coba lagi [Y/N]? ")
coba = input().upper()
if coba == "Y":
    menu()
else:
    print("\n yasudah kalo begitu")