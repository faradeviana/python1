Pertemuan 5 - Latihan
Pada pertemuan 5 bahasa pemograman, saya diberi soal untuk latihan oleh Dosen untuk membuat Aplikasi Biodata dengan python (Seperti gambar di bawah ini:) ![latihan pertemuan 5]

foto 1

Saat ini saya akan menjelaskan hasil dari tugas tersebut.
Berikut source code nya atau klik berikut (latihan 5):

print "  ====================================" 
print "       Latihan 1 Biodata FARA        "
print "  ===================================="

#variabel

nama= raw_input ("Masukan Nama Lengkap Anda: ")
panggilan= raw_input ("Masukan Nama Panggilan: ")
nim= raw_input ("Masukan Nim Anda: ")
ttl= raw_input ("Masukan Tempat Lahir Anda`: ")
tl= input ("Masukan Tanggal lahir  Anda: ")
alamat= raw_input ("Masukan Alamat Anda: ")
telpone= raw_input ("Masukan No Telpon Anda: ")

#hasil inputan dari variable
print "Assalamu'alaikum Wr.Wb"
print "Let me introduce my self My name is",nama,"but you can call me",panggilan,"my NPM is",nim,"I was born in",ttl,"and I am",tl,"years old. I am very glad if you want to invite my house in",alamat,".So, don't forget to call me before with the number",telpone,


Berikut penjelasan :
print("masukan nama lengkap anda : ")
source code fiatas berfungsi untuk mencetak hasil / output berupa " masukan nama lengkap anda : ".
Untuk menampilkan output string, saya menggunakan tanda petik dua didalam fungsi print(), sedangkan jika saya ingin menampilkan output / hasil berupa angka / interger saya tidak perlu menggunakan tanda petik dua. Contohnya:

print("nama lengkap saya adalah ...")
print(696969)
Seperti gambar berikut ini
image

Untuk source code berikutnya adalah inputan atau membuat variable. Seperti syntax dibawah ini:
nama=raw_input()
Keterangan :

Variable adalah sebuah wadah penyimpanan data pada program yang akan digunakan selama program itu berjalan. Yang berfungsi sebagai variable dalam source code diatas adalah NAMA .

Fungsi input() adalah untuk memasukan nilai dar layar console di command prompt, lalu kemudian mengembalikan nilai saat kita menekan tombol enter (newline)

image

Pada gambar diatas, hasil dari inputan tersebut berwarna putih

Untuk memasukan printah lain seperti Nama, NIM, Tempat lahir, Tanggal Lahir, Nomor Telphone, mengikuti perintah yang sama seperti memasukan NAMA

Untuk menghitung rumus umur saya menggunakan variable DOB yaitu 2020 (Tahun sekarang) dikurangi dengan Year of bircth, pada source code berikut :

dob=2020-year
Pada syntax / source code diatas, saya menggunakan variable dob dimana untuk menghitung umur (variable age pada output), yaitu dengan rumus pada variable dob=2020-year

Langkah kali ini saya akan menampilkan output yang diminta oleh Dosen.
Output pertama yang di minta Dosen adalah menampilkan salam, yaitu dengan mengetikkan syntax / source code berikut :
print("\n Asalammu'alaikum Wr.Wb. ")
Keterangan :

Fungsi \n pada source code diatas adalah untuk memberi baris baru / enter / newline
Fungsi print() seperti dijelaskan pada point Output diatas Hasil source code diatas adalah seperti gambar dibawah ini :
image

Langkah terakhir menampilkan semua hasil dari inputan diatas. Dengan mengetikan source code berikut :
print(f"Let me introduce my self. My name is {fullname}, but you can call me {nickname}. My NPM {npm}. I was born in {pob} and Iam {dob} years old. I am very glad if you want to invite my house in {address}. So don't forget to call me before with the number {phone}. \n Thank You ")
Keterangan :

Fungsi huruf f pada perintah print(f"....") adalah fungsi print atau bisa memudahkan program dalam mencetak statement dalam suatu baris dibandingkan dengan metode yang lama yaitu memisahkan string dan variable dengan symbol koma ( , ) atau plus ( + )
Sedangkan fungsi {} pada output tersebut menampilkan hasil variable
Hasil dari output tersebut seperti berikut :
image

Pertemuan 6 - lab 1
Pada halaman ini (Tugas pertemuan 6 - lab 1) Saya di berikan tugas oleh Dosen yaitu mempelajari Operator Aritmatika menggunakan bahasa pemograman python. Berikut source yang di berikan oleh Dosen source lab 1 ![Pertemmuan 6 - lab 1]

fot0 6

#Penggunaan End
print("A", end="")
print("B", end="")
print("C", end="")

print()
print("X")
print("Y")
print("Z")

#Penggunaan Separator
w,x,y,z=10,15,20,25
print(w,x,y,z)
print(w,x,y,z,sep=",")
print(w,x,y,z,sep="")
print(w,x,y,z,sep=":")
print(w,x,y,z,sep="-----")
Oke, kali ini saya menjelaskan materi yang dijelaskan oleh Dosen.


Penggunaan END Penggunaan end digunakan untuk menambahkan kata yang dicetak di akhir baris
print("A", end="")
print("B", end="")
print("C", end="")
Penggunaan print() digunakan untuk mencetak output, seperti syntax dibawah ini :

