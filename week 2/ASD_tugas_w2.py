#=======================================# 
# tugas praktikum w2: tipe data koleksi # 
# main: membuat fungsi load data      # 
#=======================================# 

nama_file = "stok_barang.txt"
#membuat fungsi untuk membaca data
def r_stok_barang(nama_file):
    data_dict= {}

    with open("stok_barang.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #hilangkan karakter baris baru (\n)

            parts = baris.split(",")
            if len(parts) !=3:
                continue
            kode, nama_brg, stok = parts
            stok_int = int(stok)
            data_dict[kode] = {"nama barang": nama_brg, "jumlah stok": stok_int}
            kode, nama_brg, stok = baris.split(", ")

            data_dict[kode] = {
                "nama barang": nama_brg,
                "jumlah stok": int(stok)
            }
    return data_dict

buka_data = r_stok_barang(nama_file)
print("jumlah data terbaca: ", len(buka_data))

#=========================================# 
# tugas praktikum w2: tipe data koleksi   # 
# menu 1: membuat fungsi menampilkan data # 
#=========================================# 

def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("data kosong")
        return
    print("=== daftar stok barang ===")
    print(f"{'kode': <8} | {'nama barang': <12} | {'jumlah stok': >5}")
    print("-" * 32)

    for kode in sorted(data_dict.keys()):
        nama_brg = data_dict[kode]["nama barang"]
        stok = data_dict[kode]["jumlah stok"]
        print(f"{kode: <8} | {nama_brg: <12} | {stok: >5}")

tampilkan_data(buka_data)

#=======================================# 
# tugas praktikum w2: tipe data koleksi # 
# menu 2: membuat fungsi mencari data   # 
#=======================================# 

def cari_data(data_dict):
    kode_cari = input("masukkan kode barang yang ingin dicari: ").strip()

    if kode_cari in data_dict:
        nama_brg = data_dict[kode_cari]["nama barang"]
        stok = data_dict[kode_cari]["jumlah stok"]
        print("data barang ditemukan")
        print(f"kode: {kode_cari}")
        print(f"nama barang: {nama_brg}")
        print(f"jumlah stok: {stok}")
    else:
        print("data barang tidak ditemukan")

cari_data(buka_data)

#=======================================# 
# tugas praktikum w2: tipe data koleksi # 
# menu 3: membuat fungsi update data    # 
#=======================================# 

def update_data(data_dict):
    kode = input("masukkan kode barang yang ingin di update: ")

    if kode not in data_dict:
        print("kode tidak ditemukan, update dibatalkan")
        return
    try:
        jumlah_stok_baru = int(input("masukkan jumlah stok barang baru: ").strip())
    except ValueError:
        print("stok harus berupa angka")
        return
    print("jumlah stok barang: ", jumlah_stok_baru)
    jumlah_stok_lama = data_dict[kode]["jumlah stok"]
    data_dict[kode]["jumlah stok"] = jumlah_stok_baru
    print(f"update berhasil, \nstok barang lama: {jumlah_stok_lama} \nstok barang baru: {jumlah_stok_baru}")

update_data(buka_data)

#=======================================# 
# tugas praktikum w2: tipe data koleksi # 
# menu 3: membuat fungsi update data    # 
#=======================================# 

