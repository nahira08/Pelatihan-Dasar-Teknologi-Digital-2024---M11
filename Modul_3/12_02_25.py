ipk = float(input("Masukkan IPK mahasiswa: "))

if 2.00 <= ipk <= 2.75:
    predikat = "Memuaskan"
elif 2.76 <= ipk <= 3.50:
    predikat = "Sangat memuaskan"
elif 3.51 <= ipk <= 4.00:
    predikat = "Dengan pujian (Cumlaude)"
else:
    predikat = "IPK tidak valid"

print(f"Predikat: {predikat}")