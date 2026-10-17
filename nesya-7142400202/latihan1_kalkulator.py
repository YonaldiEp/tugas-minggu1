# =====================================
# Latihan 1 - Kalkulator Konsol Sederhana
# Pelatihan Dasar Pemrograman MORRIS IF 26
# =====================================

print("===================================")
print(" KALKULATOR SEDERHANA")
print("===================================")
print("Operasi yang tersedia: + - * /")
print(" -----------------------------------")

angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

print(" -----------------------------------")

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil:.2f}")  

elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil:.2f}")
    
elif operator == "/":
    if angka2 == 0:
        print("Kesalahan: bilangan tidak dapat dibagi dengan nol.")
    # elif angka1 == 0:
    #     print("Kesalahan: 0 dibagi dengan bilangan apapun adalah 0.")
    else:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil:.2f}")

else:
    print(f"Operator '{operator}' tidak dikenali.")
    print("Gunakan salah satu dari: +, -, *, /")

print("====================================")
print("Terima kasih telah menggunakan kalkulator ini!")