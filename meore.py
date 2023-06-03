import tkinter as tk
from tkinter import *


#მეორე ცდა იყო და ფაილს მეორე მაგიტომ ჰქვია

root = tk.Tk()
root.title("კალკულატორი ორი")

gamotvla=""

def mimmatebeli(ricxvi):
    global gamotvla
    gamotvla += str(ricxvi)
    gamomtani.delete(1.0, "end")
    gamomtani.insert(1.0, gamotvla)
    

def gamsxvavebeli():
    global gamotvla
    try:
        resultati=str(eval(gamotvla))
        gamotvla=resultati
        gamomtani.delete(1.0, "end")
        gamomtani.insert(1.0, resultati)
    except:
        wamshleli()
        gamomtani.insert(1.0, "Errori")
        pass


def mteli():
    global gamotvla
    print(gamotvla)
    mteli = gamotvla
    mteliinti=int(float(mteli))
    print(gamotvla)
    gamomtani.delete(1.0, "end")
    gamomtani.insert(1.0, mteliinti)
    gamotvla=str(mteliinti)
    

def wamshleli():
    global gamotvla
    gamotvla=""
    gamomtani.delete(1.0, END)
    

gamomtani = tk.Text(root, height=2, width=16, font=("Arial", 24))
gamomtani.grid(columnspan=5)

k1=tk.Button(text="+",height=5, width=10, command=lambda: mimmatebeli("+"))
k1.grid(row=2,column=1)

k2=tk.Button(text="-",height=5, width=10, command=lambda: mimmatebeli("-"))
k2.grid(row=2,column=2)

k3=tk.Button(text="=",height=5, width=10, command= gamsxvavebeli)
k3.grid(row=2,column=3)

k4=tk.Button(text="წაშლა",height=5, width=10, command=wamshleli)
k4.grid(row=2,column=4)

k5=tk.Button(text="1",height=5, width=10, command=lambda: mimmatebeli("1"))
k5.grid(row=3,column=1)

k6=tk.Button(text="2",height=5, width=10, command=lambda: mimmatebeli("2"))
k6.grid(row=3,column=2)

k7=tk.Button(text="3",height=5, width=10, command=lambda: mimmatebeli("3"))
k7.grid(row=3,column=3)

k8=tk.Button(text="*",height=5, width=10, command=lambda: mimmatebeli("*"))
k8.grid(row=3,column=4)

k9=tk.Button(text="4",height=5, width=10, command=lambda: mimmatebeli("4"))
k9.grid(row=4,column=1)

k10=tk.Button(text="5",height=5, width=10, command=lambda: mimmatebeli("5"))
k10.grid(row=4,column=2)

k11=tk.Button(text="6",height=5, width=10, command=lambda: mimmatebeli("6"))
k11.grid(row=4,column=3)

k12=tk.Button(text="/",height=5, width=10, command=lambda: mimmatebeli("/"))
k12.grid(row=4,column=4)

k13=tk.Button(text="7",height=5, width=10, command=lambda: mimmatebeli("7"))
k13.grid(row=5,column=1)

k14=tk.Button(text="8",height=5, width=10, command=lambda: mimmatebeli("8"))
k14.grid(row=5,column=2)

k15=tk.Button(text="9",height=5, width=10, command=lambda: mimmatebeli("9"))
k15.grid(row=5,column=3)

k16=tk.Button(text="მთელი",height=5, width=10, command=mteli)
k16.grid(row=5,column=4)







mainloop()