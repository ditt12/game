import random
import time
import os
from datetime import datetime

def baca_tanggal_expired():
    try:
        with open("expired.txt", "r") as file:
            tanggal = file.read().strip()
            return datetime.strptime(tanggal, "%Y-%m-%d")
    except FileNotFoundError:
        print("\033[91mFile expired.txt tidak ditemukan! Pastikan file tersebut ada.\033[0m")
        exit()
    except ValueError:
        print("\033[91mFormat tanggal di expired.txt salah! Gunakan format YYYY-MM-DD.\033[0m")
        exit()

def cek_expired():
    expired_date = baca_tanggal_expired()
    current_date = datetime.now()

    if current_date > expired_date:
        print("\033[91mMaaf, game ini sudah expired pada", expired_date.strftime("%d %B %Y"), ".\033[0m")
        exit()

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
    cek_expired()  # cek tanggal expired sebelum mulai
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