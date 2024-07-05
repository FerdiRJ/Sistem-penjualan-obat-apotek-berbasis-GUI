# Projek Aplikasi Apotek Kelompok Strawberry Sains Data 2022B
# Nama Anggota Kelompok:
# 1. Daffa Fazly Rashidan (22031554006)
# 2. Ferdiansyah Rizki Junianto (22031554050)
# 3. Siti Aida Hanun (22031554044)
# 4. Selvy Aulia Ramadhan (22031554004)

import os 
os.system('cls')
from tkinter import *
import pandas as pd
import datetime
from tkinter.messagebox import showinfo
import tempfile






apot=Tk()
apot.title('Apotek')
apot.geometry('1540x850+0+0')
apot.configure(bg="#fff")
apot.resizable(True, True)


"""=======================================Input Nama=============================="""
nama_var=StringVar()
umur_var=StringVar()
resep_var=StringVar()
keluhan_var=StringVar()
nama2_var=StringVar()
umur2_var=StringVar()
"""=======================================Input Nama=============================="""


"""=======================================Lamaninput data pasien=============================="""
img1=PhotoImage(file='logoapotk.png')
Label(apot, image=img1, bg='white').place(x=50, y=50)

frem=Frame(apot, width=500, height=700, bg="white")
frem.place(x=780, y=70)

heading=Label(frem, text="Data Pembeli", fg='#ff007f', bg='white', font=('Times New Roman', 50, 'bold'))
heading.place(x=100, y=50)

def on_enter(e):
    nama.delete(0, 'end')
def on_leave(e):
    name=nama.get()
    if name=='':
        nama.insert(0, 'Nama')

def on_enter2(e):
    umur.delete(0, 'end')
def on_leave2(e):
    usia=umur.get()
    if usia=='':
        umur.insert(0, 'Usia')


