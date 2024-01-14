from mysql import connector
import os
from prettytable import PrettyTable

connect = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="glanes_cindy_terampe"
)

cursor=connect.cursor()

class induk :
    def __init__(self, id_kursus, Jenis_kursus, Biaya) :
        self.id_kursus = id_kursus
        self.jenis_kursus = Jenis_kursus
        self.biaya = Biaya

    def informasi(self) :
        cursor.execute("SELECT * FROM informasi_kursus;")
        result=cursor.fetchall()
        connect.commit()
        tabel= PrettyTable(['NO','NAMA KURSUS ', 'BIAYA'])
        tabel.add_rows(result)
        print(tabel)

    def inisialisasi(self) :
        ID_kursus = cursor.execute("SELECT id_kursus FROM informasi_kursus;")
        result1 =cursor.fetchall()
        jenis_kursus = cursor.execute("SELECT nama_kursus FROM informasi_kursus;")
        result2 = cursor.fetchall()
        biaya = cursor.execute("SELECT biaya FROM informasi_kursus;")
        result3 =cursor.fetchall()
        self.id_kursus = result1
        self.jenis_kursus = result2
        self.biaya = result3

class anak(induk) :
    def __init__(self, Nama, id_kursus, Jenis_kursus,Biaya, Status_bayar):
        super().__init__( id_kursus ,Jenis_kursus, Biaya)
        self.nama = Nama
        self.status_bayar = Status_bayar

    def menu1(self) :
        nama_peserta = input("Masukkan Nama Peserta: ")
        self.nama = nama_peserta
        id_kursus = int(input("Masukkan ID Kursus Yang Akan Diikuti: "))

        sql_query = "SELECT nama_kursus, biaya FROM informasi_kursus WHERE id_kursus = %s"
        cursor.execute(sql_query, (id_kursus,))
        result = cursor.fetchone()

        if result:
            self.jenis_kursus = result[0]
            self.biaya = result[1]
            self.id_kursus = id_kursus  

            self.status_bayar = 'Belum Lunas'

            inisialisasi_anak.input_data()
        else:
            print("ID Kursus tidak ditemukan.")

    def input_data(self) :
        sql= "INSERT INTO peserta_5220411219(nama,jenis_kursus,biaya,status_bayar) VALUES (%s, %s, %s, %s)"
        val=(self.nama ,self.jenis_kursus ,self.biaya ,self.status_bayar)
        cursor.execute(sql,val)
        connect.commit()
        print("Data berhasil disimpan")

    def Informasi(self) :
        cursor=connect.cursor()
        cursor.execute("SELECT * FROM peserta_5220411219;")
        result=cursor.fetchall()
        connect.commit()
        tabel= PrettyTable(['NO','NAMA ','JENIS KURSUS', 'PEMBAYARAN', 'STATUS PEMBAYARAN'])
        tabel.add_rows(result)
        print(tabel)

    def menu4(self) :
        cursor.execute('SELECT * FROM peserta_5220411219 ')
        hasil = cursor.fetchall()
        data= int(input('Masukkan No Pendaftaran :'))
        for i in hasil :
            if data==i[0] :
                bayar=int(input('Masukkan Nominal Pembayaran Anda :'))
                harga= i[3]
                execute= (bayar - harga)
                print('tagihan anda :',harga)
                print('pembayaran anda :',bayar)
                print('kembalian :',execute)
                keyword= 'lunas'
                sql="UPDATE peserta_5220411219 SET status_bayar = %s WHERE no  = %s"
                val=(keyword, data)
                cursor.execute(sql,val)
                cursor.fetchall()
                connect.commit()

    def menu5(self) :
        cursor= connect.cursor()
        keyword=input("Masukkan Jenis Kursus atau Nama peserta :")
        sql="SELECT * FROM peserta_5220411219 WHERE nama LIKE %s OR jenis_kursus LIKE %s;"
        val=("%{}%".format(keyword), "%{}%".format(keyword))
        cursor.execute(sql,val)
        results=cursor.fetchall()
        if cursor.rowcount<0:
            print("Tidak ada data")
        else:
            tabel= PrettyTable(['No Pendaftaran','Nama Peserta','Jenis Kursus','Pembayaran','Status Bayar'])
            tabel.add_rows(results)
            print(tabel)

    def menu6(self) :
        cursor= connect.cursor()
        keyword=int(input("masukkan no pendaftar :"))
        sql="DELETE FROM peserta_5220411219 WHERE no = %s;"
        cursor.execute(sql,(keyword,))
        results = cursor.fetchall()
        connect.commit()
        print('data telah di hapus')
    

inisialisasi = induk(7,"Data Scientist", 2000000)
inisialisasi_anak = anak("vvv", 7, "Data Scientist" , 2000000, "Belum Lunas")

os.system("cls")

while True :
    print('='*40)
    print(f"+ {'1. Informasi Kursus':<36} +")
    print(f"+ {'2. Pendaftaran':<36} +")
    print(f"+ {'3. Data Peserta':<36} +")
    print(f"+ {'4. Pembayaran':<36} +")
    print(f"+ {'5. Cari Peserta':<36} +")
    print(f"+ {'6. Batalkan Keikutsertaan':<36} +")
    print(f"+ {'0. Keluar':<36} +")
    print('='*40)
    pilih0=int(input('Masukkan Pilihan Menu :'))
    if pilih0 == 1 :
        inisialisasi.informasi()
     
    elif pilih0== 2 :
        inisialisasi_anak.menu1() 
        os.system("Pause")
        os.system("cls")
        
    elif pilih0 == 3 :
        print('='*40)
        inisialisasi_anak.Informasi()
        os.system("Pause")
        os.system("cls")

    elif pilih0== 4 :
        print('='*40)
        inisialisasi_anak.menu4()
        os.system("Pause")
        os.system("cls")

    elif pilih0 == 5 :
        print('='*40)
        inisialisasi_anak.menu5()
        os.system("Pause")
        os.system("cls")

    elif pilih0 == 6 :
        print('='*40)
        inisialisasi_anak.menu6()
        os.system("Pause")
        os.system("cls")

    elif pilih0==0 :
        break


    
print('Terimakasih Sudah Menggunakan Aplikasi Ini  <3 ')
print('\n-------------------------------------------')
    

