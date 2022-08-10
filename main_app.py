import os
from module import *

# Database Mahasiswa IAT A
list_mahasiswa_kelas_a = []

while True:
    os.system("cls")
    print(list_mahasiswa_kelas_a)
    print(f"{'Selamat datang di':^52}")
    print(f"{'Database Mahasiswa IAT Kelas A':^52}")
    print("="*52)
    print("Silahkan pilih menu yang anda inginkan : ")
    print("="*52)
    print("1. Tampilkan data")
    print("2. Menambah data")
    print("3. Mengubah data")
    print("4. Menghapus data")
    print("0. EXIT")
    print("="*52)
    pilihan_user = input(">> ")
    if pilihan_user == "1":
        show_data(list_mahasiswa_kelas_a)
        input('')
    elif pilihan_user == "2":
        add_data(list_mahasiswa_kelas_a)
    elif pilihan_user == "3":
        show_data(list_mahasiswa_kelas_a)
        update_data(list_mahasiswa_kelas_a)
    elif pilihan_user == "4":
        show_data(list_mahasiswa_kelas_a)
        del_data(list_mahasiswa_kelas_a)
        # list_mahasiswa_kelas_a.update()
    elif pilihan_user == "0":
        print("Program Selesai!!")
        break
    else:
        print("Error Boss!!")
        break
