
def input_angka():
    jumlah_angka = int(input("Masukkan jumlah angka yang akan diinput: "))
    angka_list = []

    for i in range(1, jumlah_angka + 1):
        angka = int(input(f"Angka {i}: "))
        angka_list.append(angka)

    return angka_list

def tampil_hasil(angka_list):
    if not angka_list:
        print("Belum ada angka yang diinput.")
    else:
        sorted_angka = sorted(angka_list)
        print("Hasil pengurutan:")
        print(", ".join(map(str, sorted_angka)))
        print(f"Nilai Tugas: {', '.join(map(str, angka_list))}")

def main():
    angka_list = []

    while True:
        print("\nMenu:")
        print("1. Input angka")
        print("2. Tampil hasil pengurutan")
        print("3. Selesai")

        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            angka_list.extend(input_angka())
        elif pilihan == '2':
            tampil_hasil(angka_list)
        elif pilihan == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")

if __name__ == "__main__":
    main()
