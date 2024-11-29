dataKeseluruhan = []

dataPasienBPJS = []

dataPasienReguler = []

dataPasienUGD = []

dataArsipUGD = []

dataArsipBPJS = []

dataArsipReguler = []

dataArsipPasien = []

def tampilan_menu():
    print("\n Selamat Datang di Adminitrasi Rumah Sakit\n 1. Informasi Pendaftaran\n 2. Pasien BPJS\n 3. Pasien Reguler\n 4. Pasien Gawat Darurat \n 5. Arsipkan Data Pasien\n 6. Daftar Pasien Terkini\n 7. Log Out\n 8. Matikan Perangkat")

def information():
    print("Ketentuan Pendaftaran Pasien Rs. Bung Karno")
    print("\n 1. Pendaftaran  berlaku bagi pasien yang telah memiliki Nomor Rekam Medis atau sudah pernah daftar sebelumnya di Rs. Bung Karno\n 2. Pendaftaran berlaku untuk pasien BPJS dan Reguler\n 3. Pendaftaran dapat dilakukan H-7 dari jadwal kontrol, dengan memasukkan :\n Pasien Reguler\n  1. No. KTP dan Tanggal Lahir\n Pasien JKN\n  1. No. BPJS, Tanggal Lahir & Asal Rujukan\n 4. Pasien Gawat Darurat harus menunggu hasil dari Tim Medis")

    kembali = input("Kembali ? ")
    kembali == "ya"

def hitung_nomor_urut_BPJS(poliklinik, hari_berobat):
    nomor_urut = 1 
    for pasien in dataPasienBPJS:
        if pasien["Poliklinik"] == poliklinik and pasien["Hari Berobat"] == hari_berobat:
            nomor_urut += 1
    return nomor_urut

def hitung_nomor_urut_Reguler(poliklinik, hari_berobat):
    nomor_urut = 1 
    for pasien in dataPasienReguler:
        if pasien["Poliklinik"] == poliklinik and pasien["Hari Berobat"] == hari_berobat:
            nomor_urut += 1
    return nomor_urut

def pasien_bpjs():
    print("\n============= PASIEN BPJS =============")
    while True:
        nomer_bpjs = input("Nomer BPJS (11 digit) : ")
        if len(nomer_bpjs) == 11 and nomer_bpjs.isdigit():
            break
        print("Nomer invalid. Maksimal digit adalah 11 angka")
    print("=======================================")
    nama = input("Masukkan Nama : ")
    print("=======================================")
    while True:
        tanggal_lahir = input("Tanggal Lahir (DD-MM-YYYY) : ")
        if len(tanggal_lahir) == 8 and tanggal_lahir.isdigit():
            break
        print("Nomer invalid harus berisi 8 angka")
    print("=======================================")
    while True:
        print("Pilihan Gender\n 1. Laki - laki\n 2. Perempuan")
        gender = input("Pilih opsi (1 / 2) : ")
        if gender == "1":
            gender = "Laki - laki"
            break
        elif gender == "2":
            gender = "Perempuan"
            break
        else:
            print("Pilih sesuai opsi!")
    print("=========================================")
    while True:
        asal_rujukan = input("Asal Rujukan (Faskes 1 / 2) : ")
        
        if asal_rujukan == "1":        
            asal_rujukan = "Faskes 1"
            break
        elif asal_rujukan == "2":
            asal_rujukan = "Faskes 2"
            break
        else:
            print("Pilih opsi yang ada!")
    print("=========================================")
    while True:
        asal_kota = input("Masukkan asal Kota : ")
        if asal_kota.isalpha():
            break
        print("Masukkan Kota yang benar!")

    poliklinik, type = pilih_poli()
    hari_berobat = tanggal_berobat()
    nomor_urut = hitung_nomor_urut_BPJS(poliklinik, hari_berobat)
    list_hasil_pasien_BPJS(nomer_bpjs, nama, tanggal_lahir, gender, asal_rujukan, asal_kota, poliklinik, hari_berobat, type, nomor_urut)

    dataPasien = {
        "No. BPJS": nomer_bpjs,
        "Nama Pasien": nama,
        "Tanggal Lahir": tanggal_lahir,
        "Gender": gender,
        "Alamat Pasien": asal_kota,
        "Rujukan": asal_rujukan,
        "Poliklinik": poliklinik,
        "Hari Berobat": hari_berobat,
        "Nomor Urut": nomor_urut,
        "Type": type
    }

    while True:
        cek_valid = input("Apakah data sudah benar (ya/tidak) ? ").lower()
        print("========================================")
        if cek_valid == "ya":
            dataKeseluruhan.append(dataPasien)
            dataPasienBPJS.append(dataPasien)
            print("Data pasien berhasil terdaftar...")
            print("========================================")
            break
        elif cek_valid == "tidak":
            print("Pembatalan berhasil...")
            print("========================================")
            break
        else:
            print("Input tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")

    return nomer_bpjs, nama, tanggal_lahir, gender, asal_rujukan, asal_kota, poliklinik, hari_berobat, type

