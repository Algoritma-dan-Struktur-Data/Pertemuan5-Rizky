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

rata_mhs = [sum(mhs[1]) / len(mhs[1]) for mhs in data]
max_avg = max(rata_mhs)
idx_max = rata_mhs.index(max_avg)

rata_mk = []
nilai_saja = [mhs[1] for mhs in data]

for nilai_per_mk in zip(*nilai_saja):
    avg_mk = sum(nilai_per_mk) / len(nilai_per_mk)
    rata_mk.append(avg_mk)

min_avg_mk = min(rata_mk)
idx_min_mk = rata_mk.index(min_avg_mk)

print(f"Mahasiswa Terpintar: {data[idx_max][0][1]} (Rata-rata: {round(max_avg, 2)})")
print(f"Mata Kuliah Nilai Terkecil: MK {idx_min_mk + 1} (Rata-rata: {round(min_avg_mk, 2)})")
