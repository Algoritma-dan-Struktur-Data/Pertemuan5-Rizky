# array 2 dimensi

while True:
    print("\n")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 0:
        print("Program selesai.")
        break

    baris = int(input("\nInput jumlah baris: "))
    kolom = int(input("Input jumlah kolom: "))

    print("\nInput Matriks A")
    A = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            nilai = int(input(f"A[{i}][{j}] = "))
            row.append(nilai)
        A.append(row)

    print("\nInput Matriks B")
    B = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            nilai = int(input(f"B[{i}][{j}] = "))
            row.append(nilai)
        B.append(row)

    hasil = []

    # proses sesuai pilihan
    for i in range(baris):
        row = []
        for j in range(kolom):
            if pilihan == 1:
                row.append(A[i][j] + B[i][j])
            elif pilihan == 2:
                row.append(A[i][j] - B[i][j])
            elif pilihan == 3:
                row.append(A[i][j] * B[i][j])
        hasil.append(row)

    # output hasils
    print("\nHasil:")
    for row in hasil:
        print(row)