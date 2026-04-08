# array 3 dimensi
# mencari mahasiswa yang terpintar berdasarkan rata-rata nilai
# matkul apa yg rata-ratanya paling kecil

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

rata2 = []

for i in range(len(data)):
    nilai = data[i][1]
    avg = sum(nilai) / len(nilai)
    rata2.append(avg)

nilai_maksimal = max(rata2)
index_maksimal = rata2.index(nilai_maksimal)

jumlah_mk = len(data[0][1])
rata_mk = []

for j in range(jumlah_mk):
    total = 0
    for i in range(len(data)):
        total += data[i][1][j]
    avg = total / len(data)
    rata_mk.append(avg)

nilai_minimal = min(rata_mk)
index_minimal = rata_mk.index(nilai_minimal)

print("Mahasiswa Terpintar :", data[index_maksimal][0][1], "(Nilai:", round(nilai_maksimal, 2), ")")
print("Mata Kuliah Nilai Terkecil : MK", index_minimal + 1, "(Nilai:", round(nilai_minimal, 2), ")")