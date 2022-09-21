# SELAMAT DATANG DI JPHOTEL
from tkinter.filedialog import askopenfile


print("--selamat datang di jphotel--")
print("--no-----tipe-----harga--")
print("--01-----suite-----1.000.000--")
print("--02-----royal-----500.000--")
print("--03-----bpjs-----250.000--")

# sampe resepsionis (input data)
cust = input("masukan  nama lengkap : ")
tipe = int(input("tipe kamar : "))
lama_inap = int(input("masukan lama inap : "))

# struk jphotel
print("pelanggal atas nama : ", cust)
# tipe kamar
if tipe == 1:
    print ("tipe kamar yang di pilih suite")
elif tipe == 2:
    print ("tipe kamar yang di pilih suite royal")
elif tipe == 3:
    print ("tipe kamar yang di pilih suite bpjs")
print("lama menginap : ", lama_inap)
print("tipe kamar yang di pilih :", tipe)