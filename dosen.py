class Dosen:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip


print("Data Dosen")
dosen_1 = Dosen('Patricia', 12345)
dosen_2 = Dosen('Agatha', 54321)
print(f'{dosen_1.nama} : {dosen_1.nip}')
print(f'{dosen_2.nama} : {dosen_2.nip}')