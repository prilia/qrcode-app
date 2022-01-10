from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyqrcode
import validators
import time

###############################################
# Constants
# Limit url length
url_max_len = 250
# Window frame H,W
geometry_val = '800x800'
# Color to use
color_bg = 'white'
###############################################

# Create new tkinter object
ws = Tk()
ws.title("Create QR-code Naya-DS-Course")
ws.geometry(geometry_val)
ws.config(bg=color_bg)

# Define error level
error_level = StringVar()
Label(ws, text="Choose error correction level", bg=color_bg).pack()
Radiobutton(ws, text="L - 7%", bg=color_bg, variable=error_level, value='L', state=NORMAL).pack()
Radiobutton(ws, text="M - 15%", bg=color_bg, variable=error_level, value='M').pack()
Radiobutton(ws, text="Q - 25%", bg=color_bg, variable=error_level, value='Q').pack()
Radiobutton(ws, text="H - 30%", bg=color_bg, variable=error_level, value='H').pack()
error_level.set('L')

def generate_QR():
    url = user_input.get()
    if len(url) == 0:
        messagebox.showwarning('warning', 'All Fields are Required!')
    elif validators.domain(url) or validators.url(url):
        global qr, img
        qr = pyqrcode.create(user_input.get(), error=error_level.get())
        img = BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showwarning('warning', 'Not Valid URL!')

    try:
        display_code()
    except:
        pass

def clear_QR():
    img_lbl.config(image='')
    user_input.set('')
    output.config(text='')

def display_code():
    img_lbl.config(image=img)
    output.config(text="QR code of " + user_input.get())

def limit_url_len(*args):
    value = user_input.get()
    if len(value) > url_max_len:
        user_input.set(value[:url_max_len])
        messagebox.showwarning('warning', 'Max url length is ' + str(url_max_len))

def savefile():
    qr.svg('qr_code_' + str(time.time()) + '.svg')
    # filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    # if not filename:
    #     return
    # edge.save(filename)

lbl = Label(
    ws,
    text="Enter message or URL",
    bg=color_bg
)
lbl.pack()

user_input = StringVar()
user_input.trace('w', limit_url_len)
entry = Entry(
    ws,
    textvariable=user_input,
    width=20
)
entry.pack(padx=5)

button = Button(
    ws,
    text="generate_QR",
    width=15,
    command=generate_QR
)
button.pack(pady=5)

button = Button(
    ws,
    text="Clear",
    width=15,
    command=clear_QR
)
button.pack(pady=10)

button = Button(ws, text="save as", command=savefile)
button.pack(pady=10)

img_lbl = Label(
    ws,
    bg=color_bg
)
img_lbl.pack()

output = Label(
    ws,
    text="",
    bg=color_bg
)
output.pack()

ws.mainloop()