def list_hasil_pasien_BPJS(nomer_bpjs, nama, tanggal_lahir, gender, asal_rujukan, asal_kota, poliklinik, hari_berobat, type, nomor_urut):
    print("\n============= DATA PASIEN =============")
    print(f"No. Urut          : {type}-{nomor_urut}")
    print(f"No. BPJS          : {nomer_bpjs}")
    print(f"Nama Pasien       : {nama}")
    print(f"Tanggal Lahir     : {tanggal_lahir}")
    print(f"Jenis Kelamin     : {gender}")
    print(f"Alamat Pasien     : {asal_kota}")
    print(f"Asal Rujukan      : {asal_rujukan}")
    print(f"Poliklinik        : {poliklinik}")
    print(f"Hari Berobat      : {hari_berobat}")
    print("========================================")
    
def pilih_poli():
    print("\n============= PILIH POLIKLINIK =============")
    print(" 1. Poliklinik Penyakit Dalam\n 2. Poliklinik Anak\n 3. Poliklinik Kulit dan Kelamin\n 4. Poliklinik Mata\n 5. Poliklinik Gigi dan Mulut\n 6. Poliklinik Orthopedi dan Traumatologi")
   
    while True:
        print("==================================")
        poliklinik = input("Silahkan pilih poliklinik : ")
        if poliklinik.isdigit():
            poliklinik = int(poliklinik)
            if poliklinik == 1:
                return "Poliklinik Penyakit Dalam", "PD"
            elif poliklinik == 2:
                return "Poliklinik Anak", "AN"
            elif poliklinik == 3:
                return "Poliklinik Kulit dan Kelamin", "KK"
            elif poliklinik == 4:
                return "Poliklinik Mata", "MA"
            elif poliklinik == 5:
                return "Poliklinik Gigi dan Mulut", "GM"
            elif poliklinik == 6:
                return "Poliklinik Orthopedi dan Traumatologi", "ORT"
            else:
                print("Input tidak valid. Silahkan pilih kembali")
                continue
        else:
            print("Input harus berupa angka!")

def pasien_reguler():
    print("\n============= PASIEN REGULER =============")
    while True:
        nomer_ktp = input("Nomer KTP (16 digit) : ")
        if len(nomer_ktp) == 16 and nomer_ktp.isdigit():
            break
        print(f"Nomer invalid. Maksimal digit adalah 16 angka")
    print("=======================================")
    nama = input("Masukkan Nama : ")
    print("=======================================")
    while True:
        tanggal_lahir = input("Tanggal Lahir (DD-MM-YYYY) : ")
        if len(tanggal_lahir) == 8 and tanggal_lahir.isdigit():
            break
        print("Nomer invalid harus berisi 8 angka")
    print("=======================================")
    while True:
        print("Pilihan Gender\n 1. Laki - laki\n 2. Perempuan")
        gender = input("Pilih opsi (1 / 2) : ")
        if gender == "1":
            gender = "Laki - laki"
            break
        elif gender == "2":
            gender = "Perempuan"
            break
        else:
            print("Pilih sesuai opsi!")
    print("=======================================")
    while True:
        asal_kota = input("Masukkan asal Kota : ")
        if asal_kota.isalpha():
            break
        print("Masukkan Kota yang benar!")

    poliklinik, tarif, type = pilih_poli_reguler()
    hari_berobat = tanggal_berobat()
    nomor_urut = hitung_nomor_urut_Reguler(poliklinik, hari_berobat)
    list_hasil_pencarian_Reguler(nomer_ktp, nama, tanggal_lahir, gender, asal_kota, poliklinik, hari_berobat, tarif, type, nomor_urut)

    dataPasien = {
        "No. KTP": nomer_ktp,
        "Nama Pasien": nama,
        "Tanggal Lahir": tanggal_lahir,
        "Gender": gender,
        "Alamat Pasien": asal_kota,
        "Poliklinik": poliklinik,
        "Hari Berobat": hari_berobat,
        "Tarif Harga": tarif,
        "Nomor Urut": nomor_urut,
        "Type": type
    }

    while True:
        cek_valid = input("Apakah data sudah benar (ya/tidak) ? ").lower()
        print("========================================")
        if cek_valid == "ya":
            dataKeseluruhan.append(dataPasien)
            dataPasienReguler.append(dataPasien)
            print("Data pasien berhasil terdaftar...")
            print("========================================")
            break
        elif cek_valid == "tidak":
            print("Pembatalan pasien berhasil...")
            print("========================================")
            break
        else:
            print("Input tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")
   
    return nomer_ktp, nama, tanggal_lahir, gender, asal_kota, poliklinik, hari_berobat, tarif, type

