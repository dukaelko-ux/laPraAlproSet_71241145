import re

def baca_kata(nama_file):
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            isi = f.read().lower()
            return set(re.findall(r'\b[a-z]+\b', isi))
    except FileNotFoundError:
        print(f'Error: File "{nama_file}" tidak ditemukan!')
        return None

file1 = input('Nama file pertama: ')
file2 = input('Nama file kedua  : ')
set1 = baca_kata(file1)
set2 = baca_kata(file2)

if set1 is not None and set2 is not None:
    bersama = set1 & set2
    print(f'Kata di kedua file ({len(bersama)} kata):')
    for kata in sorted(bersama):
        print(f'  - {kata}')
