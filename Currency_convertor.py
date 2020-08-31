from tkinter import *
from tkinter import ttk

def convert():
    g=float(en.get())
    From=f.get()
    rate=0.0
    To=t.get()
    if From == 'USD':
        if To == 'INR':
            rate=73.1285
            con.set(g*rate)
        elif To == 'EUR':
            rate=0.839877
            con.set(rate*g)
        elif To == 'JPY':
            rate=105.36
            con.set(rate*g)
        elif To == 'CHF':
            rate=0.90
            con.set(rate*g)
        elif To == 'GBP':
            rate=0.75
            con.set(rate*g)
        elif To == 'CAD':
            rate=1.32512
            con.set(rate*g)
        elif To == 'ZAR':
            rate=17.3137
            con.set(rate*g)
    elif From == 'INR':
        if To == 'USD':
            rate=0.0134129
            #rate=1/73.1285
            con.set(rate*g)
        elif To == 'EUR':
            rate=0.01123292
            con.set(rate*g)
        elif To == 'JPY':
            rate=1.44094
            con.set(rate*g)
        elif To == 'CHF':
            rate=0.0121078
            con.set(rate*g)
        elif To == 'GBP':
            rate=1.00994/100
            con.set(rate*g)
        elif To == 'CAD':
            rate=0.0178376
            con.set(rate*g)
        elif To == 'ZAR':
            rate=0.230506
            con.set(rate*g)
    elif From == 'EUR':
        if To == 'USD':
            rate=1.19080
            con.set(rate*g)
        elif To == 'INR':
            rate=88.6762
            con.set(rate*g)
        elif To == 'JPY':
            rate=125.548
            con.set(rate*g)
        elif To == 'CHF':
            rate=1.0788
            con.set(rate*g)
        elif To == 'GBP':
            rate=0.901491
            con.set(rate*g)
        elif To == 'CAD':
            rate=1.56382
            con.set(rate*g)
        elif To == 'ZAR':
            rate=20.4540
            con.set(rate*g)
    elif From == 'JPY':
        if To == 'USD':
            rate=0.00949082 
            con.set(rate*g)
        elif To == 'INR':
            rate=0.69
            con.set(rate*g)
        elif To == 'EUR':
            rate=0.0080 
            con.set(rate*g)
        elif To == 'CHF':
            rate=0.0086 
            con.set(rate*g)
        elif To == 'GBP':
            rate=0.0071 
            con.set(rate*g)
        elif To == 'CAD':
            rate=0.012
            con.set(rate*g)
        elif To == 'ZAR':
            rate=0.16
            con.set(rate*g)
    elif From == 'CHF':
        if To == 'USD':
            rate=1.11 
            con.set(rate*g)
        elif To == 'INR':
            rate=80.88 
            con.set(rate*g)
        elif To == 'EUR':
            rate=0.93 
            con.set(rate*g)
        elif To == 'JPY':
            rate=116.53 
            con.set(rate*g)
        elif To == 'GBP':
            rate=0.83
            con.set(rate*g)
        elif To == 'CAD':
            rate=1.45
            con.set(rate*g)
        elif To == 'ZAR':
            rate=18.33
            con.set(rate*g)
    elif From == 'GBP':
        if To == 'USD':
            rate=1.34
            con.set(rate*g)
        elif To == 'INR':
            rate=97.63 
            con.set(rate*g)
        elif To == 'EUR':
            rate=1.12
            con.set(rate*g)
        elif To == 'JPY':
            rate=140.67 
            con.set(rate*g)
        elif To == 'CHF':
            rate=1.21
            con.set(rate*g)
        elif To == 'CAD':
            rate=1.75
            con.set(rate*g)
        elif To == 'ZAR':
            rate=22.13
            con.set(rate*g)
    elif From == 'CAD':
        if To == 'USD':
            rate=0.76
            con.set(rate*g)
        elif To == 'INR':
            rate=55.78 
            con.set(rate*g)
        elif To == 'EUR':
            rate=0.639200
            con.set(rate*g)
        elif To == 'JPY':
            rate=80.37 
            con.set(rate*g)
        elif To == 'GBP':
            rate=0.57
            con.set(rate*g)
        elif To == 'CHF':
            rate=0.69
            con.set(rate*g)
        elif To == 'ZAR':
            rate=12.64
            con.set(rate*g)
    elif From == 'ZAR':
        if To == 'USD':
            rate=0.060 
            con.set(rate*g)
        elif To == 'INR':
            rate=4.41 
            con.set(rate*g)
        elif To == 'EUR':
            rate=0.051 
            con.set(rate*g)
        elif To == 'JPY':
            rate=6.36 
            con.set(rate*g)
        elif To == 'GBP':
            rate=0.045
            con.set(rate*g)
        elif To == 'CAD':
            rate=0.079
            con.set(rate*g)
        elif To == 'CHF':
            rate=0.055
            con.set(rate*g)
        
            
        


r = Tk()
r.title("Currency Convertor")
r.geometry("450x150")
ttk.Label(r, text="Currency Convertor", background="yellow", foreground="black", font=("Times New Roman",15)).grid(row=1,column=2)
ttk.Label(r, text="Enter Amount:").grid(row=3,column=1)
ttk.Label(r, text="Converted value").grid(row=3,column=3)
con=StringVar()
ben=Button(r, text="Convert", width=15,font=("Arial",10),command=convert)
ben.grid(row=4,column=2)

en=Entry(r,width=15)
en.grid(row=4,column=1)

en1=Entry(r,textvariable=con,width=15)
en1.grid(row=4,column=3)


ttk.Label(r, text="From:", font=("Times New Roman",10)).grid(row=5,column=0, padx=10, pady=25)
v=StringVar()
f=ttk.Combobox(r, width=6, textvariable=v)

f['values']=('USD','EUR','JPY','CHF','GBP','CAD','ZAR','INR')

f.grid(row=5,column=1)
ttk.Label(r,text="To:",font=("Times New Roman",10)).grid(row=5,column=2, padx=10, pady=25)
v1=StringVar()
t=ttk.Combobox(r, width=6, textvariable=v1)

t['values']=('USD','EUR','JPY','CHF','GBP','CAD','ZAR','INR')

t.grid(row=5,column=3)
f.current()
t.current()

#b=Button(r, text="Convert", width=15, command)
r.mainloop()
