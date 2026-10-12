import hashlib

target = "b20f8b0405b88e2b0b50eb3356d34ba7"

def md5(teks):
    return hashlib.md5(teks.encode()).hexdigest()

for salt in "0123456789":
    for i in range(1_000_000):
        pin = f"{i:06d}"

        h0 = salt + pin
        h1 = md5(h0)
        h2 = md5(h1)
        h3 = md5(h2)

        if h3 == target:
            print("PIN ditemukan:", pin)
            print("Salt ditemukan:", salt)
            raise SystemExit