def test():
    namae=nama_var.get()
    umure=umur_var.get()
    

    if namae=='Nama':
        Label(frem, text='                      Silahkan Masukan Nama dan Umur dengan Valid!                                        ',fg='red', bg='white').place(x=70, y=420)
        return namae
    else:
        Label(frem, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Untuk Memilih Keluhan',fg='blue', bg='white').place(x=70, y=420)
    if namae=='':
        Label(frem, text='                      Silahkan Masukan Nama dan Umur dengan Valid!                                        ',fg='red', bg='white').place(x=70, y=420)
        return namae
    else:
        Label(frem, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Untuk Memilih Keluhan',fg='blue', bg='white').place(x=70, y=420)

    if umure=='':
        Label(frem, text='                      Silahkan Masukan Nama dan Umur dengan Valid!                                        ',fg='red', bg='white').place(x=70, y=420)
        return umure
    else:
        Label(frem, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Untuk Memilih Keluhan',fg='blue', bg='white').place(x=70, y=420)

    if umure=='Usia':
        Label(frem, text='                      Silahkan Masukan Nama dan Umur dengan Valid!                                        ',fg='red', bg='white').place(x=70, y=420)
        return umure
    elif umure=='':
        Label(frem, text='                      Silahkan Masukan Nama dan Umur dengan Valid!                                        ',fg='red', bg='white').place(x=70, y=420)
    
    else:
        Label(frem, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Untuk Memilih Keluhan',fg='blue', bg='white').place(x=70, y=420)
        Button(frem, width=30,pady=6, text="Selanjutnya", font=('times new roman', 20, 'bold'),bg='blue', fg='white', border=0, command=keluhan).place(x=35, y=510)


nama=Entry(frem, width=50, fg='black', bg='white', textvariable=nama_var, font=('Microsoft YaHei UI Light', 30))
nama.place(x=30, y=200)
nama.insert(0, 'Nama')
nama.bind('<FocusIn>', on_enter)
nama.bind('<FocusOut>', on_leave)
Frame(frem, width=590, height=2, bg='black').place(x=20, y=265)

umur=Entry(frem, width=50, fg='black', bg='white', textvariable=umur_var, font=('Microsoft YaHei UI Light', 30))
umur.place(x=30, y=310)
umur.insert(0, 'Usia')
umur.bind('<FocusIn>', on_enter2)
umur.bind('<FocusOut>', on_leave2)
Frame(frem, width=590, height=2, bg='black').place(x=20, y=375)


"""=======================================Batas Laman Input data Pasien=============================="""



"""=======================================Codingan Gambar=============================="""
#gambarkeluhan
imgbatuk=PhotoImage(file='watok.png')
imgsakitkepala=PhotoImage(file='ndas.png')
imgsakitgigi=PhotoImage(file='sgigi.png')
imgsotot=PhotoImage(file='sotot.png')
imgssendi=PhotoImage(file='ssendi.png')
imgnapas=PhotoImage(file='snapas.png')
imgkulit=PhotoImage(file='kulid.png')
imgdiabet=PhotoImage(file='sdiabet (2).png')
imgsmata=PhotoImage(file='smata.png')
imgperut=PhotoImage(file='sperut.png')
imgdarah=PhotoImage(file='sdarah.png')
imgsaraf=PhotoImage(file='ssaraf.png')
imgsdalam=PhotoImage(file='sdalam.png')
imgresep=PhotoImage(file='resepdokter.png')
imgskelamin=PhotoImage(file='skelamin.png')

#gambarsakit kepala
imgsinus=PhotoImage(file='sinus.png')
imgvertigo=PhotoImage(file='vertigo.png')
imghipertensi=PhotoImage(file='hipertensi.png')
imgmigren=PhotoImage(file='migren.png')
imgpusing=PhotoImage(file='pusing.png')

#gambarbackground
imgbekgron=PhotoImage(file='bgrnbrkel.png')
imgbekgron2=PhotoImage(file='bgrnbrkel2.png')
imgbekgron3=PhotoImage(file='bgrone.png')
"""=======================================Batas codingan gambar=============================="""

datetime_object = datetime.datetime.now()



"""=======================================Codingan "Selesai"=============================="""
def home():

    

    frem=Frame(apot, width=1525, height=1500, bg="white")
    frem.place(x=1, y=1)
    gmbr=Label(frem, image=img1, bg='white').place(x=50, y=50)
    heading=Label(frem, text="Data Pembeli", fg='#ff007f', bg='white', font=('Times New Roman', 50, 'bold'))
    heading.place(x=800, y=170)

    def on_enter(e):
        nama2.delete(0, 'end')
    def on_leave(e):
        name=nama2.get()
        if name=='':
            nama2.insert(0, 'Nama')

    def on_enter2(e):
        umur2.delete(0, 'end')
    def on_leave2(e):
        usia=umur2.get()
        if usia=='':
            umur2.insert(0, 'Usia')
    

    def test():
        namae=nama2.get()
        umure=umur_var.get()
    
        if namae=='':
            Label(frem, text='                      Silahkan Masukan Nama dan Umur dengan Valid!                                        ',fg='red', bg='white').place(x=790, y=510)
            return namae
        else:
            Label(frem, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Untuk Memilih Keluhan',fg='blue', bg='white').place(x=790, y=510)

        if namae=='Nama':
            Label(frem, text='                      Silahkan Masukan Nama dan Umur dengan Valid!                                        ',fg='red', bg='white').place(x=790, y=510)
            return namae
        else:
            Label(frem, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Untuk Memilih Keluhan',fg='blue', bg='white').place(x=790, y=510)

        if umure=='':
            Label(frem, text='                      Silahkan Masukan Nama dan Umur dengan Valid!                                        ',fg='red', bg='white').place(x=790, y=510)
            return umure
        else:
            Label(frem, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Untuk Memilih Keluhan',fg='blue', bg='white').place(x=790, y=510)

        if umure=='Usia':
            Label(frem, text='                      Silahkan Masukan Nama dan Umur dengan Valid!                                        ',fg='red', bg='white').place(x=790, y=510)
            return umure
    
        else:
            Label(frem, text='Data Yang Anda Masukan Valid, Silahkan Melanjutkan Untuk Memilih Keluhan',fg='blue', bg='white').place(x=790, y=510)
            Button(frem, width=35,pady=6, text="Selanjutnya", font=('times new roman', 20, 'bold'),bg='blue', fg='white', border=0, command=keluhan).place(x=720, y=590)


    nama2=Entry(frem, width=25, fg='black', bg='white', textvariable=nama_var, font=('Microsoft YaHei UI Light', 30))
    nama2.place(x=730, y=300)
    nama2.insert(0, '')
    nama2.bind('<FocusIn>', on_enter)
    nama2.bind('<FocusOut>', on_leave)
    Frame(frem, width=550, height=2, bg='black').place(x=720, y=365)

    umur2=Entry(frem, width=25, fg='black', bg='white', textvariable=umur_var, font=('Microsoft YaHei UI Light', 30))
    umur2.place(x=730, y=410)
    umur2.insert(0, '')
    umur2.bind('<FocusIn>', on_enter2)
    umur2.bind('<FocusOut>', on_leave2)
    Frame(frem, width=550, height=2, bg='black').place(x=720, y=475)

    btn=Button(frem, width=50,pady=6, text="Check", font=('times new roman', 10, 'bold'),bg='#ff007f', fg='white', border=0, command=test).place(x=820, y=530)
"""=======================================Batas Codingan "Selesai"=============================="""



"""=======================================Codingan Keluhan (setelah click button Selanjutnya)======================================"""
def keluhan():


    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    
    bekgron=Label(frem2, image=imgbekgron)
    bekgron.place(x=0, y=5)
    heading2=Label(frem2, text="Keluhan", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 60, "bold"), padx=550, pady=4)
    
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    heading2.place(x=40, y=1)

    
    #linekeluhan1
    btnbatuk=Button(frem2, image=imgbatuk, bd=15, relief=RAISED, padx=1, pady=1, command=batuk).place(x=70, y=190)
    btnsktkpla=Button(frem2, image=imgsakitkepala,bd=15, relief=RAISED, padx=1, pady=1, command=skepala).place(x=470, y=190)
    btngigi=Button(frem2, image=imgsakitgigi, bd=15, relief=RAISED, padx=1, pady=1, command=sgigi).place(x=860, y=190)
    btnkulit=Button(frem2, image=imgkulit, bd=15, relief=RAISED, padx=1, pady=1,command=skulit).place(x=1240, y=190)
    #linekeluhan2
    btnsendi=Button(frem2, image=imgssendi, bd=15, relief=RAISED, padx=1, pady=1, command=sendi).place(x=70, y=450)
    btnotot=Button(frem2,image=imgsotot, bd=15, relief=RAISED, padx=1, pady=1, command=sotot).place(x=470, y=450)
    btnpernapasan=Button(frem2, image=imgnapas, bd=15, relief=RAISED, padx=1, pady=1, command=pernapasan).place(x=860, y=450)
    btndiabet=Button(frem2, image=imgdiabet, bd=15, relief=RAISED, padx=1, pady=1, command=sdiabetes).place(x=1240, y=450)
    btnselanjutnya2=Button(frem2, width=10, pady=10, text=">", bg='green', font=('aria', 20, 'bold'), border=0, command=keluhan2).place(x=1302, y=700)

#========================================================================================================
btn=Button(frem, width=50,pady=6, text="Check", font=('times new roman', 10, 'bold'),bg='#ff007f', fg='white', border=0, command=test).place(x=95, y=450)

#========================================================================================================

def keluhan2():


    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron)
    bekgron.place(x=0, y=5)
    heading2=Label(frem2, text="Keluhan", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 60, "bold"), padx=550, pady=4)
    heading2.place(x=40, y=1)
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    #linekeluhan1
    btnbatuk=Button(frem2, image=imgskelamin, bd=15, relief=RAISED, padx=1, pady=1, command=skelamin).place(x=70, y=190)
    btnsktkpla=Button(frem2, image=imgperut,bd=15, relief=RAISED, padx=1, pady=1, command=pencernaan).place(x=470, y=190)
    btngigi=Button(frem2, image=imgdarah, bd=15, relief=RAISED, padx=1, pady=1, command=sdarah).place(x=860, y=190)
    btnkulit=Button(frem2, image=imgsmata, bd=15, relief=RAISED, padx=1, pady=1,command=smata).place(x=1240, y=190)
    #linekeluhan2
    btnotot=Button(frem2,image=imgsaraf, bd=15, relief=RAISED, padx=1, pady=1, command=ssaraf).place(x=470, y=450)
    btnpernapasan=Button(frem2, image=imgsdalam, bd=15, relief=RAISED, padx=1, pady=1, command=sdalam).place(x=860, y=450)
    btnselanjutnya2=Button(frem2, width=10, pady=10, text=">", bg='green', font=('aria', 20, 'bold'), border=0, command=keluhan3).place(x=1302, y=700)
    btnsebelum=Button(frem2, width=10, pady=10, text="<",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan).place(x=85, y=700)
def keluhan3():


    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Keluhan", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 60, "bold"), padx=550, pady=4)
    heading2.place(x=40, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    #linekeluhan1
    #linekeluhan1
    btnresep=Button(frem2, image=imgresep, bd=15, relief=RAISED, padx=1, pady=1, command=resepdok2).place(x=650, y=300)
    btnsebelum=Button(frem2, width=10, pady=10, text="<",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan2).place(x=85, y=700)
"""==================================akhir Codingan Keluhan (setelah click button Selanjutnya)======================================"""




"""=======================================Codingan Resepdokter (setelah click button Resep Dokter)======================================"""
def resepdok2():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Masukan Keluhan dan Resep Dokter", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=315, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='white', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=700, y=590)

    def on_enter(e):
        inputkeluhan.delete(0, 'end')
    def on_leave(e):
        kel=inputkeluhan.get()
        if kel=='':
            inputkeluhan.insert(0, 'Keluhan')

    def on_enter2(e):
        resepdok.delete(0, 'end')
    def on_leave2(e):
        resep=resepdok.get()
        if resep=='':
            resepdok.insert(0, 'Resep Dokter')

    inputkeluhan=Entry(frem2, width=40, fg='black', bg='white', textvariable=keluhan_var, font=('Microsoft YaHei UI Light', 30))
    inputkeluhan.place(x=340, y=280)
    inputkeluhan.insert(0, 'Keluhan')
    inputkeluhan.bind('<FocusIn>', on_enter)
    inputkeluhan.bind('<FocusOut>', on_leave)



    resepdok=Entry(frem2, width=40, fg='black', bg='white', textvariable=resep_var, font=('Microsoft YaHei UI Light', 30))
    resepdok.place(x=340, y=450)
    resepdok.insert(0, 'Resep Dokter')
    resepdok.bind('<FocusIn>', on_enter2)
    resepdok.bind('<FocusOut>', on_leave2)
    
    Frame(frem2, width=500, height=2, bg='black').place(x=340, y=345)
    Frame(frem2, width=500, height=2, bg='black').place(x=340, y=515)
    buttonkirim=Button(frem2, width=10, pady=10, text="Kirim", font=("times new roman", 30, "bold"), bg='#ff007f', fg='white', border=0, command=resdok).place(x=690, y=700)
"""=================================akhiran=Codingan Resepdokter (setelah click button Resep Dokter)======================================"""



"""===================Codingan Akhir Resepdokter (setelah click button Kirim Pada resepdokter)============================"""
def resdok():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=356, pady=8)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN============= \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : {keluhan_var.get()}'
    msgs3=f'Resep Dokter: {resep_var.get()}\n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()
    resepe=resep_var.get()
    keluhannya=keluhan_var.get()
    datetime_object = datetime.datetime.now()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': [keluhannya],
    'Obat Yang Dibeli': [resepe]

    
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Harga di Kasir', msgs + "\n" + msgs2 + "\n" + msgs3)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2+'\n'+msgs3)).place(x=605, y=350)
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

"""===============Batas Codingan Akhir Resepdokter (setelah click button Kirim Pada resepdokter)============================"""

    





"""===================Codingan Batuk (setelah click button Batuk[keluhan])============================"""
def batuk():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnbatuk2=Button(frem2, width=20, text="Batuk Berdahak", font=("times new roman", 30, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatbtkdahak).place(x=200, y=250)
    btnbatuk3=Button(frem2, width=20, text="Batuk Tidak Berdahak", font=("times new roman", 30, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=batuktdkberdahak).place(x=850, y=250)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan).place(x=85, y=700)


"""===================Codingan Batuktidak berdahak (setelah click button Batuk tdk berdahak [Batuk])============================"""
def batuktdkberdahak():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)
    heading2=Label(frem2, text="Rekomendasi Obat Batuk Tidak Berdahak", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=315, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnbatuksirup1=Button(frem2, width=30, pady=30, text="Siladex Antitussive 60ml\n\nHarga: Rp16.000/Botol",font=("times new roman", 25, "bold"),bg='blue', fg='white', border=0, command=siladex).place(x=130, y=250)
    btnbatuktablet1=Button(frem2, width=30, pady=30, text="Konidin\n\nHarga: Rp3.000/4 Tablet",font=("times new roman", 25, "bold"),bg='blue', fg='white', border=0, command=obatobh).place(x=850, y=250)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=batuk).place(x=85, y=700)


"""===================Codingan Batuk Berdahak (setelah click button Batuk berdahak [Batuk])============================"""
def obatbtkdahak():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Batuk Berdahak", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=315, pady=4)
    heading2.place(x=10, y=1)
   
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnbatuksirup1=Button(frem2, width=30, pady=30, text="OBH Combi Batuk Berdahak \nHarga: Rp15.000/Botol", font=("times new roman", 25, "bold"),bg='green', fg='white', border=0, command=obatobh).place(x=130, y=250)
    btnbatuksirup2=Button(frem2, width=30, pady=30, text="Prospan Cough Syrup \nHarga: Rp92.000/Botol", font=("times new roman", 25, "bold"),bg='green', fg='white', border=0, command=prospan).place(x=850, y=250)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=batuk).place(x=85, y=700)


"""===================Codingan obat Batuk tidak berdahak (setelah click button batuktdkberdahak[batuk])============================"""
def siladex():
    
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}'
    msgs2 = f'Keluhan : Batuk Tidak Berdahak \nObat: Siladex batuk pilek \nHarga: Rp16.000/Botol (60ml)\n======================================'

    """===================Codingan operation file============"""
    namanye=nama_var.get()
    umoer=umur_var.get()
    datetime_object = datetime.datetime.now()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Batuk Tidak Berdahak'],
    'Obat Yang Dibeli': ['siladex'],
    'Harga':['Rp16.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False )
    """===================akhir Codingan operation file============"""

    showinfo('Struk', msgs + "\n" + msgs2)
    
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+msgs2)).place(x=605, y=350)

    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

"""===================Codingan obat Batuk tidak berdahak (setelah click button batuktdkberdahak[batuk])============================"""
def konidin():

    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Batuk Tidak Berdahak \nObat: Konidin \nHarga: Rp3.000/4 Tablet \n======================================'

    """===================Codingan operation file============"""
    namanye=nama_var.get()
    umoer=umur_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Batuk Tidak Berdahak'],
    'Obat Yang Dibeli': ['Konidin'],
    'Harga':['Rp3.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    """===================akhir Codingan operation file============"""

    showinfo('Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


"""===================Codingan obat Batuk berdahak (OBH) (setelah click button batukberdahak[batuk])============================"""
def obatobh():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Batuk Berdahak \nObat: OBH Combi Batuk Berdahak \nHarga: Rp15.000/Botol \n======================================'

    """===================akhir Codingan operation file============"""
    namanye=nama_var.get()
    umoer=umur_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Batuk Berdahak'],
    'Obat Yang Dibeli': ['OBH Combi'],
    'Harga':['Rp15.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    """===================akhir Codingan operation file============"""

    showinfo('Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

"""===================Codingan obat Batuk  berdahak (setelah click button batukberdahak[batuk])============================"""
def prospan():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Batuk Berdahak \nObat: Prospan Cough Syrup \nHarga: Rp92.000/Botol \n======================================'

    """===================Codingan operation file============"""
    namanye=nama_var.get()
    umoer=umur_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Batuk Berdahak'],
    'Obat Yang Dibeli': ['Prospan Cough'],
    'Harga':['Rp92.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    """===================akhir Codingan operation file============"""

    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)




"""==================================CODINGAN SAKIT KEPALA================================"""
def skepala():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnskepala1=Button(frem2, image=imgsinus, bg="#FFF0F5",relief=RAISED, padx=1, pady=1, command=sinus).place(x=250, y=180)
    btnskepala2=Button(frem2, image=imghipertensi, bg="#FFF0F5", relief=RAISED, padx=1, pady=1, command=hipertensi).place(x=950, y=180)
    btnskepala3=Button(frem2, image=imgmigren, bg="#FFF0F5", relief=RAISED, padx=1, pady=1,command=migren).place(x=250, y=480)
    btnskepala4=Button(frem2, image=imgvertigo, bg="#FFF0F5", relief=RAISED, padx=1, pady=1,command=vertigo).place(x=950, y=480)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan).place(x=85, y=700)
    btnselanjutnya2=Button(frem2, width=10, pady=10, text=">", bg='green', font=('aria', 20, 'bold'), fg='white', border=0, command=skepala2).place(x=1302, y=700)
def skepala2():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)


    btnskepala1=Button(frem2, image=imgpusing, bg="#FFF0F5",relief=RAISED, padx=1, pady=1, command=pusing).place(x=200, y=280)

    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skepala).place(x=85, y=700)

def vertigo():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnobatvertigo1=Button(frem2, width=40, pady=30, text="Promethazine \n\nobat antihistamin \nuntuk mengobati rasa mual dan muntah \nterkait dengan kondisi tertentu \nmisal setelah operasi atau vertigo \n\nRp270.000/ 1 pcs \n*Wajib resep dokter" , font=("times new roman", 20, "bold"),bg='red', fg='white', border=0, command=resepdokPromethazine).place(x=70, y=200)
    btnobatvertigo2=Button(frem2, width=40, pady=30, text="Diphenhydramine \n\nObat ini bekerja dengan \nmemblokir efek bahan kimia tertentu (histamin) \npenyebab mual dan muntah akibat vertigo \n\nRp30.000/ 1 pcs", bg='red', font=("times new roman", 20, "bold"), fg='white', border=0, command=Diphenhydramine).place(x=760, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skepala).place(x=85, y=700)

#obatvertigo
def Promethazine():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN============= \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Vertigo \nObat: Promethazine \nHarga: Rp270.000/ 1 pcs \n'
    msgs3=f'Resep Dokter: {resep_var.get()}\n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    resepe=resep_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Vertigo'],
    'Obat Yang Dibeli': ['Promethazine'],
    'Resep': [resepe]
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2 + "\n" + msgs3)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2+'\n'+msgs3)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def Diphenhydramine():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Vertigo \nObat: Diphenhydramine \nRp30.000/ 1 pcs \n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
   
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Vertigo'],
    'Obat Yang Dibeli': ['Diphenhydramine'],
    'Harga':['Rp30.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def resepdokPromethazine():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Masukan Resep Dokter", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=415, pady=4)
    heading2.place(x=10, y=1)
   
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='white', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=700, y=590)

    def on_enter3(e):
        resepdok.delete(0, 'end')
    def on_leave3(e):
        resep=resepdok.get()
        if resep=='':
            resepdok.insert(0, 'Resep Dokter')

    resepdok=Entry(frem2, width=40, fg='black', bg='white', textvariable=resep_var, font=('Microsoft YaHei UI Light', 30))
    resepdok.place(x=340, y=350)
    resepdok.insert(0, 'Resep Dokter')
    resepdok.bind('<FocusIn>', on_enter3)
    resepdok.bind('<FocusOut>', on_leave3)
    Frame(frem2, width=295, height=2, bg='black').place(x=280, y=128)
    buttonkirim=Button(frem2, width=10, pady=10, text="Kirim", font=("times new roman", 30, "bold"), bg='#ff007f', fg='white', border=0, command=Promethazine).place(x=690, y=700)