def list_hasil_pencarian_Reguler(nomer_ktp, nama, tanggal_lahir, gender, asal_kota, poliklinik, hari_berobat, tarif, type, nomor_urut):
    print("\n============= DATA PASIEN =============")
    print(f"No. Urut          : {type}-{nomor_urut}")
    print(f"No. KTP           : {nomer_ktp}")
    print(f"Nama Pasien       : {nama}")
    print(f"Tanggal Lahir     : {tanggal_lahir}")
    print(f"Jenis Kelamin     : {gender}")
    print(f"Alamat Pasien     : {asal_kota}")
    print(f"Poliklinik        : {poliklinik}")
    print(f"Hari Berobat      : {hari_berobat}")
    print(f"Tarif Harga       : Rp. {tarif}")
    print("========================================")

def pilih_poli_reguler():
    print("\n============= PILIH POLIKLINIK =============")
    print(" 1. Poliklinik Penyakit Dalam\n 2. Poliklinik Anak\n 3. Poliklinik Kulit dan Kelamin\n 4. Poliklinik Mata\n 5. Poliklinik Gigi dan Mulut\n 6. Poliklinik Orthopedi dan Traumatologi")
   
    tarif = 0

    while True:
        print("==================================")
        poliklinik = input("Silahkan pilih poliklinik : ")
        if poliklinik.isdigit():
            poliklinik = int(poliklinik)
            if poliklinik == 1:
                poliklinik = "Poliklinik Penyakit Dalam"
                tarif += 500000
                type = "PD-R"
            elif poliklinik == 2:
                poliklinik = "Poliklinik Anak"
                tarif += 200000
                type = "AN-R"
            elif poliklinik == 3:
                poliklinik = "Poliklinik Kulit dan Kelamin"
                tarif += 300000
                type = "KK-R"
            elif poliklinik == 4:
                poliklinik = "Poliklinik Mata"
                tarif += 150000
                type = "MA-R"
            elif poliklinik == 5:
                poliklinik = "Poliklinik Gigi dan Mulut"
                tarif += 100000
                type = "GM-R"
            elif poliklinik == 6:
                poliklinik = "Poliklinik Orthopedi dan Traumatologi"
                tarif += 800000
                type = "ORT-R"
            else:
                print("Input tidak valid. Silahkan pilih kembali")
                continue
            return poliklinik, tarif, type
        else:
            print("Input harus berupa angka!")

def pasien_ugd():
    print("\n============= PASIEN GAWAT DARURAT =============")
    while True:
        nomer_ktp = input("Nomer KTP (16 digit) : ")
        if len(nomer_ktp) == 16 and nomer_ktp.isdigit():
            break
        print(f"Nomer invalid. Maksimal digit adalah 16 angka")
    print("=======================================")
    nama = input("Masukkan Nama : ")
    print("=======================================")
    while True:
        tanggal_lahir = input("Tanggal Lahir (DD-MM-YYYY) : ")
        if len(tanggal_lahir) == 8 and tanggal_lahir.isdigit():
            break
        print("Nomer invalid harus berisi 8 angka")
    print("=======================================")
    while True:
        print("Pilihan Gender\n 1. Laki - laki\n 2. Perempuan")
        gender = input("Pilih opsi (1 / 2) : ")
        if gender == "1":
            gender = "Laki - laki"
            break
        elif gender == "2":
            gender = "Perempuan"
            break
        else:
            print("Pilih sesuai opsi!")
    print("=======================================")
    while True:
        asal_kota = input("Masukkan asal Kota : ")
        if asal_kota.isalpha():
            break
        print("Masukkan Kota yang benar!")

    poliklinik, lama_rawat_inap, total, cek_pasien_bpjs, status_pasien = pilih_poli_ugd()

    dataPasien = {
        "No. KTP": nomer_ktp,
        "Nama Pasien": nama,
        "Tanggal Lahir": tanggal_lahir,
        "Gender": gender,
        "Alamat Pasien": asal_kota,
        "Poliklinik": poliklinik,
        "Lama Rawat Inap": lama_rawat_inap,
        "Tarif Harga": total,
        "Pengguna BPJS": cek_pasien_bpjs,
        "Status": status_pasien
    }

    daftar_data_pasien_ugd(nomer_ktp, nama, tanggal_lahir, gender, asal_kota, poliklinik, lama_rawat_inap, total, cek_pasien_bpjs, status_pasien)

    while True:
        print("=======================================")
        cek_valid = input("Apakah data sudah benar (ya/tidak) ? ").lower()
        print("=======================================")
        if cek_valid.isalpha():
            if cek_valid == "ya":
                dataPasienUGD.append(dataPasien)
                print("Data pasien berhasil terdaftar...")
                print("=======================================")
                break
            elif cek_valid == "tidak":
                print("Pembatalan berhasil...")
                print("=======================================")
                break
            else:
                print("Input tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")
        else:
            print("Input harus berupa huruf!")

    return nomer_ktp, nama, tanggal_lahir, gender, asal_kota, poliklinik, lama_rawat_inap, total, cek_pasien_bpjs,status_pasien

