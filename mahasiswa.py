class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim


print('COBA GIT')
print('Data Mahasiswa')
mahasiswa_1 = Mahasiswa('Ucok', 1234567890)
mahasiswa_2 = Mahasiswa('Udin', 9087654321)
print(f'{mahasiswa_1.nama} : {mahasiswa_1.nim}')
print(f'{mahasiswa_2.nama} : {mahasiswa_2.nim}')