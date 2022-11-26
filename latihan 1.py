print("========== LATIHAN 1 - DICTIONARY ==========")
print()
r = {'Ari' : '081267888', 'Dina' : '087677776'}
print("# Daftar Kontak :\n", r)
print()

#Menampilkan Kontak
print("# Menampilkan kontak Ari : 081267888")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

#Menambahkan kontak baru
print("# Menambahkan kontak baru\n", r)
print("Daftar kontak sebelumnya :\n", r)
r['Riko']= '087654544';
print("Daftar kontak setelah ditambahkan :\n", r)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

#Mengubah kontak Dina
print("# Mengubah Kontak Dina\n")
print("Daftar Kontak Dina Sebelumnya :\n", r)
r['Dina'] = '088999776'
print("Daftar Kontak Dina Setelah Diubah :\n", r)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

#Menampilkan semua nama
print("# Menampilkan Semua Nama Kontak :\n")
print(r.keys())
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

#Menampilkan semua nomor
print("# Menampilkan Semua Nomor :\n")
print(r.values())
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

#Menampilkan Keseluruhan
print("# Daftar Kontak Keseluruhan :\n")
print(r.items())
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

#Menghapus Kontak Dina
print("# Menghapus Kontak Dina\n")
print("Daftar Kontak Sebelumnya :\n", r)
del r['Dina'];
print("Daftar Kontak Setelah Dihapus :\n", r)