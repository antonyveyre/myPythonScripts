import tkinter as tk, re, datetime


root = tk.Tk()
txt = []
v = []
def replClip(buffer):
    root.clipboard_clear()
    root.clipboard_append(buffer)

def main():
    
    dates = re.findall('"\d{13}\"',root.clipboard_get())
    
    if (dates==[]):
        dates = re.findall('\d{13}',root.clipboard_get())
    
    for dat in dates:
        i = dates.index(dat)
        tostring = str(int(dat.strip("\"")))
        lbl = str(int(dat[:-3].strip("\"")))
        w = tk.Label(root,text= lbl)
        w.grid(row = dates.index(dat),column=1)
        txt.append(datetime.datetime.fromtimestamp(float(tostring[:-3])).strftime("%d/%m/%Y %H:%M:%S"))
        v.append(tk.Button(root,text=str(txt[i])))
        v[i].configure(command = lambda x=str(txt[i]) : replClip(x))   
        v[i].grid(row=dates.index(dat),column=2)
        
    root.mainloop()

if __name__ == '__main__':
    main()
