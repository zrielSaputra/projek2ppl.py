from pickle import OBJ


class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def tambah(self):
        return self.a + self.b
    def kurang(self):
        return self.a - self.b
a = int(input('silahkan masukan angka pertama : '))
b = int(input('silahkan masukan angka kedua : '))
obj=cal(a,b)
while True:
    def menu():
        x = ('1. tambah \n2. kurang')
        print(x)
    menu()
    pilihan = int (input('silahkan masukan angka pertama'))
    if pilihan == 1:
        print("hasilnya :, obj.tambah"())
        break
    elif pilihan == 2:
        print("hasilnya :, obj.kurang"())
        break