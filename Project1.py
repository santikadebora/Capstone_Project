Menu ='''
========== Data Record Karyawan Perusahaan ==========

    1. Report Data Karyawan
    2. Menambah Data Karyawan
    3. Mengubah Data Karyawan
    4. Menghapus Data Karyawan
    5. Exit  
'''

Karyawan =[
    {'NIK' : '001', 'Nama' : 'Amanda', 'Gender': 'Wanita', 'Domisili': 'Jakarta Barat','Status':'Karyawan'},
    {'NIK': '002', 'Nama': 'Hendy', 'Gender' : 'Pria', 'Domisili': 'Jakarta Selatan', 'Status': 'Magang'},
    {'NIK': '003', 'Nama': 'Lisna', 'Gender' : 'Wanita', 'Domisili': 'Jakarta Timur', 'Status': 'Karyawan'},
    {'NIK': '004', 'Nama': 'Bryan', 'Gender' : 'Pria', 'Domisili': 'Jakarta Utara', 'Status': 'Magang'}
]

# Read data Function
def ReadMenu():
    print("********** Report Data Karyawan **********")    
    print("\n")
    print("1. Report Seluruh Data")     
    print("2. Report Data Tertentu")
    print("3. Kembali ke Menu Utama")
    menuInputRead = input("Silahkan Pilih Sub Menu Read Data [1-3]: ")
    if menuInputRead == '1':
        if len(Karyawan) != 0:
            print('Daftar Karyawan: ')
            for j,i in enumerate (Karyawan):
                print(f"""{j+1}. NIK : {i['NIK']}, Nama :{i['Nama']}, Gender : {i['Gender']}, Domisili :{i['Domisili']}, Status: {i['Status']}""")
        else:
            print('\n----- Tidak Ada Data Karyawan -----')
    elif menuInputRead == '2':
        if len(Karyawan) != 0:
            std = input("Masukan NIK : ").upper()
            print("Data Karyawan dengan NIK : ", std)
            totalFind = 0
            for j, i in enumerate (Karyawan):
                if i['NIK'] == std:
                    print(f"\n{j+1}. NIK : {i['NIK']}, Nama :{i['Nama']}, Gender : {i['Gender']}, Domisili :{i['Domisili']}, Status: {i['Status']}")
                    totalFind += 1
            if totalFind == 0:
                print('----- Tidak Ada Data Karyawan -----')
    elif menuInputRead == '3':
        Play()     
    else:
        print('\n----- Pilihan Menu Tidak Terdaftar -----')
    ReadMenu()

# Create Data Function
def CreateMenu():
    print("********** Menambah Data Karyawan **********")
    print("1. Tambah Data Karyawan")     
    print("2. Kembali ke Menu Utama")
    menuInputCreate = input("Silahkan Pilih Sub menu Create Data [1-2]: ")
    if menuInputCreate == "1":
        if len (Karyawan) != 0:
            addNIK= input("Masukan NIK : ").upper()
            for j, i in enumerate (Karyawan):
                if addNIK == i['NIK']:
                    print('Data Karyawan Sudah Ada')
                    CreateMenu()
            addNama    = input('Masukan Nama: ')
            addGender  = input('Masukan Gender: ')
            addDomisili= input('Masukan Domisili: ')
            addStatus  = input('Masukan Status: ')
            
            createData = { 
                'NIK' : '{}'.format(addNIK),
                'Nama': '{}'.format(addNama),
                'Gender': '{}'.format(addGender),
                'Domisili': '{}'.format(addDomisili),
                'Status': '{}'.format(addStatus),
            }
            print ('\nData Karyawan yang di tambahkan adalah: ',createData)
            checkerCreate = input('\nApakah Data akan disimpan?(Y/N): ').upper()
            if checkerCreate == "Y":
                Karyawan.append (createData)
                print('\n----- Data Karyawan Berhasil di Tambahkan -----')
            elif checkerCreate == "N":
                print('\n----- Data Karyawan Tidak di Tambahkan -----')
            else:
                checkerCreate = input('\nApakah Data akan disimpan?(Y/N): ').upper() 
    elif menuInputCreate == "2":
        Play()
    else :
        print('\n----- Pilihan Menu Tidak Ada -----')
    CreateMenu()

