import hashlib

target = "0110b96270248f746ecca06f1ce09746"

for i in range(1_000_000):
    pin = f"{i:06d}"
    hasil_hash = hashlib.md5(pin.encode()).hexdigest()

    if hasil_hash == target:
        print("PIN ditemukan:", pin)
        break
