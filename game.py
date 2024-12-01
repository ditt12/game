import random
import time
import os

def acak_gelas():
    print("mengacak posisi gelas...", end="", flush=True)
    for _ in range(5):
        for simbol in [".", "..", "..."]:
            print(f"\r{simbol}", end="", flush=True)
            time.sleep(0.3)
    print("\racak selesai! ", end="", flush=True)

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def warna_merah(teks):
    return f"\033[91m{teks}\033[0m"

def warna_hijau(teks):
    return f"\033[92m{teks}\033[0m"

def main():
    bersihkan_layar()
    print("selamat datang di game tebak gelas medium level!")
    print("ada tiga gelas di depanmu, salah satunya ada bolanya.")
    print("gelas bernomor: 1, 2, dan 3.")
    
    bola = random.randint(1, 3)
    
    posisi_gelas = [1, 2, 3]
    random.shuffle(posisi_gelas)
    bola = posisi_gelas[0]
    
    acak_gelas()

    bersihkan_layar()
    
    print("Coba perhatikan gerakan gelas!")
    
    while True:
        try:
            tebakan = int(input("tebak gelas mana yang ada bolanya (1/2/3): "))
            
            if tebakan not in [1, 2, 3]:
                print("nomor tidak valid! pilih hanya 1, 2, atau 3.")
                continue
            break
        except ValueError:
            print("masukkan angka yang valid!")
    
    if tebakan == bola:
        print(warna_hijau(f"selamat! tebakanmu benar. bola ada di gelas nomor {bola}."))
    else:
        print(warna_merah(f"salah! bola ada di gelas nomor {bola}."))
        
    lagi = input("mau main lagi? (y/n): ").lower()
    if lagi == 'y':
        main()
    else:
        print("terima kasih sudah bermain!")

if __name__ == "__main__":
    main()
