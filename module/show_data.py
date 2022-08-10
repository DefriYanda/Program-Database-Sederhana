import os


def show_data(list_kelas):
    i = 0
    os.system("cls")
    if len(list_kelas) <= 0:
        print("="*52)
        print(f"{'Belum ada data yang di masukkan':^52}")
        print(f"{'Silahkan masukan data terlebih dahulu!!':^52}")
        print("="*52)
    else:
        print(f"{'Data Mahasiswa Kelas A':^52}")
        print("="*52)
        print(f"{'No':^3}|{'Nama':^19}|{'NIM':^13}|{'Instagram':^13}")
        print("="*52)
        for data in list_kelas:
            i += 1
            print(
                f"{i:^1}.  {data['nama']:<19}  {data['nim']:<11}   {data['ig']:<13}")
        print("="*52)
