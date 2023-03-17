# Nama : Muslim Nur Wahid
# NIM : 22091116070
# Kelas : Sistem Informasi B

from prettytable import PrettyTable
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
                
class LinkedList:
    def __init__(self):
        self.head = None
    
    def tambahwarga(self, value):
        if self.head is None:
            self.head = Node(value)
        else: 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def hapuswarga(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print()
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next
    def urutan(self, index):
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node

            current_node = current_node.next
            current_index += 1
            
    def tampildatawarga(self):
        if self.head is None:
            print("Tidak ada data warga")
        else :
            tabelwarga = PrettyTable()
            tabelwarga.field_names = ["No. Rumah", "Nama Lengkap Warga"]
            n = self.head
            a = 1
            while n is not None:
                tabelwarga.add_row([a, n.data])
                a += 1
                n = n.next
                print(tabelwarga)
    
class linkedlist_menambahdatawarga:
    def __init__(self):
        self.head = None
    
    def tambahwarga1(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def tampildatawarga1(self):
        if self.head is None:
            print("Tidak ada data warga")
        else :
            tabelwarga1 = PrettyTable()
            tabelwarga1.field_names =  ["No. Rumah", "Nama Lengkap Warga"]
            n = self.head
            b = 1
            while n is not None:
                tabelwarga1.add_row([b, n.data])
                b += 1
                n = n.next
            print(tabelwarga1)
            
class linkedlist_menghapusdatawarga:
    def __init__(self):
        self.head = None
    
    def tambahwarga2(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def tampildatawarga2(self):
        if self.head is None:
            print("Tidak ada data warga")
        else :
            tabelwarga2 = PrettyTable()
            tabelwarga2.field_names = ["No. Rumah", "Nama Lengkap Warga"]
            n = self.head
            c = 1
            while n is not None:
                tabelwarga2.add_row([c, n.data])
                c += 1
                n = n.next
                print(tabelwarga2)
                
datawarga = LinkedList()
tambahdatawarga = linkedlist_menambahdatawarga()
hapusdatawarga = linkedlist_menghapusdatawarga()

def menambahdatawarga():
    inputA = input("Masukkan nama lengkap warga baru : ")
    datawarga.tambahwarga(inputA)
    tambahdatawarga.tambahwarga1(inputA)
def menghapusdatawarga():
    hapus = int(input("Masukkan nomor rumah warga yang ingin dihapus : "))
    b = datawarga.urutan(hapus-1)
    hapusdatawarga.tambahwarga2(b.data)
    datawarga.hapuswarga(hapus-1)
  
while True:
    print("MENU WARGA PERUMAHAN CITRALAND")
    print()
    print("1. Tambah Data Warga Baru\n2. Hapus Data Warga\n3. Lihat Seluruh Data Warga\n4. History Data Warga\n5. Exit")
    pilih = input("Pilih nomor yang ingin kamu lakukan : ")
    if pilih == "1":    
        menambahdatawarga()
    elif pilih == "2":
        datawarga.tampildatawarga()
        menghapusdatawarga()
    elif pilih == "3":    
        datawarga.tampildatawarga()
    elif pilih == "4" :
        while True:
            print("Menu History")
            print()
            print("1. Warga yang ada di Perumahan Citraland\n2. Warga yang pindah dari Perumahan Citraland\n3. Kembali ke menu awal")
            pilih1 = input("Masukkan nomor yang ingin dilakukan : ")
            if pilih1 == "1":
                print("List data warga yang ada di Perumahan Citraland")
                tambahdatawarga.tampildatawarga1()
            elif pilih1 == "2":
                print("List data warga yang pindah")
                hapusdatawarga.tampildatawarga2()
            elif pilih1 == "3":
                break
            else:
                print('Input Salah')
    elif pilih == "5":
        print("Kamu telah keluar dari program")
        print("Terimakasih!!!")
        exit()
    else :
        print("masukan inputan dengan benar")