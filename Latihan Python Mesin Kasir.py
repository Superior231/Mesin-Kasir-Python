from tkinter import *
from tkinter import messagebox

app = Tk()

bakso = StringVar()
mie = StringVar()
esteh = StringVar()
aqua = StringVar()
texttotal = StringVar()
textuang = StringVar()
total = 0


def tombolSpindiklik():
    global bakso, mie, esteh, aqua, texttotal, total
    hargabakso = int(bakso.get())*12000
    hargamie = int(mie.get())*10000
    hargaesteh = int(esteh.get())*3000
    hargaaqua = int(aqua.get())*500
    total = hargabakso + hargamie + hargaesteh + hargaaqua
    texttotal.set(str(total))

def totaldiklik():
    uang = int(textuang.get())

    if uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message='Kembalian Anda Sebesar Rp.{}'.format(str(kembalian)))
        
    else:
        messagebox.showwarning(message='Maaf Uang Anda Tidak Cukup')

def clearklik():
    bakso.set('0')
    mie.set('0')
    esteh.set('0')
    aqua.set('0')
    texttotal.set('0')
    textuang.set('0')



app.geometry('450x550')
app.configure(bg='#050a30')


Label(app, text='WARUNG BAKSO PAK KUMIS', bg='#050a30', foreground='white', font='arial 10 bold').place(x=140,y=30)
Label(app, text='1. Bakso', bg='#050a30', foreground='white', font='arial 10 bold').place(x=40,y=100)
Label(app, text='2. Mie Ayam', bg='#050a30', foreground='white', font='arial 10 bold').place(x=40,y=150)
Label(app, text='3. Es Teh', bg='#050a30', foreground='white', font='arial 10 bold').place(x=40,y=200)
Label(app, text='4. Aqua Gelas', bg='#050a30', foreground='white', font='arial 10 bold').place(x=40,y=250)


Label(app, text='Rp. 12,000', bg='#050a30', foreground='white', font='arial 10 bold').place(x=190,y=100)
Label(app, text='Rp. 10,000', bg='#050a30', foreground='white', font='arial 10 bold').place(x=190,y=150)
Label(app, text='Rp. 3,000', bg='#050a30', foreground='white', font='arial 10 bold').place(x=190,y=200)
Label(app, text='Rp. 500', bg='#050a30', foreground='white', font='arial 10 bold').place(x=190,y=250)


Spinbox(app, from_=0, to=100, width=5, font='arial 10 bold', textvariable=bakso, command=tombolSpindiklik).place(x=320,y=100)
Spinbox(app, from_=0, to=100, width=5, font='arial 10 bold', textvariable=mie, command=tombolSpindiklik).place(x=320,y=150)
Spinbox(app, from_=0, to=100, width=5, font='arial 10 bold', textvariable=esteh, command=tombolSpindiklik).place(x=320,y=200)
Spinbox(app, from_=0, to=100, width=5, font='arial 10 bold', textvariable=aqua, command=tombolSpindiklik).place(x=320,y=250)


Label(app, text='Masukkan Uang Anda', bg='#050a30', foreground='white').place(x=40,y=350)
Entry(app, textvariable=textuang).place(x=40,y=380)


Label(app, text='Rp.', bg='#050a30', foreground='white', font='arial 14 bold').place(x=280,y=370)
Label(app, textvariable=texttotal, bg='#050a30', foreground='white', font='arial 14 bold').place(x=315,y=370)


Button(app, text='TOTAL', bg='green', width=20, font='arial 10 bold', foreground='white', command=totaldiklik).place(x=40,y=450)
Button(app, text='CLEAR', bg='#eeede7', width=20, font='arial 10 bold', foreground='black', command=clearklik).place(x=240,y=450)

app.mainloop()