def pilih_poli_ugd():
    print("\n============= PILIH POLIKLINIK =============")
    print(" 1. Poliklinik Penyakit Dalam\n 2. Poliklinik Anak\n 3. Poliklinik Kulit dan Kelamin\n 4. Poliklinik Mata\n 5. Poliklinik Gigi dan Mulut\n 6. Poliklinik Orthopedi dan Traumatologi")
   
    tarif = 0
    status_pasien = "Rawat Inap"

    while True:
        poliklinik = input("Silahkan pilih poliklinik : ")
        if poliklinik.isdigit():
            poliklinik = int(poliklinik)
            if poliklinik == 1:
                poliklinik = "Poliklinik Penyakit Dalam"
                tarif += 500000
                break
            elif poliklinik == 2:
                poliklinik = "Poliklinik Anak"
                tarif += 200000
                break
            elif poliklinik == 3:
                poliklinik = "Poliklinik Kulit dan Kelamin"
                tarif += 300000
                break
            elif poliklinik == 4:
                poliklinik = "Poliklinik Mata"
                tarif += 150000
                break
            elif poliklinik == 5:
                poliklinik = "Poliklinik Gigi dan Mulut"
                tarif += 100000
                break
            elif poliklinik == 6:
                poliklinik = "Poliklinik Orthopedi dan Traumatologi"
                tarif += 800000
                break
            else:
                print("Input tidak valid. Silahkan pilih kembali")
                continue
        else:
            print("Input harus berupa angka!")
    print("=======================================")
    while True:
        lama_rawat_inap = input("Berapa lama rawat inap : ")
        if lama_rawat_inap.isdigit():
            lama_rawat_inap = int(lama_rawat_inap)
            tarif_hari = 250000 * lama_rawat_inap
            break
        else:
            print("Input harus berupa angka!")
    
    while True:
        print("=======================================")
        cek_pasien_bpjs = input("Apakah pasien pengguna PBJS (ya / tidak): ").lower()
        print("=======================================")
        if cek_pasien_bpjs.isalpha():
            if cek_pasien_bpjs == "ya" or cek_pasien_bpjs == "iya":
                cek_pasien_bpjs = "BPJS"
                break
            elif cek_pasien_bpjs == "tidak":
                cek_pasien_bpjs = "Reguler"
                total = tarif + tarif_hari
                break
            else:
                print("Input sesuai opsi!")
        else:
            print("Input harus berupa huruf (ya / tidak)")

    if cek_pasien_bpjs == "BPJS":
        if poliklinik == "Poliklinik Penyakit Dalam":
            diskon = 20
            potongan = 500000 * diskon // 100
            total = (500000 - potongan) + tarif_hari
        elif poliklinik == "Poliklinik Anak":
            diskon = 10
            potongan = 200000 * diskon // 100
            total = (200000 - potongan) + tarif_hari
        elif poliklinik == "Poliklinik Kulit dan Kelamin":
            diskon = 15
            potongan = 300000 * diskon // 100
            total = (300000 - potongan) + tarif_hari
        elif poliklinik =="Poliklinik Mata":
            diskon = 10
            potongan = 150000 * diskon // 100
            total = (150000 - potongan) + tarif_hari
        elif poliklinik == "Poliklinik Gigi dan Mulut":
            diskon = 5
            potongan = 100000 * diskon // 100
            total = (100000 - potongan) + tarif_hari
        elif poliklinik == "Poliklinik Orthopedi dan Traumatologi":
            diskon = 15
            potongan = 800000 * diskon // 100
            total = (800000 - potongan) + tarif_hari
   
    return poliklinik, lama_rawat_inap, total, cek_pasien_bpjs, status_pasien
            
def daftar_data_pasien_ugd(nomer_ktp, nama, tanggal_lahir, gender, asal_kota, poliklinik, lama_rawat_inap, total, cek_pasien_bpjs, status_pasien):
    print("\n============= DATA PASIEN =============")
    print(f"No. BPJS          : {nomer_ktp}")
    print(f"Nama Pasien       : {nama}")
    print(f"Tanggal Lahir     : {tanggal_lahir}")
    print(f"Jenis Kelamin     : {gender}")
    print(f"Alamat Pasien     : {asal_kota}")
    print(f"Poliklinik        : {poliklinik}")
    print(f"Hari Berobat      : {lama_rawat_inap} Hari")
    print(f"Tarif Harga       : Rp. {total}")
    print(f"Pengguna BPJS     : {cek_pasien_bpjs}")
    print(f"Status Pasien     : {status_pasien}")

def tanggal_berobat():
    print("\n============= PILIH HARI =============")
    print(" Pilih Hari Berobat\n 1. Senin\n 2. Selasa\n 3. Rabu\n 4. Kamis\n 5. Jumat\n 6. Sabtu (Pelayanan Libur)\n 7. Minggu (Pelayanan Libur)")
    print("=======================================")
    while True:
        pilihan = input("Silahkan pilih hari berobat (1-7): ")
        if pilihan.isdigit():
            if pilihan == "1":
                hari = "Senin"
            elif pilihan == "2":
                hari = "Selasa"
            elif pilihan == "3":
                hari = "Rabu"
            elif pilihan == "4":
                hari = "Kamis"
            elif pilihan == "5":
                hari = "Jumat"
            elif pilihan == "6" or pilihan == "7":
                print("Pelayanan tidak tersedia pada hari tersebut.")
                continue
            else:
                print("Input tidak valid. Silahkan pilih antara 1-7.")
            return hari
        else:
            print("Input harus angka!")

