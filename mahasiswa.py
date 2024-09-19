class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim


print('DATA')
print('Data Mahasiswa')
mahasiswa_2 = Mahasiswa('Udin', 9087654321)
mahasiswa_3 = Mahasiswa('Amanda', 1111111111)
print(f'{mahasiswa_2.nama} : {mahasiswa_2.nim}')
print(f'{mahasiswa_3.nama} : {mahasiswa_3.nim}')

print("Hayoloh Ini Beda Paragraph")