#Operator Relasional

print("Pemeriksaan berat bagasi")
batas_maksimum = 50 * 0.4536
print("Ketentuan: batas maksimum berat bagasi yaitu", batas_maksimum, "kg")

benda1 = 110
benda2 = 49

ketentuan1 = benda1 <= batas_maksimum
ketentuan2 = benda2 <= batas_maksimum

print("Benda 1 memiliki berat", benda1, "kg sehingga benda 1 masuk kategori", ketentuan1)
print("Benda 2 memiliki berat", benda2, "kg sehingga benda 2 masuk kategori", ketentuan2)
