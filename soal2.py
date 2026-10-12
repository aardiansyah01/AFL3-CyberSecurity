import hashlib

target = "8d4c531eb4b0f54df72aa6839abbeaec"

for salt in "0123456789":
    for i in range(1_000_000):
        pin = f"{i:06d}"
        input_hash = salt + pin
        hasil_hash = hashlib.md5(
            input_hash.encode()
        ).hexdigest()

        if hasil_hash == target:
            print("PIN ditemukan:", pin)
            print("Salt ditemukan:", salt)
            raise SystemExit
