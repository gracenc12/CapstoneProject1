# Capstone Project 1 - Grace NC

student_list_data = [
    {"id": "001", "nama" : "Abigail Zefanya", "matematika" : 85, "fisika" : 80, "kimia" : 87, "biologi": 90},
    {"id": "002", "nama" : "Bianca Jeanette", "matematika" : 88, "fisika" : 80, "kimia" : 86, "biologi": 83},
    {"id": "003", "nama" : "Clara Limanttan", "matematika" : 80, "fisika" : 85, "kimia" : 87, "biologi": 85},
    {"id": "004", "nama" : "Dammian Angkasa", "matematika" : 90, "fisika" : 80, "kimia" : 84, "biologi": 86}
]

def find_id(student_id):
    '''mencari siswa berdasarkan ID unik'''
    for student in student_list_data:
        if student["id"] == student_id:
            return student
    return None

def add_student(new_student):
    '''menambahkan data siswa'''
    student_list_data.append(new_student)

def edit_student(student, column, new_value):
    '''mengubah data siswa spesifik'''
    student[column] = new_value

def edit_student_all(student, new_values):
    '''mengubah semua data siswa per baris'''
    for keys in student.keys():
        if keys in new_values:
            student[keys] = new_values[keys]
    
def remove_student(student):
    '''menghapus data siswa'''
    student_list_data.remove(student)

# import prettytable untuk format tabel yg lebih rapi
from prettytable import PrettyTable

# Function untuk tabel
def display_table(data, title):
    '''menampilkan data dengan format dan judul table'''
    # error handling jika list kosong
    if not data: 
        print("\nSemua data siswa sudah dihapus. Tidak ada data untuk ditampilkan.")
        return
    
    # memberikan nama judul tabel
    if title:
        print(f"\n {title}\n")

    # jika data berupa dictionary tunggal, ubah ke list
    if type(data) == dict:
        data = [data] 
        
    # membuat list menampung nama kolom untuk header tabel
    headers = []
    for key in data[0].keys():
        if key.lower() == "id":
            headers.append("id")
        else:
            headers.append(key.title())

    table = PrettyTable()
    table.field_names = headers

    # menambahkan tiap baris list data siswa ke dalam tabel
    for row in data:
        table.add_row([row.get(i, "") for i in data[0].keys()])
    
    print(table)

# Validasi data ID siswa
def id_validation(text):
    '''validasi ID unik siswa'''
    while True:
        student_id = input(text).lower()

        if student_id == "kembali":
            return None

        # validasi panjang ID
        if len(student_id) != 3:
            print("Jumlah ID harus 3 digit. (contoh: 005)")
            continue
        
        # cek ID dan jika bukan digit, minta agar angka
        if not student_id.strip().isdigit():
            print("ID tidak valid. Harus 3 digit angka.")

        # cek sudah ada atau belum
        if find_id(student_id):  
            print("ID sudah ada. Silakan masukkan ID lain.")
            continue
        return student_id

# Validasi data nama siswa
def name_validation(text):
    '''validasi nama siswa'''
    while True:
        student_name = input(text)
        if student_name.replace(" ","").isalpha(): #menghapus spasi dan cek apakah nama sudah dalam bentuk huruf
            return student_name.title()
        else:
            print("Nama harus huruf. Silakan masukkan kembali nama siswa.")

# Validasi data nilai siswa
def score_validation(text):
    '''validasi nilai hanya angka dan hanya dalam rentang 0 - 100'''
    while True:
        try:
            score = int(input(text))
            if 0 <= score <= 100:
                return score
            else:
                print("Masukkan nilai dalam rentang 0–100! ")
        except:
            print("Input tidak valid. Masukkan angka.")

def display_all_data():
    '''Menu menampilkan semua data siswa'''
    display_table(student_list_data, title = "Data Nilai Siswa")
    
def display_spesific_data():
    '''Menu menampilkan data siswa tertentu'''
    while True:
        student_id = input("Masukkan ID siswa yang ingin ditampilkan atau 'kembali' untuk kembali: ").lower() 
        if student_id == "kembali":  
            return
        student = find_id(student_id)
        if student:
            display_table(student, title="Data Nilai Siswa")
        else:
            print("Data yang dicari tidak ditemukan. Silakan coba kembali. ")

