import random
import time

def serang(pelaku, target, nama_pelaku):
    serangan = {
        'Pukulan': (5, 0.8),
        'Tendangan': (7, 0.6),
        'Laser': (10, 0.4),
        'Missile': (12, 0.3)
    }
    print(f"\n{nama_pelaku} memilih serangan:")
    for i, (nama, (dmg, chance)) in enumerate(serangan.items(), 1):
        print(f"{i}. {nama} (Damage: {dmg}, Akurasi: {int(chance*100)}%)")

    while True:
        try:
            pilihan = int(input("Pilih serangan (1-4): "))
            if 1 <= pilihan <= 4:
                break
            else:
                print("Masukkan angka antara 1 sampai 4!")
        except:
            print("Input tidak valid!")

    nama_serang = list(serangan.keys())[pilihan-1]
    dmg, chance = serangan[nama_serang]

    if random.random() <= chance:
        target['hp'] -= dmg
        print(f"Serangan {nama_serang} mengenai! Damage {dmg}.")
    else:
        print(f"Serangan {nama_serang} meleset!")

def musuh_serang(pelaku, target):
    serangan = {
        'Pukulan': (5, 0.8),
        'Tendangan': (7, 0.6),
        'Laser': (10, 0.4),
        'Missile': (12, 0.3)
    }
    nama_serang = random.choice(list(serangan.keys()))
    dmg, chance = serangan[nama_serang]
    print(f"\nMusuh memilih serangan {nama_serang}...")

    time.sleep(1)
    if random.random() <= chance:
        target['hp'] -= dmg
        print(f"Serangan {nama_serang} mengenai! Damage {dmg}.")
    else:
        print(f"Serangan {nama_serang} meleset!")

def main():
    print("🤖 Selamat datang di Battle Robot Duel!")
    player = {'hp': 50}
    enemy = {'hp': 50}

    while player['hp'] > 0 and enemy['hp'] > 0:
        print(f"\nHP Kamu: {player['hp']}  |  HP Musuh: {enemy['hp']}")

        serang(player, enemy, "Kamu")
        if enemy['hp'] <= 0:
            print("\n🎉 Kamu menang! Musuh hancur!")
            break

        musuh_serang(enemy, player)
        if player['hp'] <= 0:
            print("\n💀 Kamu kalah! Robotmu hancur!")
            break

    print("Game selesai!")

if __name__ == "__main__":
    main()