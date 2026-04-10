while True:
    print("\n1. Tambah\n2. Kurang\n3. Kali\n0. Keluar")
    pilih = int(input("Pilih: "))

    if pilih == 0:
        print("Program selesai.") 
        break

    r = int(input("Baris: "))
    c = int(input("Kolom: "))

    print("\nMatriks 1:")
    m1 = [[int(input(f"M1[{i}][{j}]: ")) for j in range(c)] for i in range(r)]

    print("\nMatriks 2:")
    m2 = [[int(input(f"M2[{i}][{j}]: ")) for j in range(c)] for i in range(r)]

    if pilih == 1:
        hasil = [[m1[i][j] + m2[i][j] for j in range(c)] for i in range(r)]
    elif pilih == 2:
        hasil = [[m1[i][j] - m2[i][j] for j in range(c)] for i in range(r)]
    elif pilih == 3:
        hasil = [[m1[i][j] * m2[i][j] for j in range(c)] for i in range(r)]

    print("\nHasil:")
    for baris in hasil:
        print(baris)
