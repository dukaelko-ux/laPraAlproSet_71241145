n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}
for i in range(n):
    nama_kategori = input('Nama kategori: ')
    aplikasi = set()
    for j in range(5):
        aplikasi.add(input('Nama aplikasi: '))
    data_aplikasi[nama_kategori] = aplikasi

daftar_set = list(data_aplikasi.values())
semua = set().union(*daftar_set)
semua_irisan_pasangan = set()
for i in range(len(daftar_set)):
    for j in range(i+1, len(daftar_set)):
        semua_irisan_pasangan |= daftar_set[i] & daftar_set[j]

print('Hanya di satu kategori:', semua - semua_irisan_pasangan)

if n > 2:
    tepat_dua = set()
    for i in range(len(daftar_set)):
        for j in range(i+1, len(daftar_set)):
            irisan = daftar_set[i] & daftar_set[j]
            for k in range(len(daftar_set)):
                if k != i and k != j:
                    irisan -= daftar_set[k]
            tepat_dua |= irisan
    print('Tepat di dua kategori:', tepat_dua)
