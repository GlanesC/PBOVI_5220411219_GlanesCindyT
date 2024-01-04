import os

class SeniBudaya:
    def __init__(self, nama):
        self._nama = nama

    def display_info(self):
        return f"Seni atau Budaya: {self._nama}"


class SeniVisual(SeniBudaya):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self._jenis = jenis

    def display_info(self):
        print("Nama Seni Visual  :", self._nama)
        print("jenis Seni Visual :", self._jenis)


class beliKarya(SeniVisual):
    def __init__(self, nama, hargaa, jenis):
        super().__init__(nama, jenis)
        self.hargaa = hargaa

    def jenis(self) :
        return self._jenis
    
    def harga(self) :
        return self.hargaa
    
    def beli(self) :
        print("Nama Karya Seni :", self._nama)
        print("Jenis Karya Seni:", self._nama)
        print("harga           :", self.hargaa)


class SeniPertunjukan(SeniBudaya):
    def __init__(self, nama, jenis, asal):
        super().__init__(nama)
        self._jenis = jenis
        self._asal = asal
    
    def display_info(self):
        print("Jenis Pertunjukkan :", self._nama)
        print("Nama               :", self._jenis)
        print("Asal               :", self._asal)


def main_menu():
    print(15*"=","Menu Utama:","="*15)
    print("1. Informasi Seni Visual")
    print("2. Beli Karya Seni Visual")
    print("3. Informasi Seni Pertunjukan")
    print("0. Keluar")
    print("-"*43)


def main():
    while True:
        main_menu()
        pilihan = input("Pilih Menu (0-3): ")
        print("-"*43)
        os.system("cls")
        if pilihan == "1":
            print("-"*43)
            if seni_visual:
                print(seni_visual.display_info())
            else:
                print("Belum ada informasi Seni Visual.")
                
        elif pilihan == "2":
            print("-"*43)
            if beliKaryaa:
                jenis = input("Masukkan jenis karya seni visual: ")
                if jenis == beliKaryaa.jenis() :
                    harga = beliKaryaa.harga()
                    banyak = int(input("banyak Pembelian :"))
                    total = harga * banyak
                    print("total Belanja :", total)
            else:
                print("Buat Seni Visual terlebih dahulu sebelum membuat karya seni.")

        
        elif pilihan == "3":
            print("-"*43)
            if seni_pertunjukan:
                print(seni_pertunjukan.display_info())
            else:
                print("Belum ada informasi Seni Pertunjukan.")
        elif pilihan == "0":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")



seni_visual = SeniVisual("Lukisan", "Muralisme")
beliKaryaa = beliKarya("Lukisan", 200000000, "Muralisme")
seni_pertunjukan = SeniPertunjukan("Tari Legong", "Tari Tradisional", "Bali")

main()