while True:
    print("\n")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    opsi = int(input("Pilih menu: "))

    if opsi == 0:
        print("Program selesai.")
        break

    r = int(input("\nInput jumlah baris: "))
    c = int(input("Input jumlah kolom: "))

    print("\nInput Matriks Pertama")
    mat_1 = []
    for i in range(r):
        baris_data = []
        for j in range(c):
            angka = int(input(f"Matriks1[{i}][{j}] = "))
            baris_data.append(angka)
        mat_1.append(baris_data)

    print("\nInput Matriks Kedua")
    mat_2 = []
    for i in range(r):
        baris_data = []
        for j in range(c):
            angka = int(input(f"Matriks2[{i}][{j}] = "))
            baris_data.append(angka)
        mat_2.append(baris_data)

    output = []

    for i in range(r):
        baris_hasil = []
        for j in range(c):
            if opsi == 1:
                baris_hasil.append(mat_1[i][j] + mat_2[i][j])
            elif opsi == 2:
                baris_hasil.append(mat_1[i][j] - mat_2[i][j])
            elif opsi == 3:
                baris_hasil.append(mat_1[i][j] * mat_2[i][j])
        output.append(baris_hasil)

    print("\nHasil Akhir:")
    for baris_hasil in output:
        print(baris_hasil)
