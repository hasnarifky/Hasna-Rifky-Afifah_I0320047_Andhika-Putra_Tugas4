#Operator Logika

print("Pendaftaran kursus online")
print(" ")

print("Masukkan data yang dibutuhkan")
print("Peserta harus menjawab pertanyaan dengan jujur dan mempertanggungjawabkan apapun yang diisikan")

print("Berapa usia peserta saat ini?")
usia = int(input("Usia : "))

if usia >= 21 :
    print("Apakah peserta sudah lulus ujian kualifikasi? (tulis Y/T)")
    kelulusan = input("Kelulusan ujian : ")
    if kelulusan == "Y" :
        print("Anda dapat mendaftar di kursus")
    else :
        print("Anda tidak dapat mendaftar di kursus")
else :
    print("Anda tidak dapat mendaftar di kursus")
