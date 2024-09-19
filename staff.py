class Staff:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip


print('DATA STAFF')
print('Data Staff')
staff_1 = Staff('Agus', 4567890)
staff_2 = Staff('Samsul', 3654321)
print(f'{staff_1.nama} : {staff_1.nip}')
print(f'{staff_2.nama} : {staff_2.nip}')