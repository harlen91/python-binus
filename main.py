import matematika
import nilai

bil1=int(input("Masukkan Bilangan 1 : "))
bil2=int(input("Masukkan Bilangan 2 : "))
hasil=matematika.tambah(bil1,bil2)
print("Hasil Tambah : ",hasil)

tugas=int(input("Nilai tugas Anda: "))
mid=int(input("Nilai Mid : "))
uas=int(input("Nilai UAS : "))
na=nilai.proses(tugas,mid,uas)
ket=nilai.pengumuman(na)
print("Nilai Anda Adalah : ",na)
print("Hasil Nilai: ",ket)