def create_data():
    '''Menu menambahkan data siswa'''
    print("\nMenu Tambah Data")
    while True:
        new_student_id = id_validation("Masukkan ID siswa baru (contoh: 004) atau 'kembali' untuk kembali: ")
        if new_student_id is None:
            return
        
        name = name_validation("Masukkan nama siswa: ")
        math = score_validation("Masukkan nilai Matematika: ")
        physics = score_validation("Masukkan nilai Fisika: ")
        chemistry = score_validation("Masukkan nilai Kimia: ")
        biology = score_validation("Masukkan nilai Biologi: ")

        while True:
            confirmation = input("Apakah ingin menambahkan data siswa? (Yes/No): ").lower()
            if confirmation == "yes":
                new_student = {
                "id" : new_student_id,
                "nama" : name,
                "matematika" : math,
                "fisika" : physics,
                "kimia" : chemistry,
                "biologi" : biology,
                }
                add_student(new_student)
                print("Data berhasil ditambahkan.")
                display_all_data()
                return
            elif confirmation == 'no':
                print("Penambahan data dibatalkan.")
                return
            else:
                print("Input tidak valid. Silakan masukkan 'Yes' atau 'No'.")

def update_spesific_data():
    '''Mengubah data siswa'''
    print("\nMenu Ubah Data")

    while True:
        student_id = input("Masukkan ID siswa yang ingin di update (contoh: 004) atau 'kembali' untuk kembali: ").lower()
        if student_id == "kembali":
            return None 
        
        student = find_id(student_id)
        if not student:
            print("Data yang dicari tidak ditemukan, coba kembali.")
            continue
        
        if student:
            print("Data ditemukan")
            display_table(student, title = "Data Nilai Siswa")
        
        
        confirmation = input("Apakah ingin mengubah data siswa tersebut? (Yes/No): ").lower()
        if confirmation == "no":
            print("Perubahan data dibatalkan.")
            return
            
        if confirmation == "yes":
            column = input("Masukkan kolom yang ingin diubah (Nama/Matematika/Fisika/Kimia/Biologi) atau 'batal' untuk batal: ").lower()
            if column == "batal":
                return None
            if column == "nama":
                new_value = name_validation("Masukkan nama siswa baru: ")
            else:
                new_value = score_validation("Masukkan nilai siswa: ")

        while True:
            confirmation_to_update = input("Apakah yakin ingin mengubah data siswa tersebut? (Yes/No): ").lower()
            if confirmation_to_update == "yes":
                edit_student(student, column, new_value)
                display_all_data()
                print("Data berhasil diubah.")
        
                return
            elif confirmation_to_update == "no":
                print("Perubahan data dibatalkan.")
                return
            else:
                print("Input tidak valid. Silakan masukkan Yes atau No.")

def update_row_data():
    '''Mengubah data siswa'''
    print("\nMenu Ubah Data")

    while True:
        student_id = input("Masukkan ID siswa yang ingin di update (contoh: 004) atau 'kembali' untuk kembali: ").lower()
        if student_id == "kembali":
            return None 
        
        student = find_id(student_id)
        if not student:
            print("Data yang dicari tidak ditemukan, coba kembali.")
            continue
        
        if student:
            print("Data ditemukan")
            display_table(student, title = "Data Nilai Siswa")
        
        confirmation = input("Apakah ingin mengubah data siswa tersebut? (Yes/No): ").lower()
        if confirmation == "no":
            print("Perubahan data dibatalkan.")
            return
            
        if confirmation  == "yes":
            new_values = {
                "nama": name_validation("Masukkan nama siswa: "),
                "matematika": score_validation("Masukkan nilai Matematika: "),
                "fisika": score_validation("Masukkan nilai Fisika: "),
                "kimia": score_validation("Masukkan nilai Kimia: "),
                "biologi": score_validation("Masukkan nilai Biologi: ")
            }

            while True:
                confirmation_to_update = input("Apakah yakin ingin mengubah data siswa tersebut? (Yes/No): ").lower()
                if confirmation_to_update == "yes":
                    edit_student_all(student, new_values)
                    print("Data berhasil diubah.")
                    display_all_data()
                    return
                elif confirmation_to_update == "no":
                    print("Perubahan data dibatalkan.")
                    return
                else:
                    print("Input tidak valid. Silakan masukkan Yes atau No.")
        else:
            print("Input tidak valid. Masukkan input yang sesuai.")