#Update Data Function
def UpdateMenu() :    
    print("********** Mengubah Data Karyawan **********")
    print("1. Ubah Data Karyawan")     
    print("2. Kembali ke Menu Utama")
    menuInputUpdate = input("Silahkan Pilih Sub menu Create Data [1-2]: ")
    if menuInputUpdate == "1":
        if len (Karyawan) != 0: 
            inputNIK = input("Masukan NIK : ").upper()
            totalFind = 0
            for j, i in enumerate (Karyawan):
                if inputNIK == i['NIK']:
                    print(f"""{j+1}. Nama :{i['Nama']}, Gender :{i['Gender']}, Domisili :{i['Domisili']}, Status:{i['Status']}""")
                    totalFind += 1
            if totalFind == 0:
                print('----- Tidak Ada Data Karyawan -----')
            else :
                askUpdate = input ('Tekan Y jika ingin lanjut update data atau N jika ingin cancel update (Y/N): ').capitalize()
                if askUpdate == "Y":
                    fieldUpdate = input('Masukan Kolom/Keterangan yang ingin di Update(NIK/Nama/Gender/Domisili/Status): ').capitalize()
                    # make sure input key is NIK (Uppercase)
                    if fieldUpdate == 'Nik' or fieldUpdate == 'nik':
                        fieldUpdate = 'NIK'

                    if fieldUpdate == 'NIK' or 'Nama' or 'Gender' or 'Domisili' or 'Status':
                        valueUpdate = input("Masukan "+ str(fieldUpdate) +" Baru: ")
                        askUpdate = input('Apakah Data akan diUpdate? (Y/N): ').upper()
                        if askUpdate == "Y":
                            # Update process
                            for j, i in enumerate (Karyawan):
                                if inputNIK == i['NIK']:
                                    Karyawan[j][f'{fieldUpdate}']= valueUpdate 
                                    print('Data Karyawan Berhasil diupdate')
                        elif askUpdate == "N":
                            print("Data Tidak Terupdate")                   
    elif menuInputUpdate == "2":
        Play()
    else :
        print('\n----- Pilihan Menu Tidak Ada -----')
    UpdateMenu()     

# Delete Data Function
def DeleteMenu():
    print("********** Menghapus Data Karyawan **********")
    print("1. Hapus Data Karyawan")     
    print("2. Kembali ke Menu Utama")
    menuInputDelete = input("Silahkan Pilih Sub menu Create Data [1-2]: ")
    if menuInputDelete == "1":
        if len (Karyawan) != 0: 
            deleteNIK = input("Masukan NIK : ").upper()
            totalFind = 0
            for j, i in enumerate (Karyawan):
                if deleteNIK == i['NIK']:
                    print(f"""{j+1}. Nama :{i['Nama']}, Gender :{i['Gender']}, Domisili :{i['Domisili']}, Status:{i['Status']}""")
                    totalFind += 1
            if totalFind == 0:
                print('Data Karyawan Tidak Ada')
            else:
                askdelete = input('Apakah Data akan di Hapus? (Y/N): ').upper()
                if askdelete == "Y":
                    # delete process
                    for j, i in enumerate (Karyawan):
                        if deleteNIK == i['NIK']:
                            del Karyawan[j]
                            print('Data Karyawan Berhasil dihapus')
                elif askdelete == "N":
                    print('Data tidak terhapus')                          
    elif menuInputDelete == "2":
        Play()    
    DeleteMenu()

def Play():
    # Execute Data Menu
    print(Menu)

    # Choose function
    pilih = input("Silahkan Pilih Main_Menu [1-5]: ")
    if pilih == "1":
        ReadMenu()
    elif pilih == "2":
        CreateMenu()
    elif pilih == "3":
        UpdateMenu()
    elif pilih == "4":
        DeleteMenu()
    elif pilih == "5":
        print("Thank You and Good Bye!!!")
        exit()
    else: 
        print("Pilihan yang Anda Masukan Salah")

# Running system
Play()
