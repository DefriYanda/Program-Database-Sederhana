def del_data(list_mahasiswa):
    if (len(list_mahasiswa)) > 0:
        is_hapus = input("Apakah anda yakin ingin mengubah data? y/n")
        if is_hapus == "y":
            data_yg_akan_dihapus = int(
                input("Silahkan masukan nomor data yang ingin di hapus : "))
            for i in range(len(list_mahasiswa)):
                if i == data_yg_akan_dihapus-1:
                    del list_mahasiswa[i]
                    break
            input("Data berhasil dihapus!!")
        elif is_hapus == "n":
            input("")
    else:
        input('')
