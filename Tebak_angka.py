import random

angka_rahasia = random.randint(1,20)
sedang_bermain = True
percobaan = 0

print(" === SELAMAT BERMAIN TEBAK ANGKA ===")

while sedang_bermain:
    try:
        Tebakan = int(input("Tebak Angka Dari 1 - 20 : "))
    except ValueError:
        print("Masukan Angka yaaa")
        continue

    percobaan += 1
    
    if Tebakan == angka_rahasia:
        print(f"Tebakan kamu benar dan kamu cuman membutuhkan {percobaan}")
        break
    elif Tebakan < angka_rahasia:
        print("Tebakan kamu terlalu kecil, ayo naikan lagi")
    else:
        print("Tebakan kamu terlalu besar, coba kecilkan lagi")