def arsipDataPasien():
    print("\n===== ARSIP DATA PASIEN =====")
    print("1. Arsipkan Pasien BPJS")
    print("2. Arsipkan Pasien Reguler")
    print("3. Arsipkan Pasien Rawat Inap")
    print("4. Data Pasien Ter-Arsip")
    print("=======================================")

    while True:
        pilih = input("Pilih nemu yang ada : ")
        print("=======================================")
        if pilih == "1":
            arsipBPJS()
            break
        elif pilih == "2":
            arsipReguler()
            break
        elif pilih == "3":
            arsipUGD()
            break
        elif pilih == "4":
            arsipPasien()
            break
        else:
            print("Pilih opsi yang ada!")

def admin():
    print("\n===== ADMIN ADMINTRASI =====")
    print("1. Pasien BPJS")
    print("2. Pasien Reguler")
    print("3. Pasien Rawat Inap")
    print("4. Cari Data Pasien")
   
    while True:
        print("=======================================")
        pilih = input("Pilih nemu yang ada : ")
        
        if pilih == "1":
            daftarPasienBPJS()
            break
        elif pilih == "2":
            daftarPasienReguler()
            break
        elif pilih == "3":
            ugd()
            break
        elif pilih == "4":
            cariDataPasien()
            break
        else:
            print("Pilih opsi yang ada!")

def cariDataPasien():
    print("===== CARI DATA PASIEN =====")
    print("=======================================")
    print("Pencarian Berdasarkan Poliklinik:")
    print("1. Poliklinik Penyakit Dalam")
    print("2. Poliklinik Anak")
    print("3. Poliklinik Kulit dan Kelamin")
    print("4. Poliklinik Mata")
    print("5. Poliklinik Gigi dan Mulut")
    print("6. Poliklinik Orthopedi dan Traumatologi")
    print("=======================================")
    while True:
        poliklinik = input("Pilih opsi yang ada (1 - 6) : ")
        print("=======================================")
        
        if poliklinik == "1":
            poliklinik = "Poliklinik Penyakit Dalam"
            break
        elif poliklinik == "2":
            poliklinik = "Poliklinik Anak"
            break
        elif poliklinik == "3":
            poliklinik = "Poliklinik Kulit dan Kelamin"
            break
        elif poliklinik == "4":
            poliklinik = "Poliklinik Mata"
            break
        elif poliklinik == "5":
            poliklinik = "Poliklinik Gigi dan Mulut"
            break
        elif poliklinik == "6":
            poliklinik = "Poliklinik Orthopedi dan Traumatologi"
            break
        else:
            print("Pilih opsi yang ada!")
    
    print("Pilih Hari:")
    print("1. Senin")
    print("2. Selasa")
    print("3. Rabu")
    print("4. Kamis")
    print("5. Jumat")
    print("=======================================")

    while True:
        hari = input("Pilih Hari Pasien Dicari (1 - 5): ")
        print("=======================================")

        if hari == "1":
            hari = "Senin"
            break
        elif hari == "2":
            hari = "Selasa"
            break
        elif hari == "3":
            hari = "Rabu"
            break
        elif hari == "4":
            hari = "Kamis"
            break
        elif hari == "5":
            hari = "Jumat"
            break
        else:
            print("Pilih opsi yang ada!")

    hasilBPJS = []
    hasilReguler = []
    
    for data in dataKeseluruhan:
        if data["Poliklinik"] == poliklinik and data["Hari Berobat"] == hari:
            if "No. BPJS" in data:
                hasilBPJS.append(data)
            else:
                hasilReguler.append(data)

    if hasilBPJS:
        print("Hasil Pencarian (BPJS): ")
        for pasien in hasilBPJS:
            print(f"No. Urut          : {pasien["Nomor Urut"]}")
            print(f"No. BPJS          : {pasien["No. BPJS"]}")
            print(f"Nama Pasien       : {pasien["Nama Pasien"]}")
            print(f"Tanggal Lahir     : {pasien["Tanggal Lahir"]}")
            print(f"Jenis Kelamin     : {pasien["Gender"]}")
            print(f"Alamat Pasien     : {pasien["Alamat Pasien"]}")
            print(f"Asal Rujukan      : {pasien["Rujukan"]}")
            print(f"Poliklinik        : {pasien["Poliklinik"]}")
            print(f"Hari Berobat      : {pasien["Hari Berobat"]}")
            print("=======================================")
    else:
        print("Tidak ada data Pasien BPJS yang ditemukan")
        print("============================================")

    if hasilReguler:
        print("Hasil Pencarian (Reguler):")
        for pasien in hasilReguler:
            print(f"No. Urut          : {pasien["Nomor Urut"]}")
            print(f"No. KTP           : {pasien['No. KTP']}")
            print(f"Nama Pasien       : {pasien['Nama Pasien']}")
            print(f"Tanggal Lahir     : {pasien['Tanggal Lahir']}")
            print(f"Jenis Kelamin     : {pasien['Gender']}")
            print(f"Alamat Pasien     : {pasien['Alamat Pasien']}")
            print(f"Poliklinik        : {pasien['Poliklinik']}")
            print(f"Hari Berobat      : {pasien['Hari Berobat']}")
            print(f"Tarif Harga       : {pasien['Tarif Harga']}")
            print("=======================================")
    else:
        print("Tidak ada data Pasien Reguler yang ditemukan")
        print("============================================")