print()
Syntax dibawah ini digunakan untuk menampilkan output berupa string

print("X")
print("Y")
print("Z")
Hasil dari source code terseut seperti gambar di bawah ini:

Screenshot (78)

Pengertian separaktor Sepaktor adalah pemisah yang berfungsi sebagai tanda pemisah antar objek yang dicetak. Defaultnya adalah tanda sepasi

Pendeklarasian beberapa variable berserta nilainya

w,x,y,z=10,15,20,25
Menampilkan hasil setiap variable tiap-tiap variable

print(w,x,y,z)
Menampilkan hasil variable dari tiap-tiap variable menggunakan pemisah , (koma)

print(w,x,y,z,sep=",")
Menampilkan hasil variable dari tiap-tiap variable tanpa menggunakan pemisah

print(w,x,y,z,sep="")
Menampilkan hasil variable dari tiap-tiap variable dengan menggunakan pemisah : (titik dua)

print(w,x,y,z,sep=":")
Menampilkan hasil variable dari tiap-tiap variable dengan menggunakan pemisah ----

print(w,x,y,z,sep="-----")
Hasil dari syntax / source code diatas adalah seperti berikut iniL:
Output Separator



Pertemuan 6 - lab 1-2
String format
String formatting atau pemformatan string memungkinkan kita menyuntikkan item kedalam string daripada kita mencoba menggabungkan string menggunakan koma atau string concatenation.
Penggunaan pada source yang di berikan Dosen sebagai berikut :
Lab 1-2

# string format 1
print(0, 10 ** 0)
print(1, 10 ** 1)
print(2, 10 ** 2)
print(3, 10 ** 3)
print(4, 10 ** 4)
print(5, 10 ** 5)
print(6, 10 ** 6)
print(7, 10 ** 7)
print(8, 10 ** 8)
print(9, 10 ** 9)
print(10, 10 ** 10)

# string format 2
print('{0:>3}{1:>16})'.format(0, 10 ** 0))
print('{0:>3}{1:>16})'.format(1, 10 ** 1))
print('{0:>3}{1:>16})'.format(2, 10 ** 2))
print('{0:>3}{1:>16})'.format(3, 10 ** 3))
print('{0:>3}{1:>16})'.format(4, 10 ** 4))
print('{0:>3}{1:>16})'.format(5, 10 ** 5))
print('{0:>3}{1:>16})'.format(6, 10 ** 6))
print('{0:>3}{1:>16})'.format(7, 10 ** 7))
print('{0:>3}{1:>16})'.format(8, 10 ** 8))
print('{0:>3}{1:>16})'.format(9, 10 ** 9))
print('{0:>3}{1:>16})'.format(10, 10 ** 10))

Saat ini saya akan menjelaskan satu persatu dari syntax yang diberikan oleh Dosen
1. **String format 1**
Pada syntax / source code string format 1 akan menampilkan output berupa 2 outputan.
Yang pertama (sebelah kiri) akan menampilkan angka urut dari angka 0 hingga 10, sedangkan sebelah kanan akan menampilkan Oprasi Aritmatika Pangkat.
Dengan ketentuan sebagau berikut, oprasi pangkat dengan angka kiri sebagai pokok (Rumus : ** [Bintang dua])
Hasil dari syntax tersebut adalah 10 pangkat 0, hingga 10 pangkat 10. Dengan output sebagai berikut :
Operasi Aritmatika pangkat **


String Format 2

Pada syntax / source code string format 2 akan menampilkan output berupa 2 output'an juga (Seoerti string format 1, yaitu kanan dan kiri)
Dengan ketentuan sebagai berikut :
Alignment, padding, dan precesion dengan .format() dalam kurung kurawal kita dapat menetapkan panjang bidang, rata kanan/kiri, parameter pembulatan dan banyak lagi. Contoh lain seperti berikut :

print('{0:8} | {1:9}'.format('sepatu','Jumlah'))
print('{0:8} | {1:9}'.format('dalas', 3.))
print('{0:8} | {1:9}'.format('NB',10))
Hasil dari source code contoh di atas akan seperti berikut :
OutPut Aligmnent contoh


Secara default, .format() menggunakan rata text kiri, angka ke kanan. <,^, atau > untuk perataan kiri, tengah , atau kanan. Contoh lain dari penggunaan .format() sebagai berikut :

print('{:<30}{:^30}{:>30}'.format('Kiri','Tengah','Kanan'))
print('{:<30}{:^30}{:>30}'.format(12,34,56))
Hasil dari source code contohdiatas akan muncul seperti ini :
Output Alignment

Hasil string format 2 adalah :
Output Alignment contoh 2


Pertemuan 6 - Lab 2
Konversi Nilai Variable Untuk pembahasan terakhir, kali ini akan myenyelesaikan tugas Lab 2 dari Dosen, yaitu Konversi Nilai Variable
Tugas yang di berikan oleh Dosen adalah seperti gambar dibawah ini atau bisa di temukan dengan link berikut : (temukan)
a=int(input("Masukkan Nilai A : "))
b=int(input("Masukkan Nilai B : "))
print("Variable A : ",a)
print("Variable B : ",b)
print("Hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

#Konversi nilai variable
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))

Hasil dari source / code diatas :
Output source diatas