def migren():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Migren", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnobtmigren1=Button(frem2, width=40, pady=30, text="paracetamol \n\nmeredakan peradangan, demam, dan \nnyeri, termasuk sakit kepala \nefektif digunakan untuk mengobati sakit \nkepala tegang dan migren \n\nRp20.000/ 1 pcs",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=paracetamol).place(x=70, y=200)
    btnobtmigren2=Button(frem2, width=40, pady=30, text="ibuprofen \n\nobat yang dapat meredakan peradangan, demam, dan \nnyeri, termasuk sakit kepala \nefektif digunakan untuk mengobati \nsakit kepala ringan \n\nRp28.000/ 1 pcs", bg='red', fg='white',font=("times new roman", 20, "bold"), border=0, command=ibuprofenmigren).place(x=750, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skepala).place(x=85, y=700)

#obatmigren
def paracetamol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN============= \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Migren \nObat: paracetamol \nHarga: Rp20.000/ 1 pcs \n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Migren'],
    'Obat Yang Dibeli': ['Paracetamol'],
    'Harga':['Rp20.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def ibuprofenmigren():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN============= \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Migren \nObat: Ibuprofen \nnHarga: Rp28.000/ 1 pcs \n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Migren'],
    'Obat Yang Dibeli': ['Ibuprofen'],
    'Harga':['Rp28.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


def sinus():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Sinus", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnobtsinus1=Button(frem2, width=45, pady=30, text="Kortikosteroid \n\nefektif mengurangi peradangan dan pembengkakan di sinus. \nSelain itu, kortikosteroid mampu mengecilkan polip \nhidung yang sering kali menjadi penyebab sinusitis \n\nRp30.000/ 1 pcs \n*Wajib resep dokter", font=("times new roman", 20, "bold"),bg='red', fg='white', border=0, command=resepdokk2).place(x=60, y=200)
    btnobtsinus2=Button(frem2, width=40, pady=25, text="Dekongestan \n\nmembantu mengencerkan lendir atau ingus sehingga\n udara lebih mudah keluar-masuk melalui hidung \ndan Anda dapat bernapas dengan lega. \n\nRp50.000/ 1 pcs \n*Wajib resep dokter", bg='red', fg='white',font=("times new roman", 20, "bold"), border=0, command=resepdok3).place(x=790, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skepala).place(x=85, y=700)

#obatsinus
def Kortikosteroid():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN============= \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Sinusitis \nObat: Kortikosteroid \nHarga: Rp30.000/ 1 pcs \n'
    msgs3=f'Resep Dokter: {resep_var.get()}\n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    resepe=resep_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Sinusitis'],
    'Obat Yang Dibeli': ['Kortikosteroid'],
    'resep':[resepe]
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2 + "\n" + msgs3)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2+'\n'+msgs3)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def Dekongestan():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Sinusitis \nObat: Dekongestan \nRp50.000/ 1 pcs \n======================================'
    msgs3 =f'Resep Dokter: {resep_var.get()}\n======================================'


    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Sinusitis'],
    'Obat Yang Dibeli': ['Dekongestan'],
    'Harga':['Rp50.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2 + "\n" + msgs3)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs + "\n" + msgs2 + "\n" + msgs3)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


def hipertensi():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Hipertensi", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=319, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnobthipertensi1=Button(frem2, width=40, pady=25, text="Furosemide 40mg \n\nMengatasi penumpukan cairan di dalam tubuh \nEfek Samping: \npusing, dehidrasi, sering buang air kecil. \n\nHarga: Rp3.500/10 Tablet \n*Wajib resep dokter", font=("times new roman", 25, "bold"), bg='red', fg='white', border=0, command=resepdok).place(x=20, y=250)
    btnobthipertensi2=Button(frem2, width=30, pady=25, text="Captopril 12.5mg \n\nEfek Samping: \nPusing atau sensasi rasa melayang \nHilang kemampuan merasa \nRasa hangat di wajah, leher, atau dada \nHarga: \nRp2.000/10 Tablet", font=("times new roman", 25, "bold"),bg='red', fg='white', border=0, command=captopril).place(x=900, y=250)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skepala).place(x=85, y=700)
    btnselanjutnya2=Button(frem2, width=10, pady=10, text=">", bg='green', font=('aria', 20, 'bold'), border=0, command=hipertensi2).place(x=1302, y=700)
def hipertensi2():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Hipertensi", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=319, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnobthipertensi1=Button(frem2, width=30, pady=17, text="Valsartan 80mg \n\nEfek Samping: \nkelelahan \njarang diare \nsakit kepala \nmimisan \ntrombositopenia \nnyeri sendi \n\nHarga: Rp40.000/10 Tablet", font=("times new roman", 25, "bold"),bg='red', fg='white', border=0, command=valsartan).place(x=20, y=200)
    btnobthipertensi2=Button(frem2, width=30, pady=17, text="Amlodipine 10mg \n\nEfek Samping: pusing \nmengantuk \nsakit perut \nmual \nkelelahan \n\nHarga: Rp6.000/10 Tablet", font=("times new roman", 25, "bold"),bg='red', fg='white', border=0, command=amlodipine).place(x=900, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=hipertensi).place(x=85, y=700)

#obathipertensy
def furosemide():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    

    msgs = f'============STRUK PEMBAYARAN============= \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Hipertensi \nObat: Furosemide 40mg \nHarga: Rp3.500/10 Tablet \n'
    msgs3=f'Resep Dokter: {resep_var.get()}\n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    resepe=resep_var.get()

    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Hipertensi'],
    'Obat Yang Dibeli': ['Furosemide'],
    'Resep Obat': [resepe]
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Struk', msgs + "\n" + msgs2 + "\n" + msgs3)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2+'\n'+msgs3)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def captopril():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Hipertensi \nObat: Captoprill \nHarga: Rp2.000/10 Tablet \n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Hipertensi'],
    'Obat Yang Dibeli': ['Captoprill'],
    'Harga':['Rp2.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
#obathipertensi2
def valsartan():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Hipertensi \nObat: Varsartan \nHarga: Rp40.000/10 Tablet \n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Hipertensi'],
    'Obat Yang Dibeli': ['Varsartan'],
    'Harga':['Rp40.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def amlodipine():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Hipertensi \nObat: Amlodipine \nHarga: Rp57.000/1 BOX (isi 10 strip (10 tablet)) \n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Hipertensi'],
    'Obat Yang Dibeli': ['Amlodipine'],
    'Harga':['Rp57.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Struk', msgs + "\n" + msgs2)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)



"""==================================CODINGAN SAKIT OTOT================================"""
def sotot():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnbatuk2=Button(frem2, width=20, text="Distrofi Otot \n\nKesulitan berjalan, \nPostur tubuh buruk, \nReflek tubuh berkurang", font=("times new roman", 30, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatdistrofiotot).place(x=200, y=250)
    btnbatuk3=Button(frem2, width=20, text="Keseleo", font=("times new roman", 30, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatkeseleo).place(x=850, y=250)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan).place(x=85, y=700)
def obatdistrofiotot():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Distrofiotot", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=269, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnsrwan1=Button(frem2, width=30, pady=30, text="Barbiturat\n\nHarga: Rp40.000/Botol (190ml)", bg='blue', fg='white', font=("times new roman", 25, "bold"),border=0, command=barbiturat).place(x=70, y=160)
    btnsrwan2=Button(frem2, width=30, pady=30, text="Prednison\n\n-Menyembuhkan sakit tenggorokan, \n-Peradangan rongga mulut\n!Tidak dikonsumsi anak dibawah 10Tahun!\nHarga: Rp14.000/Strip(10 Tablet)", bg='green', fg='white',font=("times new roman", 25, "bold"),border=0, command=Prednison).place(x=800, y=160)
    btnsrwan3=Button(frem2, width=35, pady=30, text="ACE inhibitor\n\nHarga: Rp40.000/Botol (15ml)", font=("times new roman", 25, "bold"),bg='green', fg='white', border=0, command=obtnovelcooling).place(x=70, y=500)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sotot).place(x=85, y=700)