def daftarPasienBPJS():
    print("\n===== DATA PASIEN BPJS =====")
    if not dataPasienBPJS :
        print("Tidak ada data pasien.....")
        print("=======================================")

    for i in range(len(dataPasienBPJS)):
        data = dataPasienBPJS[i]
        print(f"\n{i + 1}. No. Urut        : {data['Nomor Urut']}")
        print(f"   No. BPJS        : {data['No. BPJS']}")
        print(f"   Nama Pasien     : {data['Nama Pasien']}")
        print(f"   Tanggal Lahir   : {data['Tanggal Lahir']}")
        print(f"   Jenis Kelamin   : {data['Gender']}")
        print(f"   Alamat Pasien   : {data['Alamat Pasien']}")
        print(f"   Asal Rujukan    : {data['Rujukan']}")
        print(f"   Poliklinik      : {data['Poliklinik']}")
        print(f"   Hari Berobat    : {data['Hari Berobat']}")
        print("=======================================")

def daftarPasienReguler():
    print("\n===== DATA PASIEN REGULER =====")
    if not dataPasienReguler :
        print("Tidak ada data pasien.....")
    print("=======================================")

    for i in range(len(dataPasienReguler)):
        data = dataPasienReguler[i]
        print(f"\n{i + 1}. No. Urut        : {data['Nomor Urut']}")
        print(f"   No. KTP         : {data['No. KTP']}")
        print(f"   Nama Pasien     : {data['Nama Pasien']}")
        print(f"   Tanggal Lahir   : {data['Tanggal Lahir']}")
        print(f"   Jenis Kelamin   : {data['Gender']}")
        print(f"   Alamat Pasien   : {data['Alamat Pasien']}")
        print(f"   Poliklinik      : {data['Poliklinik']}")
        print(f"   Hari Berobat    : {data['Hari Berobat']}")
        print(f"   Tarif           : {data['Tarif Harga']}")
        print("=======================================")

def arsipBPJS():
    print("\n===== DATA PASIEN BPJS =====")
    if not dataPasienBPJS :
        print("Tidak ada data pasien.....")
        print("=======================================")
        return

    for i in range(len(dataPasienBPJS)):
        data = dataPasienBPJS[i]
        print(f"\n{i + 1}. No. Urut        : {data['Nomor Urut']}")
        print(f"   No. BPJS        : {data['No. BPJS']}")
        print(f"   Nama Pasien     : {data['Nama Pasien']}")
        print(f"   Tanggal Lahir   : {data['Tanggal Lahir']}")
        print(f"   Jenis Kelamin   : {data['Gender']}")
        print(f"   Alamat Pasien   : {data['Alamat Pasien']}")
        print(f"   Asal Rujukan    : {data['Rujukan']}")
        print(f"   Poliklinik      : {data['Poliklinik']}")
        print(f"   Hari Berobat    : {data['Hari Berobat']}")
        print("=======================================")

    while True:
        pilih = input("Pilih data yang ingin diubah : ")
        print("=======================================")
        if not pilih.isdigit():
            print("Input harus berupa angka.")
            print("=======================================")

        if pilih.isalpha() or int(pilih) < 1 or int(pilih) > len(dataPasienBPJS):
            print("Nomor invalid. Pilih nomor yang sesuai.")
            print("=======================================")
        else:
            pilih = int(pilih)
            data_pasien = dataPasienBPJS[pilih - 1]
            konfirmasi = input("Apakah anda yakin? (ya/tidak): ").lower()
            if konfirmasi == "ya":
                dataArsipPasien.append(data_pasien)
                dataArsipBPJS.append(data_pasien)
                dataPasienBPJS.pop(pilih - 1)
                print("Berhasil mengubah..")
                print("=======================================")
                break
            elif konfirmasi == "tidak":
                print("Tidak ada data yang diubah..")
                print("=======================================")
                break
            else:
                print("Pilih sesuai opsi!")

