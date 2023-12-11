class Program:
    def __init__(self):
        self.angka_list = []

    def input_angka(self):
        jumlah_angka = int(input("Masukkan jumlah angka yang akan diinput: "))
        for i in range(1, jumlah_angka + 1):
            angka = int(input(f"Angka {i}: "))
            self.angka_list.append(angka)

    def tampil_hasil(self):
        if not self.angka_list:
            print("Belum ada angka yang diinput.")
        else:
            sorted_angka = sorted(self.angka_list)
            print("Hasil pengurutan:")
            print(", ".join(map(str, sorted_angka)))
            print(f"Nilai Tugas: {', '.join(map(str, self.angka_list))}")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Input angka")
            print("2. Tampil hasil pengurutan")
            print("3. Selesai")

            pilihan = input("Masukkan pilihan (1/2/3): ")

            if pilihan == '1':
                self.input_angka()
            elif pilihan == '2':
                self.tampil_hasil()
            elif pilihan == '3':
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")


if __name__ == "__main__":
    program = Program()
    program.run()
