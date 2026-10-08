while True:
    print("1 = tambah, 2 = kurang, 3 = kali, 4 = bagi, 0 = keluar")
    try:
        operasi = int(input("Pilih operasi : "))
        if operasi==0:
            break

        a = float(input("masukan angka pertama : "))
        b = float(input("masukan angka kedua : "))

        match operasi:
            case 1 : print(f"Hasil dari penjumlahan kamu adalah : {a + b}")
            case 2 : print(f"Hasil dari perkurangan kamu : {a - b}")
            case 3 : print(f"Hasil dari perkalian kamu : {a * b}")
            case 4 : 
                if b == 0:
                    print("Tidak bisa di bagi dengan 0")
                else:
                    print(f"Hasil dari Pembagian kamu : {a / b}")
            case _: print("Pilihan Tidak ada")

    except ValueError:
        print("masukan dengan benar dan harus menggunakan angka yaaa")