def delete_specific_data():
    '''Menu delete data siswa tertentu'''
    if not student_list_data:
        print("Tidak ada data siswa untuk dihapus.")
        return
    
    while True:
        student_id = input("Masukkan ID siswa yang ingin dihapus (contoh: 004) atau 'kembali' untuk kembali: ").lower()
        if student_id == "kembali":
            return None
        
        student = find_id(student_id)
        if not student:
            print("Data tidak ditemukan, silakan masukkan ID kembali.")

        if student:
            print("Data Ditemukan")
            display_table(student, title = "Data Nilai Siswa")

            confirmation = input("Apakah yakin ingin menghapus data siswa ini? (Yes/No): ").lower()
            if confirmation == "yes":
                for i in student_list_data:
                    if i["id"] == student_id: 
                        student_list_data.remove(student)
                        print("Data berhasil di hapus")
                        display_all_data()
                        return
                    
            if confirmation == "no":
                print("Penghapusan data siswa dibatalkan.")
                display_all_data()
            else:
                print("Input tidak valid. Silakan masukkan Yes atau No.")

def delete_all_data():
    '''Menu delete semua data siswa'''
    if not student_list_data:
        print("Tidak ada data siswa untuk dihapus.")
        return

    while True:
        confirmation = input("Apakah yakin ingin menghapus semua data siswa? (Yes/No) atau 'kembali' untuk kembali: ").lower()
        if confirmation == "kembali":
            return None
        if confirmation == "yes":
            student_list_data.clear()
            print("Semua data siswa berhasil dihapus")
            return
        if confirmation == "no":
            print("Penghapusan semua data dibatalkan.")
        else:
            print("Input tidak valid. Silakan masukkan Yes atau No.")

def read_data():
    '''Menu read untuk fitur Read Data'''
    while True:
        print("\nMenu Read")
        print("1. Tampilkan semua data siswa")
        print("2. Tampilkan data siswa berdasarkan ID siswa")
        print("3. Kembali ke menu utama")
        
        choice = input("Masukkan pilihan 1/2/3 : ")
        if choice == "1":
            display_all_data()
        elif choice == "2":
            display_spesific_data()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Masukkan pilihan 1/2/3 saja.")

def update_data():
    '''Menu read untuk fitur Read Data'''
    while True:
        print("\nMenu Update")
        print("1. Ubah data siswa spesifik berdasarkan ID siswa")
        print("2. Ubah semua data siswa berdasarkan ID siswa")
        print("3. Kembali ke menu utama")
        
        choice = input("Masukkan pilihan 1/2/3 : ")
        if choice == "1":
            update_spesific_data()
        elif choice == "2":
            update_row_data()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Masukkan pilihan 1/2/3 saja.")

def delete_data():
    '''Menu delete untuk fitur Delete Data'''
    while True:
        print("\nMenu Delete")
        print("1. Menghapus data berdasarkan ID siswa")
        print("2. Menghapus semua data siswa")
        print("3. Kembali ke menu utama")

        choice = input("Masukkan pilihan 1/2/3 : ")
        if choice == "1":
            delete_specific_data()
        elif choice == "2":
            delete_all_data()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Masukkan pilihan 1/2/3 saja.")

def main():
    '''Main program untuk semua fitur'''
    while True:
        print("\nCapstone Project Module 1 - CRUD")
        print("Manajemen Data Nilai Siswa")
        print("\nMenu Utama")
        print("1. Menu Read Data")
        print("2. Menu Create Data")
        print("3. Menu Update Data")
        print("4. Menu Delete Data")
        print("5. Exit Program")

        choice = input("Masukkan pilihan menu: ")
        if choice == "1":
            read_data()
        elif choice == "2":
            create_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            print("Exit Program. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Masukkan pilihan 1-5 saja.")

if __name__ == "__main__":
    main()