def arsipReguler():
    print("\n===== DATA PASIEN REGULER =====")
    if not dataPasienReguler :
        print("Tidak ada data pasien.....")
        print("=======================================")
        return

    for i in range(len(dataPasienReguler)):
        data = dataPasienReguler[i]
        print(f"\n{i + 1}. No. Urut        : {data['Nomor Urut']}")
        print(f"   No. KTP         : {data['No. KTP']}")
        print(f"   Nama Pasien     : {data['Nama Pasien']}")
        print(f"   Tanggal Lahir   : {data['Tanggal Lahir']}")
        print(f"   Jenis Kelamin   : {data['Gender']}")
        print(f"   Alamat Pasien   : {data['Alamat Pasien']}")
        print(f"   Poliklinik      : {data['Poliklinik']}")
        print(f"   Hari Berobat    : {data['Hari Berobat']}")
        print(f"   Tarif           : {data['Tarif Harga']}")
        print("=======================================")

    while True:
        pilih = input("Pilih data yang ingin diubah : ")
        print("=======================================")
        if not pilih.isdigit():
            print("Input harus berupa angka.")
            print("=======================================")
 
        if pilih.isalpha() or int(pilih) < 1 or int(pilih) > len(dataPasienReguler):
            print("Nomor invalid. Pilih nomor yang sesuai.")
            print("=======================================")
        else:
            pilih = int(pilih)
            data_pasien = dataPasienReguler[pilih - 1]
            konfirmasi = input("Apakah anda yakin? (ya/tidak): ").lower()
            if konfirmasi == "ya":
                dataArsipPasien.append(data_pasien)
                dataArsipReguler.append(data_pasien)
                dataPasienReguler.pop(pilih - 1)
                print("Berhasil mengubah..")
                print("=======================================")
                break
            elif konfirmasi == "tidak":
                print("Tidak ada data yang diubah..")
                print("=======================================")
                break
            else:
                print("Pilih sesuai opsi!")

def arsipPasien():
    hasilBPJS = []
    hasilReguler = []
    hasilUGD = []
    
    for data in dataArsipPasien:
        if "No. BPJS" in data:
            hasilBPJS.append(data)
        elif "Status" in data:
            hasilUGD.append(data)
        else:
            hasilReguler.append(data)

    if hasilBPJS:
        print("Hasil Pencarian (BPJS): ")
        for pasien in hasilBPJS:
            print(f"No. Urut          : {pasien["Nomor Urut"]}")
            print(f"No. BPJS          : {pasien["No. BPJS"]}")
            print(f"Nama Pasien       : {pasien["Nama Pasien"]}")
            print(f"Tanggal Lahir     : {pasien["Tanggal Lahir"]}")
            print(f"Jenis Kelamin     : {pasien["Gender"]}")
            print(f"Alamat Pasien     : {pasien["Alamat Pasien"]}")
            print(f"Asal Rujukan      : {pasien["Rujukan"]}")
            print(f"Poliklinik        : {pasien["Poliklinik"]}")
            print(f"Hari Berobat      : {pasien["Hari Berobat"]}")
            print("=======================================")
    else:
        print("Tidak ada data Pasien BPJS yang ditemukan")
        print("=======================================")

    if hasilReguler:
        print("Hasil Pencarian (Reguler):")
        for pasien in hasilReguler:
            print(f"No. Urut          : {pasien["Nomor Urut"]}")
            print(f"No. KTP           : {pasien['No. KTP']}")
            print(f"Nama Pasien       : {pasien['Nama Pasien']}")
            print(f"Tanggal Lahir     : {pasien['Tanggal Lahir']}")
            print(f"Jenis Kelamin     : {pasien['Gender']}")
            print(f"Alamat Pasien     : {pasien['Alamat Pasien']}")
            print(f"Poliklinik        : {pasien['Poliklinik']}")
            print(f"Hari Berobat      : {pasien['Hari Berobat']}")
            print(f"Tarif Harga       : {pasien['Tarif Harga']}")
            print("=======================================")
    else:
        print("Tidak ada data Pasien Reguler yang ditemukan")
        print("=======================================")

    if hasilUGD:
        print("Hasil Pencarian (UGD):")
        for pasien in hasilUGD:
            print(f"No. KTP           : {pasien['No. KTP']}")
            print(f"Nama Pasien       : {pasien['Nama Pasien']}")
            print(f"Tanggal Lahir     : {pasien['Tanggal Lahir']}")
            print(f"Jenis Kelamin     : {pasien['Gender']}")
            print(f"Alamat Pasien     : {pasien['Alamat Pasien']}")
            print(f"Poliklinik        : {pasien['Poliklinik']}")
            print(f"Lama Rawat Inap   : {pasien['Lama Rawat Inap']}")
            print(f"Tarif Harga       : Rp. {pasien['Tarif Harga']}")
            print(f"Pengguna BPJS     : {pasien['Pengguna BPJS']}")
            print(f"Status Pasien     : {pasien['Status']}")
            print("=======================================")
    else:
        print("Tidak ada data Pasien UGD yang ditemukan")
        print("=======================================")

