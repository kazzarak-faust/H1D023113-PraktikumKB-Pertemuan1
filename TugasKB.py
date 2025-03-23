import random
from datetime import datetime

siswa = [
    {"nama": "Ahmad", "nilai": random.randint(50, 100)},
    {"nama": "Budi", "nilai": random.randint(50, 100)},
    {"nama": "Citra", "nilai": random.randint(50, 100)},
]

print("=== Daftar Siswa dan Status Kelulusan ===")
for data in siswa:
    nama = data["nama"]
    nilai = data["nilai"]
    
    if nilai >= 80:
        status = "Lulus dengan Predikat A"
    elif nilai >= 70:
        status = "Lulus dengan Predikat B"
    elif nilai >= 60:
        status = "Lulus dengan Predikat C"
    else:
        status = "Tidak Lulus"
    
    print(f"Nama: {nama}, Nilai: {nilai}, Status: {status}")

waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("\nProgram dijalankan pada:", waktu_sekarang)
