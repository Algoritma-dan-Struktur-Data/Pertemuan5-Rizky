data = [
    [
        [10121001, "Asep"],
        [50, 70, 40, 80]
    ],
    [
        [10121002, "Budi"],
        [78, 78, 80, 65]
    ],
    [ 
        [10121003, "Cecep"],
        [57, 88, 67, 69]
    ]
]

rata_mhs = []

for mhs in data:
    nilai = mhs[1]
    rata = sum(nilai) / len(nilai)
    rata_mhs.append(rata)

nilai_tertinggi = max(rata_mhs)
index_pintar = rata_mhs.index(nilai_tertinggi)

jumlah_mhs = len(data)
jumlah_mk = len(data[0][1])
rata_mk = []

for i in range(jumlah_mk):
    total_nilai_mk = 0
    for j in range(jumlah_mhs):
        total_nilai_mk += data[j][1][i]
    
    rata_rata_mk = total_nilai_mk / jumlah_mhs
    rata_mk.append(rata_rata_mk)

nilai_mk_terendah = min(rata_mk)
index_mk_rendah = rata_mk.index(nilai_mk_terendah)

print("Mahasiswa Terpintar:", data[index_pintar][0][1], "(Nilai:", round(nilai_tertinggi, 2), ")")
print("Mata Kuliah Nilai Terkecil: MK", index_mk_rendah + 1, "(Nilai:", round(nilai_mk_terendah, 2), ")")