def obatkeseleo():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Keseleo", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=319, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnsrwan1=Button(frem2, width=30, pady=30, text="Diclofenac Sodium\n\nMengobati nyeri dan peradangan\n\nHarga: Rp4.000/strip (10 tablet)", font=("times new roman", 25, "bold"),bg='blue', fg='white', border=0, command=obtbetadine).place(x=70, y=160)
    btnsrwan2=Button(frem2, width=30, pady=30, text="Cardio Aspirin\n\n-Meredakan nyeri, \n-peradangan dan mencegah \nterbentuknya gumpalan darah\nHarga: Rp19.000/Strip(10 Tablet)", font=("times new roman", 25, "bold"),bg='green', fg='white', border=0, command=obtdegirol).place(x=70, y=450)
    btnsrwan1=Button(frem2, width=30, pady=30, text="Capsaicin Cream \n\nMeredakan nyeri \nEfek Samping: \nMelepuh/bengkak di daerah penggunaan \nPeningkatan rasa sakit tidak biasa\n di daerah penggunaan. \n\nHarga: Rp35.000/1 Bungkus", bg='blue', fg='white', font=("times new roman", 25, "bold"),border=0, command=capsaicin).place(x=870, y=160)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sotot).place(x=85, y=700)

#obatdistrofotot
def barbiturat():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=370, pady=8)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Distrofi Otot \nObat: Barbiturat \nHarga: Rp40.000/Botol (190ml) \n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Distrofi otot'],
    'Obat Yang Dibeli': ['Barbiturat'],
    'Harga':['Rp40.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def Prednison():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Distrofi Otot \nObat: Prednison \nHarga: Rp14.000/Strip(10 Tablet)\n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Distrofi otot'],
    'Obat Yang Dibeli': ['predinson'],
    'Harga':['Rp14.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def ACEinhibitor():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Distrofi Otot \nObat: ACEinhibitor \nHarga: Rp40.000//botol\n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Distrofi otot'],
    'Obat Yang Dibeli': ['ACEinhibitor'],
    'Harga':['Rp40.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)



"""==================================CODINGAN pERNAPASAN================================"""
def pernapasan():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)
    
    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnbatuk2=Button(frem2, width=20, text="Asma", font=("times new roman", 30, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=asma).place(x=200, y=250)
    btnbatuk3=Button(frem2, width=20, text="Flu", font=("times new roman", 30, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=flu).place(x=850, y=250)
    btnbatuk3=Button(frem2, width=20, text="Tuberkolosis (TBC)", font=("times new roman", 30, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=tbc).place(x=200, y=450)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan).place(x=85, y=700)
def asma():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)
    
    heading2=Label(frem2, text="Rekomendasi Obat Asma", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=359, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnsrwan1=Button(frem2, width=30, pady=30, text="Antrovent MDI 10mL 200 doses \n\nEfek samping:\nMulut kering, \niritasi tenggorokan/reaksi alergi,\nbatuk\n\nHarga: Rp240.000/buah (10ml)", font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=antrovent).place(x=70, y=200)
    btnsrwan2=Button(frem2, width=50, pady=30, text="Ventolin inhaler 200 doses\n\nmeredakan/mengontrol gejala \npenyempitan saluran pernapasan akibat asma, \nEfek samping: \n-Rasa tertekan \n-vasodilatasi perifer\n-Sakit kepala \n\nHarga: Rp185.000/buah", font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=Ventolin).place(x=580, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=pernapasan).place(x=85, y=700)

    
def flu():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)
    
    heading2=Label(frem2, text="Rekomendasi Obat Flu", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)

    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnsrwan1=Button(frem2, width=30, pady=30, text="Mixagrip Flu\n\nMengobati nyeri dan peradangan\nHarga: Rp4.000/strip (10 tablet)", font=("times new roman", 20, "bold"), bg='blue', fg='white', border=0, command=mixagrip).place(x=70, y=200)
    btnsrwan2=Button(frem2, width=50, pady=30, text="panadol\n\n-Meredakan nyeri, \n-peradangan dan mencegah terbentuknya gumpalan darah\n\nHarga: Rp19.000/Strip(10 Tablet)",font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=panadol).place(x=680, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=pernapasan).place(x=85, y=700)

def tbc():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)
    
    heading2=Label(frem2, text="Rekomendasi Obat TBC", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)

    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=720)
    btnsrwan1=Button(frem2, width=30, pady=30, text="Isoniazid 300mg \nEfek samping: \n-muntah\n-pusing\n-lemas\n-maag\nHarga: Rp5.000/strip (10 tablet)", font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=isoniazid).place(x=70, y=180)
    btnsrwan2=Button(frem2, width=30, pady=30, text="Rifampicin 600mg \n\Efek samping: \n-mual, muntah\n-diare\nkantuk\n\nHarga: Rp40.000/Strip(10 Tablet)",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=Rifampicin).place(x=780, y=180)
    btnsrwan3=Button(frem2, width=30, pady=30, text="Ethambutol 500mg \nEfek samping: \n-muntah, mual\n-lemas\nHarga: Rp15.000/strip (10 tablet)", font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=Ethambutol).place(x=480, y=480)

    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=pernapasan).place(x=85, y=700)


