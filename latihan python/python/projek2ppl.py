#fungsi garis guys
def garis1():
    print("===================")

def garis2():
    print("-------------------")


# Perpus kosong untuk menyimpan buku
from os import remove


buku = []

#fungsi show buku ( perlihatkan buku )
def show_buku():
    if len(buku) <= 0:
        garis1()
        print ("Buku Kosong mas!")
        garis1()
    else:
        for indeks in range(len(buku)):
            garis1()
            print ("[{}] {}".format (indeks,buku [indeks]))
            garis1()

# fungsi untuk edit buku
def edit_buku():
    show_buku()
    indeks = int(input("inputkan ID buku : "))
    if indeks > len (buku):
        print("ID SALAH")
        garis2()
    else:
        judul_baru = input("judul baru : ")
        buku[indeks] = judul_baru
        garis2()
        print("buku berhasi di rubah!")
        show_buku()
        garis1()

#fungsi insert buku
def insert_buku():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)

#fungsi delet buku
def delet_buku():
    show_buku()
    indeks = int(input("inputkan ID buku : "))
    if indeks > len (buku):
        print ("ID SALAH")
    else:
        buku.remove(buku [indeks])
        garis1()
        print ("buku berhasil dihapus!")
        garis2()

# Menu untuk tampilan perpus
def show_menu():
    print("\n")
    print("-Selamat datang di Perpus-")
    print("1. Show buku")
    print("2. Insert buku")
    print("3. Edit buku")
    print("4. Delete buku")
    print("5. Keluar")

    menu = int(input("Pilih Menu : > "))


    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print ("Upss Salaahh")

# tampilkan Menu
if __name__ == "__main__":
    while True:
        show_menu()