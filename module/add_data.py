import os


def add_data(list_kelas):
    os.system('cls')
    print("="*52)
    print(f"{'Silahkan Input Data Anda':^52}")
    print("="*52)
    nama = input("Masukan nama anda : ")
    nim = int(input("Masukan NIM anda : "))
    ig = input("Masukan Username ig anda : ")
    bio_mahasiswa = {
        "nama": nama,
        "nim": nim,
        "ig": ig
    }
    list_kelas.append(bio_mahasiswa)
    input("Data telah ditambahkan!! ")