#obattbc
def isoniazid():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : TBC \nObat: Isoniazid 300mg \nHarga: Rp5.000/strip (10 tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['TBC'],
    'Obat Yang Dibeli': ['Isoniazid'],
    'Harga':['Rp5.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def Rifampicin():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : TBC \nObat: Rifampicin 600mg \nHarga: Rp40.000/strip (10 tablet) \n======================================'
    
    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['TBC'],
    'Obat Yang Dibeli': ['Rifampicin'],
    'Harga':['Rp40.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def Ethambutol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : TBC \nObat: Ethambutol 500mg \nHarga: Rp15.000/strip (10 tablet) \n======================================'
    
    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['TBC'],
    'Obat Yang Dibeli': ['Ethambutol'],
    'Harga':['Rp15.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)



#obatasma
def Ventolin():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Asma \nObat: Ventolin inhaler 200 doses \nHarga: Rp185.000 \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Asma'],
    'Obat Yang Dibeli': ['Ventolin inhaler'],
    'Harga':['Rp185.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def antrovent():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Asma \nObat: Antrovent MDI 10mL 200 doses (inhaler) \nHarga: Rp240.000/buah (10ml) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()
    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Asma'],
    'Obat Yang Dibeli': ['Antrovent MDI'],
    'Harga':['Rp240.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)




#obatnyaflu
def mixagrip():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Flu \nObat: Mixagrip \nHarga: Rp4.000/strip (10 tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Flu'],
    'Obat Yang Dibeli': ['Mixagrip'],
    'Harga':['Rp4.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def panadol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
  
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Flu \nObat: Panadol \nHarga: Rp19.000/strip (10 tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['flu'],
    'Obat Yang Dibeli': ['Panadol'],
    'Harga':['Rp19.000']

    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)



"""==================================CODINGAN SAKIT GIGI================================"""
def sgigi():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnbatuk2=Button(frem2, width=20, text="Sariawan",font=("times new roman", 30, "bold"), bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatsariawan).place(x=200, y=250)
    btnbatuk3=Button(frem2, width=30, text="Gingivitis (peradangan gusi) \n\n•Terdapat nanah antara gigi dan gusi\n•Gusi bengkak dan sakit\n•Warna gusi merah kehitaman\n•Bau napas tidak sedap, \nmisalnya seperti bau logam", font=("times new roman", 20, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatgingivitis).place(x=850, y=250)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan).place(x=85, y=700)
def obatsariawan():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Sariawan", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=305, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnsrwan1=Button(frem2, width=30, pady=30, text="Betadine kumur\n\nHarga: Rp40.000/Botol (190ml)", font=("times new roman", 20, "bold"),bg='blue', fg='white', border=0, command=obtbetadine).place(x=70, y=200)
    btnsrwan2=Button(frem2, width=50, pady=30, text="Degirol 0,25mg (obat hisap) \n\n-Menyembuhkan sakit tenggorokan, \n-Peradangan rongga mulut\n!Tidak dikonsumsi anak dibawah 10Tahun!\nHarga: Rp14.000/Strip(10 Tablet)", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=obtdegirol).place(x=680, y=200)
    btnsrwan3=Button(frem2, width=35, pady=30, text="Novell Cooling 5 Spray Cool Mint (spray)\n\nHarga: Rp40.000/Botol (15ml)", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=obtnovelcooling).place(x=70, y=450)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sgigi).place(x=85, y=700)
def obtbetadine():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=269, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Sariawan \nObat: Betadine Kumur \nHarga: Rp40.000/Botol \n======================================'
   
    namanye=nama_var.get()
    umoer=umur_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Sariawan'],
    'Obat Yang Dibeli': ['Betadine kumur'],
    'Harga':['Rp40.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)

    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtdegirol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : sariawan \nObat: Degirol 0,25mg (obat hisap) \nHarga: Rp14.000/strip(10 Tablet)\n!Tidak dikonsumsi untuk anak dibawan 10 Tahun! \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Sariawan'],
    'Obat Yang Dibeli': ['Degirol'],
    'Harga':['Rp14.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtnovelcooling():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
   
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Sariawan \nObat: Novell Cooling 5 Spray Cool Mint (spray) \nHarga: Rp40.000/Botol \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Sariawan'],
    'Obat Yang Dibeli': ['Novell Cooling'],
    'Harga':['Rp40.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


def obatgingivitis():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Gingivitis (Peradangan Gusi)", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=249, pady=4)
    heading2.place(x=10, y=1)
   
    btngingi1=Button(frem2, width=40, pady=20, text="Minosep Chlorhexidine (Obat Kumur) \n\nberguna untuk membantu mengurangi peradangan, \npembengkakan, dan pendarahan gusi. \nEfek samping: \n-Mulut kering \n-Perubahan rasa makanan atau minuman\nHarga: Rp33.000/Botol (150ml)", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=obtminosep).place(x=50, y=200)
    btngingi2=Button(frem2, width=46, pady=20, text="Grafadon-Acetaminophen \n\nMembantu meringankan ketidaknyamanan gigi dan mulut. \nEfek samping: \n-Sakit tenggorokan\n-Kelelahan atau kelemahan yang luar biasa \nHarga: Rp4.000/Strip(10 Tablet)", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=obtgrafadon).place(x=760, y=200)
    btnselanjutnya2=Button(frem2, width=10, pady=10, text=">", bg='green', font=('aria', 20, 'bold'), border=0, command=obatgingivitis2).place(x=1302, y=700)
    btnsebelum=Button(frem2, width=10, pady=10, text="<",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sgigi).place(x=85, y=700)
def obatgingivitis2():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Gingivitis (Peradangan Gusi)",font=("times new roman", 40, "bold"), bd=30
                        , bg="#FFB6C1", fg="#ff007f", padx=369, pady=4)
    heading2.place(x=10, y=1)

    btngingi3=Button(frem2, width=30, pady=30, text="Antibiotik Amoksisilin \n\nmembantu mengobati infeksi gigi. \nEfek samping: \n-Diare\n-Mual\n-sakit kepala \nHarga: Rp7.700/Strip(10 Tablet)", font=("times new roman", 20, "bold"),bg='red', fg='white', border=0, command=obtantibiotik).place(x=400, y=200)
    
    btnsebelum=Button(frem2, width=10, pady=10, text="<",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=obatgingivitis).place(x=85, y=700)
def obtminosep():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
 
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Peradangan Gusi \nObat: Minosep Chlorhexidine (Obat Kumur) \nHarga: Rp33.000/Botol \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Peradangan Gusi'],
    'Obat Yang Dibeli': ['Minosep Chlorhexidine'],
    'Harga':['Rp33.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obtgrafadon():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Peradangan Gusi \nObat: Grafadon-Acetaminophen \nHarga: Rp4.000/Strip(10 Tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Peradangan Gusi'],
    'Obat Yang Dibeli': ['Grafadon-Acetaminophen'],
    'Harga':['Rp4.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obtantibiotik():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)

    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Peradangan Gusi \nObat: Antibiotik Amoksisilin \nHarga: Rp7.700/Strip(10 Tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Peradangan Gusi'],
    'Obat Yang Dibeli': ['Antibiotik Amoksisilin'],
    'Harga':['Rp7.700']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)



"""==================================CODINGAN SAKIT PUSING================================"""
def pusing():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)

    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnpusing1=Button(frem2, width=40, pady=30, text="Oskadon \n\ncocok digunakan untuk sakit \nkepala dan sakit gigi. \nEfek Samping: \nMual, Muntah, Nyeri lambung/rasa panas di ulu hati. \n\nHarga: Rp2.000/1 Strip (4 Tablet) ",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=oskadon).place(x=70, y=200)
    btnpusing2=Button(frem2, width=40, pady=30, text="Bodrex \n\ndigunakan untuk meringankan sakit kepala,\n sakit gigi, dan menurunkan demam. \nEfek Samping: \nGejala alergi atau ruam \ntekanan darah rendah \nsulit tidur dan gangguan fungsi hati \nHarga: \nRp5.000/1 Strip (10 Tablet)",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=bodrex).place(x=780, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skepala2).place(x=85, y=700)

def bodrex():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)

    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan :  Pusing \nObat: Bodrex \nHarga: Rp5.000/Strip(10 Tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Pusing'],
    'Obat Yang Dibeli': ['Bodrex'],
    'Harga':['Rp5.000']

    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


def oskadon():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)

    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan :  Pusing \nObat: Oskadon \nHarga: Rp2.000/Strip(10 Tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Pusing'],
    'Obat Yang Dibeli': ['Oskadon'],
    'Harga':['Rp2.000']

    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)




"""==================================CODINGAN SAKIT SENDI================================"""
def sendi():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)

    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnsendi2=Button(frem2, width=30, pady=30, text="Arthritis (Radang Sendi): \n •Nyeri atau rasa sakit \n •sendi terasa kaku dan sulit digerakkan", font=("times new roman", 30, "bold"),bg='#ff007f', fg='white', border=0, command=obatkrim).place(x=100, y=200)
    btnsendi3=Button(frem2, width=20, pady=30, text="Asam Urat", bg='#ff007f', fg='white',font=("times new roman", 30, "bold"), border=0, command=asamurat).place(x=900, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan).place(x=85, y=700)


def asamurat():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Asam Urat", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=278, pady=4)
    heading2.place(x=10, y=1)

    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnbatuksirup1=Button(frem2, width=30, pady=30, text="Kolton - Allopurinol \nEfek Samping: \n•Hipersensitivitas \n•Gangguan kulit dan jaringan subkutan \n•Gangguan gastrointestinal \n•Mengantuk dan sakit kepala. \n\nHarga: Rp15.000/10 Tablet \n*Wajib Resep Dokter",font=("times new roman", 25, "bold"), bg='red', fg='white', border=0, command=kolton).place(x=90, y=190)
    btnbatuktablet1=Button(frem2, width=35, pady=30, text="Ibuprofen \nPeringatan: \n•Pasien gagal jantung \n•Gangguan ginjal dan hati \n•Hindari merokok dan minuman beralkohol \n•Kondisi kulit sensitif. \n\nHarga: Rp3.000/10 Tablet", font=("times new roman", 25, "bold"),bg='red', fg='white', border=0, command=ibuprofen).place(x=800, y=190)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sendi).place(x=85, y=700)


#ovbatradangsendi
def obatkrim():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Radang Sendi", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=299, pady=4)
    heading2.place(x=10, y=1)

    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnsrwan1=Button(frem2, width=30, pady=30, text="Capsaicin Cream \n\nMeredakan nyeri \nEfek Samping: \nMelepuh/bengkak di daerah penggunaan \nPeningkatan rasa sakit tidak biasa\n di daerah penggunaan. \n\nHarga: Rp35.000/1 Bungkus", bg='blue', fg='white', font=("times new roman", 25, "bold"),border=0, command=capsaicin).place(x=70, y=160)
    btnsrwan2=Button(frem2, width=30, pady=30, text="Counterpain \n\nMeredakan nyeri \nEfek samping: \nGatal \nKulit kemerahan \nHarga: Rp30.000/1 Tube(50gr)", bg='green', fg='white',font=("times new roman", 25, "bold"),border=0, command=counterpain).place(x=800, y=160)

    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sendi).place(x=85, y=700)


#obatkrimrdngsndi
def capsaicin():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)

    msgs = f'Nama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Radang Sendi \nObat: capsaicin \nHarga: Rp35.000/1 bungkus \n'

    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Radang sendi'],
    'Obat Yang Dibeli': ['Capsaicin'],
    'Harga':['Rp35.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def counterpain():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)

    msgs = f'Nama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Radang Sendi \nObat: Counterpain \nHarga: Rp30.000/1 Tube (50gr) \n'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Radang Sendi'],
    'Obat Yang Dibeli': ['Counterpain'],
    'Harga':['Rp30.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


#obatasamurat
def kolton():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)


    msgs = f'Nama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Asam Urat \nObat: Kolton - Allopurinol \nHarga: Rp15.000/10 Tablet \n'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Asam Urat'],
    'Obat Yang Dibeli': ['Kolton - Allopurinol'],
    'Harga':['Rp15.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)

    showinfo( 'Struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def ibuprofen():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=8)
    heading2.place(x=10, y=1)

    msgs = f'Nama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Asam Urat \nObat: Ibuprofen \nHarga: Rp3.000/10 Tablet \n'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Asam Urat'],
    'Obat Yang Dibeli': ['Ibuprofen'],
    'Harga':['Rp3.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)

    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)



"""==================================CODINGAN RESEP DOKTER================================"""
def resepdokk2():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Masukan Resep Dokter", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=415, pady=4)
    heading2.place(x=10, y=1)
   
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='white', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=700, y=590)

    def on_enter3(e):
        resepdok.delete(0, 'end')
    def on_leave3(e):
        resep=resepdok.get()
        if resep=='':
            resepdok.insert(0, 'Resep Dokter')

    resepdok=Entry(frem2, width=40, fg='black', bg='white', textvariable=resep_var, font=('Microsoft YaHei UI Light', 30))
    resepdok.place(x=340, y=350)
    resepdok.insert(0, 'Resep Dokter')
    resepdok.bind('<FocusIn>', on_enter3)
    resepdok.bind('<FocusOut>', on_leave3)


    Frame(frem2, width=500, height=2, bg='black').place(x=340, y=435)
    buttonkirim=Button(frem2, width=10, pady=10, text="Kirim", font=("times new roman", 30, "bold"), bg='#ff007f', fg='white', border=0, command=Kortikosteroid).place(x=690, y=700)
def resepdok3():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Masukan Resep Dokter", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=415, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='white', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=700, y=590)

    def on_enter4(e):
        resepdok.delete(0, 'end')
    def on_leave4(e):
        resep=resepdok.get()
        if resep=='':
            resepdok.insert(0, 'Resep Dokter')

    resepdok=Entry(frem2, width=40, fg='black', bg='white', textvariable=resep_var, font=('Microsoft YaHei UI Light', 30))
    resepdok.place(x=340, y=350)
    resepdok.insert(0, 'Resep Dokter')
    resepdok.bind('<FocusIn>', on_enter4)
    resepdok.bind('<FocusOut>', on_leave4)


    Frame(frem2, width=500, height=2, bg='black').place(x=340, y=435)
    buttonkirim=Button(frem2, width=10, pady=10, text="Kirim", font=("times new roman", 30, "bold"), bg='#ff007f', fg='white', border=0, command=Dekongestan).place(x=690, y=700)


def resepdok():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Masukan Resep Dokter", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=415, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='white', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=700, y=590)
    def on_enter2(e):
        resepdok.delete(0, 'end')
    def on_leave2(e):
        resep=resepdok.get()
        if resep=='':
            resepdok.insert(0, 'Resep Dokter')

    resepdok=Entry(frem2, width=40, fg='black', bg='white', textvariable=resep_var, font=('Microsoft YaHei UI Light', 30))
    resepdok.place(x=340, y=350)
    resepdok.insert(0, 'Resep Dokter')
    resepdok.bind('<FocusIn>', on_enter2)
    resepdok.bind('<FocusOut>', on_leave2)

    
    Frame(frem2, width=500, height=2, bg='black').place(x=340, y=435)
    buttonkirim=Button(frem2, width=10, pady=10, text="Kirim", font=("times new roman", 30, "bold"), bg='#ff007f', fg='white', border=0, command=furosemide).place(x=690, y=700)


"""==================================CODINGAN SAKIT KULIT================================"""
def skulit():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=488, pady=4)
    heading2.place(x=10, y=1)

    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnbatuk2=Button(frem2, width=15, text="jerawat", bg='#ff007f', fg='white',font=("times new roman", 40, "bold"), relief=RAISED, padx=1, pady=10, command=obatjerawat).place(x=100, y=200)
    btnbatuk2=Button(frem2, width=15, text="Panu", bg='#ff007f', fg='white',font=("times new roman", 40, "bold"), relief=RAISED, padx=1, pady=10, command=obatpanu).place(x=950, y=200)
    btnbatuk3=Button(frem2, width=15, text="Bisul", bg='#ff007f', fg='white',font=("times new roman", 40, "bold"), relief=RAISED, padx=1, pady=10, command=obatbisul).place(x=550, y=400)
    btnsebelum=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan).place(x=85, y=700)


def obatjerawat():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Jerawat", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnsrwan1=Button(frem2, width=30, pady=30, text="Acnes Gel\n\nHarga: Rp25.000/pcs (9Gram)\nUntuk usia >13 tahun", font=("times new roman", 20, "bold"),bg='blue', fg='white', border=0, command=obtacnes).place(x=70, y=200)
    btnsrwan2=Button(frem2, width=50, pady=30, text="Acnol \n\n-Mengeringkan jerawat meradang\nUntuk usia >13 tahun \nHarga: Rp14.000/Botol", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=obtacnol).place(x=620, y=200)
    btnsrwan3=Button(frem2, width=35, pady=30, text="Benzolac\nUntuk usia >13 tahun\nHarga: Rp37.000/pcs (10gram)", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=obtbenzolac).place(x=70, y=450)
    btnsebelum=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skulit).place(x=85, y=700)
def obtacnes():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Jerawat \nObat: Acnes Gel \nHarga: Rp25.000/pcs \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Jerawat'],
    'Obat Yang Dibeli': ['Acnes Gel'],
    'Harga':['Rp25.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtacnol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARANirol=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : jerawat \nObat: Acnol \nHarga: Rp14.000/Botol\n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Jerawat'],
    'Obat Yang Dibeli': ['Acnol'],
    'Harga':['Rp14.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtbenzolac():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Jerawat \nObat: Benzolac \nHarga: Rp37.000/pcs \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Jerawat'],
    'Obat Yang Dibeli': ['Benzolac'],
    'Harga':['Rp37.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obatbisul():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Bisul", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=459, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btngingi1=Button(frem2, width=40, pady=30, text="ICHTYOL \n\nberguna sebagai antiseptik \nuntuk mengatasi bisul,\nanti bakteri, anti jamur dan anti peradangan\nAman untuk anak kecil dan ibu menyususi \nEfek samping:  \n-Gatal\nHarga: Rp9.000/Pot ", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=obtichtyol).place(x=70, y=200)
    btngingi2=Button(frem2, width=40, pady=30, text="Kapsida \n\nMembantu mengurangi gatal-gatal.\nMelancarkan peredaran darah dan \nmemelihara kesehatan kulit \nEfek samping: \n-Tidak ada efek samping \nHarga: Rp15.000/Botol(12 capsul)",font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=obtkapsida).place(x=840, y=200)
    btnsebelum=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skulit).place(x=85, y=700)
def obtichtyol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Bisul \nObat: ICHTYOL \nRp9.000/Pot \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['bisul'],
    'Obat Yang Dibeli': ['Ichtyol'],
    'Harga':['Rp9.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtkapsida():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Bisul \nObat: Kapsida \nRp15.000/Botol(12 capsul) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Bisul'],
    'Obat Yang Dibeli': ['Kapsida'],
    'Harga':['Rp15.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obatpanu():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Panu", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=459, pady=4)
    heading2.place(x=10, y=1)
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)


    btngingi1=Button(frem2, width=40, pady=30, text="Nizoral Tablet\n\nuntuk membantu mengobati\n infeksi jamur pada kulit\nGolongan obat keras \nEfek samping:  \n-\nHarga: Rp80.000/strip ",font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=obtnizoraltblt).place(x=70, y=200)
    btngingi2=Button(frem2, width=40, pady=30, text="Kapsida \n\nMembantu mengurangi gatal-gatal.\nMelancarkan peredaran darah\n dan memelihara kesehatan kulit \nEfek samping: \n-Tidak ada efek samping \nHarga: Rp15.000/Botol(12 capsul)",font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=obtkapsida).place(x=740, y=200)
    btnsebelum=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skulit).place(x=85, y=700)

def obtnizoraltblt():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Bisul \nObat: Nizoral Tablet \nRp80.000/Strip \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Bisul'],
    'Obat Yang Dibeli': ['Nizoral'],
    'Harga':['Rp80.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtkapsida():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Bisul \nObat: Kapsida \nRp15.000/Botol(12 capsul) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Bisul'],
    'Obat Yang Dibeli': ['Kapsida'],
    'Harga':['Rp15.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)



"""==================================CODINGAN SAKIT DIABETES================================"""
def sdiabetes():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btndbts=Button(frem2, width=20, text="Diabetes tipe 2", bg='#ff007f', fg='white', font=("times new roman", 30, "bold"), command=obatdbts).place(x=900, y=250)
    btndbts2=Button(frem2, width=20, text="Diabetes tipe 1", bg='#ff007f', fg='white', font=("times new roman", 30, "bold"),  command=obatdbts2).place(x=150, y=250)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan).place(x=85, y=700)

def obatdbts():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Diabetes", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btndbts=Button(frem2, width=30, pady=30, text="Glabinclamide\n\n-Mengurangi kadar gula darah\n-Efek samping: mual,diare, muntah\nHarga: Rp26.000/Dus ", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=obtglabinclamide).place(x=520, y=200)
    btndbts=Button(frem2, width=50, pady=30, text="Metformin \n\n-Mengurangi kadar gula yang diproduksi oleh organ hati (liver) \nEfek samping: mual, diare, lidah kebas, nafsu makan berkurang\nHarga: Rp30.000/Dus", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=obtmetformin).place(x=350, y=450)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sdiabetes).place(x=85, y=700)
    btnselanjutnya2=Button(frem2, width=10, pady=10, text=">", bg='green', font=('aria', 20, 'bold'), border=0, command=obatdbts2).place(x=1302, y=700)


def obatdbts2():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Diabetes", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btndbts=Button(frem2, width=35, pady=30, text="Pioglitazone\n\nuntuk mengontrol kadar glukosa dalam darah pada penderita Diabetes Tipe 2\nEfek samping: gangguan penglihatan, sinusitis, edema ringan s/d sedang, insomnia, anemia\nHarga: Rp4.800/Tablet", font=('times new roman', 20, 'bold'),bg='green', fg='white', border=0, command=obtpioglitazone).place(x=70, y=250)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=obatdbts).place(x=85, y=700)
def obtglabinclamide():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=359, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Diabetes tipe 2 \nObat: Tablet Glabinclamide \nHarga: Rp26.000/Dus \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Diabetes Tipe 2'],
    'Obat Yang Dibeli': ['Glabinclamide'],
    'Harga':['Rp26.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtmetformin():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=359, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Diabetes tipe 2 \nObat: Metformin \nHarga: Rp30.000/Dus\nTidak dikonsumsi untuk anak dibawan 10 Tahun! \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Diabetes Tipe 2'],
    'Obat Yang Dibeli': ['Metformin'],
    'Harga':['Rp30.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtpioglitazone():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Diabetes tipe 2 \nObat: Pioglitazone \nHarga: Rp4.800/Tablet \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Diabetes Tipe 2'],
    'Obat Yang Dibeli': ['Pioglitazone'],
    'Harga':['Rp4.800']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obatdbts2():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Diabetes Tipe 1", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=479, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btndbts2=Button(frem2, width=40, pady=30, text="Insulin Aprida Solostar pen \n\nEfek samping: kemerahan kulit, pembengkakan\nHarga: Rp230.000/Pen",font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=obtaspen).place(x=440, y=250)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sdiabetes).place(x=85, y=700)

def obtaspen():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Diabetes tipe 1 \nObat: Insulin Aprida Solostar pen \nHarga: Rp230.000/Pen \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Diabetes Tipe 1'],
    'Obat Yang Dibeli': ['Insulin Aprida Solostar Pen'],
    'Harga':['Rp230.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)





#=============================================================KeluhanHal2====================================



"""==================================CODINGAN SAKIT MATA================================"""
def smata():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnmta=Button(frem2, width=20, text="Mata Memerah dan Gatal",font=("times new roman", 30, "bold"), bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatmtamrh).place(x=150, y=200)
    btnmta2=Button(frem2, width=20, text="Belekan", bg='#ff007f',font=("times new roman", 30, "bold"), fg='white', relief=RAISED, padx=1, pady=30, command=obatbelekan).place(x=830, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan2).place(x=85, y=700)
def obatmtamrh():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Mata Merah dan Gatal", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnmta=Button(frem2, width=40, pady=30, text="Insto (15ml)\n\nuntuk mata yang memerah, gatal karena \niritasi ringan yang disebabkan oleh debu dan asap.\nDosis: sehari 3-4 x 2-3 tetes pada setiap mata\n-Efek samping: mata perih, panas, hiperemia\nHarga: Rp 15.398,- / Tube ",font=("times new roman", 20, "bold"), bg='blue', fg='white', border=0, command=obtinsto).place(x=70, y=200)
    btnmta=Button(frem2, width=45, pady=30, text="Rohto Cool Eye Drop (7ml) \n\nuntuk meredakan mata merah akibat iritasi\n ringan yang disebabkan debu, asap, angin atau alergi.\nDosis: 3-4x sehari teteskan 1 atau 2 tetes \nEfek samping: mata pedih, panas,\nhipereremi pada penggunaan yang berlebihan\nHarga: Rp 19.049,- / Botol",font=("times new roman", 20, "bold"), bg='blue', fg='white', border=0, command=obtcool).place(x=780, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=smata).place(x=85, y=700)
    btnselanjutnya2=Button(frem2, width=10, pady=10, text=">", bg='green', font=('aria', 20, 'bold'), border=0, command=obatmtamrh2).place(x=1302, y=700)

def obatmtamrh2():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Mata Merah dan Gatal", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnmta=Button(frem2, width=50, pady=30, text="Braito Tears 5ml\n\nMengatasi \ngejala mata kering, menyejukkan mata & sebagai lubrikan mata\n1-2 tetes pada mata yang sakit\nEfek samping: -\nHarga: Rp 12.192,- / Pcs",font=("times new roman", 20, "bold"), bg='blue', fg='white', border=0, command=obtbraito).place(x=70, y=200)

    btnkembali1=Button(frem2, width=10, pady=10, text="<",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=obatmtamrh).place(x=85, y=700)

def obtinsto():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Mata Memerah dan Gatal \nObat: Tetes Insto \nHarga: Rp 15.398,- / Tube \n======================================'
    
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Mata Gatal Dan Merah'],
    'Obat Yang Dibeli': ['Tetes Insto'],
    'Harga':['Rp15.398']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtcool():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Mata Memerah dan Gatal \nObat: Rohto Cool Eye Drop (7ml)  \nHarga:  Rp 19.049,- / Botol \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Mata Merah dan Gatal'],
    'Obat Yang Dibeli': ['Rohto Cool Eye'],
    'Harga':['Rp19.049']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtbraito():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Mata Memerah dan Gatal \nObat: Braito Tears 5ml\nHarga: Rp 12.192,- / Pcs \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Mata Merah dan Gatal'],
    'Obat Yang Dibeli': ['Braito Tears'],
    'Harga':['Rp12.192']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obatbelekan():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Belekan", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=359, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btndbts2=Button(frem2, width=50, pady=30, text="Polidemisine Eye Drop\n\nuntuk mengobati infeksi dan peradangan\nDosis: 4-6 x sehari 1 atau 2 tetes pada mata yang terinfeksi\nEfek samping: sensitasi konjungtiva\nHarga: Rp 41.237,-/ Pcs", font=("times new roman", 30, "bold"), bg='red', fg='white', border=0, command=obtpolidemisine).place(x=50, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=smata).place(x=85, y=700)

def obtpolidemisine():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Sakit Mata Belekan \nObat: Polidemisine Eye Drop \nHarga: Rp 41.237,- / Pcs \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Sakit Mata Belekan'],
    'Obat Yang Dibeli': ['Polidemisine'],
    'Harga':['Rp41.237']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


"""==================================CODINGAN SAKIT SARAF================================"""
def ssaraf():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnsrf=Button(frem2, width=25, text="Epilepsi",font=("times new roman", 30, "bold"), bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatepilepsi).place(x=100, y=200)
    btnsrf2=Button(frem2, width=25, text="Stroke", font=("times new roman", 30, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatstroke).place(x=750, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan2).place(x=85, y=700)
def obatepilepsi():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Epilepsi", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=419, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnsrf=Button(frem2, width=30, pady=30, text="Bamgetol 200 mg @100 tablet\n\nuntuk meringankan nyeri saraf\nDosis: orang dewasa dan anak \nberusia > 12 tahun, \ndiawali dengan 200 mg 2x sehari,\n bisa ditingkatkan dalam jangka waktu \n1 minggu sampai 200 mg 3-4x sehari.\n-Efek samping: \nmual dan muntah, \npusing, mengantuk\nHarga: Rp 165.000,-/box ", font=("times new roman", 20, "bold"),bg='red', fg='white', border=0, command=obtbamgetol).place(x=70, y=200)
    btnsrf=Button(frem2, width=50, pady=30, text="Tegretol Tablet (200mg) \n\nuntuk mengobati epilepsi\nDosis: Dewasa diawali 100-200 mg sekali atau 2 kali sehari\nEfek samping: pusing, mengantuk, muntah\nHarga:  Rp 13.000 / Strip", font=("times new roman", 20, "bold"),bg='red', fg='white', border=0, command=obttegretol).place(x=660, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=ssaraf).place(x=85, y=700)
def obtbamgetol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Epilepsi \nObat: Bamgetol 200 mg\nHarga: Rp 165.000,-/box \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Epilepsi'],
    'Obat Yang Dibeli': ['Bamegetol'],
    'Harga':['Rp165.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obttegretol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Epilepsi\nObat: Tegretol Tablet (200mg) \nHarga:  Rp 13.000 / Strip\n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Epilepsi'],
    'Obat Yang Dibeli': ['Tegretol'],
    'Harga':['Rp13.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obatstroke():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Stroke", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btndbts2=Button(frem2, width=50, pady=30, text="Cpg 75mg Tablet\n\nmengurangi resiko terkena serangan jantung dan stroke\nDosis: 1 x sehari 1 tablet\nEfek samping: sakit kepala, pusing, paresthesia, \ngangguan gastrointestinal & hematologikal, ruam, pruritus\nHarga: Rp 23.113,- / Tablet", font=("times new roman", 20, "bold"),bg='red', fg='white', border=0, command=obtcpg).place(x=70, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=ssaraf).place(x=85, y=700)

def obtcpg():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 30, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Sakit Stroke \nObat:Cpg 75mg Tablet \nHarga: Rp 23.113,- / Tablet \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Stroke'],
    'Obat Yang Dibeli': ['Cpg'],
    'Harga':['Rp23.113']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo( 'Struk',msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


"""==================================CODINGAN SAKIT KELAMIN================================"""
def skelamin():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=479, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnbatuk2=Button(frem2, width=30, text="Disuria (Anyang-anyangan)",font=("times new roman", 20, "bold"), bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatdisuria).place(x=570, y=350)

    btnbatuk2=Button(frem2, width=30, text="Gatal",font=("times new roman", 20, "bold"), bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatgatal).place(x=170, y=200)
    btnbatuk3=Button(frem2, width=30, text="Sipilis",font=("times new roman", 20, "bold"), bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatsipilis).place(x=750, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan2).place(x=85, y=700)


def obatgatal():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Gatal Kelamin", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=329, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btngatal1=Button(frem2, width=40, pady=30, text="Climdamycyin \n\nHarga: Rp60.000/300mg \nUntuk usia >10 tahun, \nmemperlambat pertumbuhan bakteri", font=("times new roman", 20, "bold"),bg='red', fg='white', border=0, command=obtClimdamycyin).place(x=70, y=200)
    btngatal2=Button(frem2, width=40, pady=30, text="Salep 88 \n\n-membasmi jamur  yang \ndisebabkan oleh infeksi\nUntuk usia >13 tahun \nHarga: Rp14.000/Botol", font=("times new roman", 20, "bold"),bg='blue', fg='white', border=0, command=obtslp88).place(x=780, y=200)
    btngatal3=Button(frem2, width=35, pady=30, text="Miconazole \nUntuk menghambat biosintesis ergosterol yang \nmerusak biosintesis dan membran sel kelamin \nHarga: Rp8.000/pcs (10gram)",font=("times new roman", 20, "bold"), bg='blue', fg='white', border=0, command=obtmiconazol).place(x=70, y=450)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skelamin).place(x=85, y=700)
def obtClimdamycyin():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : gatal kelamin  \nObat: Climdamycyin kapsul \nHarga: Rp60.000/300mg \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Gatal Kelamin'],
    'Obat Yang Dibeli': ['Climdamycyin'],
    'Harga':['Rp60.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtslp88():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : gatal kelamin \nObat: Salep 88 \nHarga: Rp14 .000/Botol\n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Gatal Kelamin'],
    'Obat Yang Dibeli': ['Salep88'],
    'Harga':['Rp14.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtmiconazol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Gatal Kelamin \nObat: Miconazol \nHarga: Rp14.000/pcs \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['gatal kelamin'],
    'Obat Yang Dibeli': ['miconazol'],
    'Harga':['Rp14.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obatsipilis():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Sipilis ", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnsipilis1=Button(frem2, width=40, pady=30, text="Super Tetra \n\nmengobati infeksi bateri dikelamin\n dilarang untuk ibu menyusui, \nibu hamil dan usia <8 tahun\n  benjolankelamin\nHarga: Rp10.000 per strip ",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=obtsprtetra).place(x=10, y=200)
    btnsipilis2=Button(frem2, width=40, pady=30, text="Doxicor\n\nterapi penyandang sipilis\n belum aman untuk ibu menyusui dan\n ibu hamil usia minimal >10 \nEfek samping: \n-bisa saja demam \nHarga: Rp63.000/strep(10 capsul)", font=("times new roman", 20, "bold"),bg='red', fg='white', border=0, command=obtdoxicor).place(x=740, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skelamin).place(x=85, y=700)
def obtsprtetra():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Sipilis \nObat: super tetra \nRp10.000/strip \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Sipilis'],
    'Obat Yang Dibeli': ['Super Tetra'],
    'Harga':['Rp10.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtdoxicor():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : sipilis \nObat: Doxicor \nRp63.000/strep(10 capsul) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Sipilis'],
    'Obat Yang Dibeli': ['Doxicor'],
    'Harga':['Rp63.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obatdisuria():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Disuria ", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btndisuria1=Button(frem2, width=40, pady=30, text="Nephrolit\n\nuntuk melancarkan buang air kecil\nAnjuran minum air putih 2 liter / hari \n-\nHarga: Rp7000/strip (5kapsul)",font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=obtnephrolit).place(x=70, y=200)
    btndisuria2=Button(frem2, width=40, pady=30, text= "Uriupas \n\nmeredakan dan sekaligus mencegah\n otot kejang pada saluran kemih \nMembantu mengurangi sakit karena anyang anyang. \nHarga: Rp50.000/Strip(10 talblet)",font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=obturipas).place(x=740, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=skelamin).place(x=85, y=700)

def obtnephrolit():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : anyang anyangan \nObat: Nephrolit \nRp7.000/Strip (5 kapsul) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Anyang Anyangan'],
    'Obat Yang Dibeli': ['Nephrolit'],
    'Harga':['Rp7.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obturipas():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Anyang anyangan \nObat: Uripas \nRp60.000/Strip(10 tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Anyang anyangan'],
    'Obat Yang Dibeli': ['Uripas'],
    'Harga':['Rp60.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


"""==================================CODINGAN SAKIT DARAH================================"""
def sdarah():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih salah satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btndarah1=Button(frem2, width=20, text="Darah Rendah",font=("times new roman", 40, "bold"), bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatdarahrendah).place(x=100, y=200)
    btndarah2=Button(frem2, width=20, text="Darah Tinggi",font=("times new roman", 40, "bold"), bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=obatdrhtinggi).place(x=790, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan2).place(x=85, y=700)


def obatdarahrendah():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Darah Rendah", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=269, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btndarahrendah1=Button(frem2, width=35, pady=30, text="Midrodine \n\nHarga: Rp108.000/250mg(10pil) \nUntuk usia >10 tahun\n digunakan untuk mengobati tekanan \ndarah rendah ketika berdiri\n (hipotensi ortostatik)\n efek samping: \n detak jantung berdebar dan\n mata sedikit kabur", font=("times new roman", 20, "bold"),bg='blue', fg='white', border=0, command=obtmidodrin).place(x=70, y=200)
    btndarahrendah2=Button(frem2, width=50, pady=30, text="Maltofer Chewable\n\n-Suplemen penambah darah dalam bentuk \ntablet kunyah dengan rasa coklat yang \nenak dan tidak amis \nuntuk penyakit anemia\nUntuk usia anak >12th dan \naman untuk ibu hamil maupun menyusui \nHarga: Rp23.000/ strip(5tablet)",font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=obtmaltofer).place(x=680, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sdarah).place(x=85, y=700)
def obtmidodrin():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Darah Rendah  \nObat: midodrin tablet \nHarga: Rp108.000/250mg(10 tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Darah Rendah'],
    'Obat Yang Dibeli': ['Midodrin'],
    'Harga':['Rp108.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtmaltofer():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARANirol 10ml =============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Darah Rendah \nObat: Maltofer \nHarga: Rp23 .000/strip (6tablet)\n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Darah Rendah'],
    'Obat Yang Dibeli': ['Maltofer'],
    'Harga':['Rp23.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obatdrhtinggi():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Darah Tinggi", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=249, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btndrhtinggi1=Button(frem2, width=45, pady=30, text="Captopril \n\nUntuk mengurangi tekanan darah pada penderita \nhipertensi, gagal jantung kongestif, \ndan mengurangi kekambuhan dari stroke.\n Diperbolehkan untuk bayi dengan \ndosis yang ditentukan dokter\n Harga: Rp30.000/strip (10 tablet) ",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=obtcaptopril).place(x=10, y=200)
    btndrhtinggi2=Button(frem2, width=45, pady=30, text="Pacekap \n\n Suplemen herbal yang secara tradisional \ndapat membantu menurunkan tekanan darah\n yang tinggi pada penderita hipertensi \nsekaligus dapat meningkatka\nn daya tahan tubuh .\n usia > 10th\nHarga: Rp40.000/strip(10 capsul)",font=("times new roman", 20, "bold"), bg='darkgreen', fg='white', border=0, command=obtpacekap).place(x=790, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sdarah).place(x=85, y=700)
def obtcaptopril():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Darah Tinggi \nObat: captropil \nRp10.000/strip \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Darah Tinggi'],
    'Obat Yang Dibeli': ['Captropil']
    ,
    'Harga':['Rp10.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obtpacekap():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Darah Tinggi \nObat: Pacekap suplemen \nRp40.000/strip(10 capsul) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Darah Tinggi'],
    'Obat Yang Dibeli': ['Pacekap'],
    'Harga':['Rp40.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)



"""==================================CODINGAN SAKIT PERUT================================"""
def pencernaan():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih salah satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=489, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnpencernaan2=Button(frem2, width=20, text="Sembelit", font=("times new roman", 40, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=sembelit).place(x=80, y=200)
    btnpencernaan3=Button(frem2, width=20, text="Diare", font=("times new roman", 40, "bold"),bg='#ff007f', fg='white', relief=RAISED, padx=1, pady=30, command=diare).place(x=750, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan2).place(x=85, y=700)

#sembeliddd
def sembelit():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Sembelit", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=349, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnobatsembelit1=Button(frem2, width=40, pady=30, text="Lactulax Sirup 60 ml \n\nLactulax mengandung lactulose \nyang dapat membantu untuk melunakkan feses \npada usus besar sehingga lebih mudah \ndikeluarkan \n\nRp80.000/ 1 pcs", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=Lactulax).place(x=80, y=200)
    btnobatsembelit2=Button(frem2, width=40, pady=30, text="Microlax 5 ml \n\nObat ini mengandung \nsorbitol, PEG 400, dan natrium lauril sulfoasetat \nGabungan dari bahan tersebut dapat menurunkan \ntegangan feses sekaligus \nmenyerap air ke dalam usus besar \n\nRp21.000/ 1 pcs", font=("times new roman", 20, "bold"),bg='green', fg='white', border=0, command=Microlax).place(x=850, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=pencernaan).place(x=85, y=700)

#obatsembelit
def Lactulax():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN============= \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Sembelit \nObat: Lactulax \nHarga: Rp80.000/ 1 pcs \n'

    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['sembelit'],
    'Obat Yang Dibeli': ['Lactulax'],
    'Harga':['Rp80.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def Microlax():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Sembelit \nObat: Microlax \nRp21.000/ 1 pcs \n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Sembelit'],
    'Obat Yang Dibeli': ['Microlax'],
    'Harga':['Rp21.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

#diare
def diare():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Diare", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btnobatdiare1=Button(frem2, width=40, pady=30, text="Diapet \n\nObat ini mengandung ekstrak \ndaun jambu biji \nyang memang sudah terkenal efektif untuk \nmengatasi diare \n\nRp3.000/ 1 pcs",font=("times new roman", 20, "bold"), bg='darkgreen', fg='white', border=0, command=Diapet).place(x=80, y=200)
    btnobatdiare2=Button(frem2, width=40, pady=30, text="Oralit \n\nOralit berguna untuk \nterapi rehidrasi oral yang diberikan untuk \nmencegah atau mengatasi kehilangan\n cairan dan elektrolit \nakibat diare \n\nRp1.000/ 1 pcs",font=("times new roman", 20, "bold"), bg='green', fg='white', border=0, command=Oralit).place(x=850, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=pencernaan).place(x=85, y=700)

#obatdiare
def Diapet():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN============= \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Diare \nObat: Diapet \nHarga: Rp3.000/ 1 pcs \n'

    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Diare'],
    'Obat Yang Dibeli': ['Diapet'],
    'Harga':['Rp3.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def Oralit():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============\nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Diare \nObat: Oralit \nRp1.000/ 1 pcs \n======================================'

    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Diare'],
    'Obat Yang Dibeli': ['Oralit'],
    'Harga':['Rp1.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)


"""==================================CODINGAN PENYAKIT DALAM================================"""
def sdalam():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Pilih Salah Satu", bd=30, relief=RIDGE
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=488, pady=4)
    heading2.place(x=10, y=1)

    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)

    btnbatuk2=Button(frem2, width=15, text="Kolesterol", bg='#ff007f', fg='white',font=("times new roman", 40, "bold"), relief=RAISED, padx=1, pady=10, command=kolesterol).place(x=100, y=200)
    btnbatuk2=Button(frem2, width=15, text="Hepatitis", bg='#ff007f', fg='white',font=("times new roman", 40, "bold"), relief=RAISED, padx=1, pady=10, command=hepatitis).place(x=950, y=200)
    btnbatuk3=Button(frem2, width=25, text="Angina Pectoris (Angin duduk)", bg='#ff007f', fg='white',font=("times new roman", 30, "bold"), relief=RAISED, padx=1, pady=10, command=anginduduk).place(x=450, y=400)
    btnsebelum=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=keluhan2).place(x=85, y=700)
def kolesterol():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Kolesterol ", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btndisuria1=Button(frem2, width=40, pady=30, text="Simvastatin Kf 20mg\n-\nHarga: Rp8.000/strip (10 Tablet)",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=obtkoles).place(x=70, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sdalam).place(x=85, y=700)

def anginduduk():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Angin Duduk ", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btndisuria1=Button(frem2, width=40, pady=30, text="Coralan (Ivabradine HCL) 5mg\n-\nHarga: Rp72.000/5 Tablet",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=obtanginduduk).place(x=70, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sdalam).place(x=85, y=700)

def hepatitis():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron2)
    bekgron.place(x=0, y=5)

    heading2=Label(frem2, text="Rekomendasi Obat Hepatitis ", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 50, "bold"), padx=389, pady=4)
    heading2.place(x=10, y=1)
    
    hedingnama1=Label(frem2, text=f"Nama : {nama_var.get()} \nUsia : {umur_var.get()}", fg='#ff007f', bg='#FFF0F5', font=('Aria', 20, 'bold'))
    hedingnama1.place(x=680, y=710)
    btndisuria1=Button(frem2, width=35, pady=30, text="Hepatitis C\n\nCopegus 200mg Tablet-botol\n\nHarga: Rp300.000/botol (42 Tablet)",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=obthepac).place(x=70, y=480)
    btndisuria=Button(frem2, width=35, pady=30, text="Hepatitis B\n\nHepsera Adefovir Dipivoxil\nDewasa (18-65)th 1 kali sehari\n\nHarga: Rp500.000/botol (30 Tablet)",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=obthepab1).place(x=70, y=200)
    btndisuria2=Button(frem2, width=40, pady=30, text="Hepatitis B\n\nHeplav Lamivudine\nDewasa (18-65)th 1 kali sehari\n\nHarga: Rp200.000/botol (30 Tablet)",font=("times new roman", 20, "bold"), bg='red', fg='white', border=0, command=obthepab2).place(x=740, y=200)
    btnkembali1=Button(frem2, width=10, pady=10, text="Kembali",font=('aria', 20, 'bold'), bg='red', fg='white', border=0, command=sdalam).place(x=85, y=700)



#obatnyahepatitis==================================================
def obthepac():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Hepatitis C \nObat: Copegus 200mg Tablet-botol \nHarga: Rp300.000/botol (42 Tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Hepatitis C'],
    'Obat Yang Dibeli': ['Copegus'],
    'Harga':['Rp300.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obthepab1():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Hepatitis B \nObat: Hepsera Adefovir Dipivoxil \nHarga: Rp500.000/botol (30 Tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Hepatitis B'],
    'Obat Yang Dibeli': ['Hepsera Adefovir'],
    'Harga':['Rp500.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
def obthepab2():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Hepatitis B \nObat: Heplav lamivudine \nHarga: Rp200.000/botol (30 Tablet)\n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Hepatitis B'],
    'Obat Yang Dibeli': ['Heplav'],
    'Harga':['Rp200.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)
#obatnyakolesterol=================================================
def obtkoles():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=150)
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Kolesterol \nObat: Simvastatin Kf 20mg \nHarga: Rp8.000/Strip(10 tablet) \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Kolesterol'],
    'Obat Yang Dibeli': ['Simvastatin'],
    'Harga':['Rp8.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)

def obtanginduduk():
    frem2=Frame(apot, width=1525, height=1500, bg="white")
    frem2.place(x=1, y=1)
    bekgron=Label(frem2, image=imgbekgron3)
    bekgron.place(x=0, y=10)

    heading2=Label(frem2, text="Silahkan Selesaikan Pembayaran Di Kasir", bd=30
                        , bg="#FFB6C1", fg="#ff007f", font=("times new roman", 40, "bold"), padx=369, pady=4)
    heading2.place(x=10, y=1)
    
    msgs = f'============STRUK PEMBAYARAN=============    \nNama : {nama_var.get()} \nUsia :{umur_var.get()}\n'
    msgs2 = f'Keluhan : Angin Duduk \nObat: Coralan (Ivabradine HCL) 5mg \nHarga: Rp72.000/5 tablet \n======================================'
    namanye=nama_var.get()
    umoer=umur_var.get()    
    data = {
    'Nama': [namanye],
    'Usia': [umoer],
    'Keluhan': ['Angin Duduk'],
    'Obat Yang Dibeli': ['Coralan (Ivabradine Hcl)'],
    'Harga':['Rp72.000']
    ,
    'Tanggal Pembelian':[datetime_object]
    }
    dta = pd.DataFrame(data)

    dta.to_csv('datayangbeli.csv', mode='a', index=False, header=False)
    showinfo('struk', msgs + "\n" + msgs2)
    def print(txt):
        print_item=tempfile.mktemp('.txt')
        open(print_item, 'w').write(txt)
        os.startfile(print_item, 'print')
    printbutton=Button(frem2, width=20, pady=10, text="Print Struk pembelian", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0,command=lambda:print(msgs+'\n'+msgs2)).place(x=605, y=350)
    
    btnselesai=Button(frem2, width=20, pady=10, text="Selesai", font=('Times New Roman', 20, 'bold'), bg='red', fg='white', border=0, command=home).place(x=340, y=700)
    btntambah=Button(frem2, width=20, pady=10, text="Tambah", font=('Times New Roman', 20, 'bold'), bg='green', fg='white', border=0, command=keluhan).place(x=890, y=700)




apot.mainloop()
"""=========================================Akhir Codingan projek============================================="""