def arsipUGD():
    print("\n===== ARSIP DATA PASIEN RAWAT INAP =====")
    if not dataPasienUGD :
        print("Tidak ada data pasien.....")
        print("=======================================")
        return

    for i in range(len(dataPasienUGD)):
        data = dataPasienUGD[i]
        print(f"\n{i + 1}. No. KTP: {data['No. KTP']}\n   Nama: {data['Nama Pasien']}\n   Alamat Pasien: {data['Alamat Pasien']}\n   Poliklinik: {data['Poliklinik']}\n   Tarif: {data['Tarif Harga']}\n   Status: {data['Status']}")
        print("=======================================")

    while True:
        perubahan = input("Apakah ingin mengarsipkan (ya / tidak)? ").lower() #disini ada minus
        print("=======================================")
        if perubahan.isalpha():
            if perubahan == "ya":
                while True:
                    if not dataPasienUGD:
                        print("Tidak ada data Pasien")
                        print("=======================================")
                        break
                    else:
                        pilih = input("Pilih data yang ingin diubah : ") #ada yang minus woi
                        print("=======================================")
                        
                        if not pilih.isdigit() or int(pilih) < 1 or int(pilih) > len(dataPasienUGD):
                            print("Nomer invalid..")
                        else:
                            pilih = int(pilih)
                            data_pasien = dataPasienUGD[pilih - 1]
                            tambahan_harga = input("Apakah ada tambahan harga (ya / tidak) ? ")
                            print("=======================================")
                            
                            if tambahan_harga == "ya":
                                if not dataPasienUGD:
                                    print()
                                    print("Tidak ada data pasien.....")
                                    print("=======================================")
                                    print()
                                else:
                                    while True:
                                        tambahTarif = input("Masukkan Harga : ")
                                        print("=======================================")
                                        if tambahTarif.isdigit():
                                            tambahTarif = int(tambahTarif)
                                            data_pasien["Tarif Harga"] += tambahTarif
                                            break
                                        else:
                                            print("Input harus angka!")
                                    
                                    konfirmasi = input("Apakah anda yakin? (ya/tidak): ").lower()
                                    print("=======================================")
                                    if konfirmasi == "ya":
                                        data_pasien["Status"] = "Selesai"
                                        dataArsipPasien.append(data_pasien)
                                        dataArsipUGD.append(data_pasien)
                                        dataPasienUGD.pop(pilih - 1)
                                        print("Berhasil mengubah..")
                                        print("=======================================")
                                        break
                                    elif konfirmasi == "tidak":
                                        print("Tidak ada data yang di ubah..")
                                    else:
                                        print("Pilih sesuai opsi!")

                            elif tambahan_harga == "tidak":
                                data_pasien["Status"] = "Selesai"
                                dataArsipPasien.append(data_pasien)
                                dataArsipUGD.append(data_pasien)
                                dataPasienUGD.pop(pilih - 1)
                                print("Berhasil mengubah..")
                                print("=======================================")
                                break
                            else:
                                print("Pilih 'ya' atau 'tidak'")

            elif perubahan == "tidak":
                print("Tidak ada data yang diubah. Terimakasih")
                print("=======================================")
                break
            else:
                print("Pilih opsi (ya / tidak)!")
        else:
            print("Input harus berupa opsi yang ada")

def ugd():
    print("\n===== DATA PASIEN RAWAT INAP =====")
    if not dataPasienUGD :
        print("Tidak ada data pasien.....")
        print("=======================================")
        return

    for i in range(len(dataPasienUGD)):
        data = dataPasienUGD[i]
        print(f"\n{i + 1}. No. KTP: {data['No. KTP']}\n   Nama: {data['Nama Pasien']}\n   Alamat Pasien: {data['Alamat Pasien']}\n   Poliklinik: {data['Poliklinik']}\n   Tarif: {data['Tarif Harga']}\n   Status: {data['Status']}")
        print("=======================================")
    
def login():
    print("=====================================")
    print("========   SELAMAT DATANG    ========")
    while True:
        password = input("Masukkan Password Admin Adminitrasi: ")
        print("==================================================")
        if password == "Admin123":
            print("\n Berhasil Login...")
            print("\n=============================")
            print(" Selamat Datang Admin Dimas")
            break
        elif password == "Admin12":
            print("\n Berhasil Login...")
            print("\n=============================")
            print(" Selamat Datang Admin Sheva")
            break
        else:
            print("Password salah. Silahkan isi dengan benar!")

login()

while True :
    tampilan_menu()
    print("==============================================")
    pilih_menu = input("Silahkan pilih menu yang tersedia : ")

    if pilih_menu == "1" :
        information()
    elif pilih_menu == "2" :
        pasien_bpjs()
    elif pilih_menu == "3" :
        pasien_reguler()
    elif pilih_menu == "4" :
        pasien_ugd()
    elif pilih_menu == "5" :
        arsipDataPasien()
    elif pilih_menu == "6" :
        admin()
    elif pilih_menu == "7" :
        print("Terimakasih...")
        login()
    elif pilih_menu == "8" :
        print("Terimakasih...")
        break
    else:
        print("=====================================================================")
        print("Pilihan tidak valid. Silakan pilih sesuai menu yang sudah disediakan.")
        print("=====================================================================")
    