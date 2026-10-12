import hashlib

target = "0110b96270248f746ecca06f1ce09746"

with open("pinlist.txt", "r", encoding="utf-8") as file:
    daftar_pin = file.readlines()

for kandidat in daftar_pin:
    pin = kandidat.strip()

    if not pin.isdigit() or len(pin) != 6:
        continue

    hasil_hash = hashlib.md5(pin.encode()).hexdigest()

    if hasil_hash == target:
        print("PIN ditemukan:", pin)
        break
else:
    print("PIN tidak ditemukan dalam file")
