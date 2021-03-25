#Memperbaiki kode dengan mengubah string

s = "Strings are awesome!"

#Panjang string
print("panjang dari s = %d" % len(s))

#index pertama huruf 'a'
print("Kemunculan pertama a = %d" % s.index("a"))

#jumlah huruf a
print("a muncul sebanyak %d kali" % s.count("a"))

#memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" % s[:5])
print("Lima karakter berikutnya adalah '%s'" % s[5:10])
print("Karakter ketiga belas adalah '%s'" % s[12])
print("Karketer dengan indeks ganjil adalah '%s'" %s[1::2])
print("Lima karakter terakhir adalah '%s'" % s[-5:])

#konversikan ke uppercase
print("String dalam huruf besar: %s" % s.upper())

#konversikan ke lowercase
print("String dalam huruf kecil: %s" % s.lower())

#cek bagaimana string itu dimulai
if s.startswith("Str"):
    print("String dimulai dengan 'Str'. Good!")

#cek bagaimana string itu diakhiri
if s.endswith("ome!"):
    print("String diakhiri dengan 'ome!'. Good!")

#Pisahkan string menjadi tiga string,
#masing-masing hanya berisi satu kata
print("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))
