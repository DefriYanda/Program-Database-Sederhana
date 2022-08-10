
def update_data(list_mahasiswa):
    if (len(list_mahasiswa)) > 0:
        is_ubah = input("Apakah anda yakin ingin mengubah data? y/n")
        if is_ubah == "y":
            data_yg_akan_diupdate = int(
                input("Silahkan masukan nomor data yang ingin di ubah : "))
            data_lama = list_mahasiswa[data_yg_akan_diupdate-1]
            data_lama["nama"] = input("Masukan nama baru : ")
            data_lama["nim"] = int(input("Masukan NIM baru : "))
            data_lama["ig"] = input("Masukan Username IG baru : ")
            input("Data berhasil dirubah!!")
        elif is_ubah == "n":
            input("")
    else:
        input('')
