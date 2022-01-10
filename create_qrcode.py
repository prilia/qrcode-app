from tkinter import *
from tkinter import messagebox
import pyqrcode
import validators


# Limit url length
url_max_len = 50

# Create new tkinter object
ws = Tk()
ws.title("Create QR-code Naya-DS-Course")
ws.geometry('800x800')
ws.config(bg='white')

# Define error level
error_level = StringVar()
Label(ws, text="Choose error correction level", bg='white').pack()
Radiobutton(ws, text="L - 7%", bg='white', variable=error_level, value='L', state=NORMAL).pack()
Radiobutton(ws, text="M - 15%", bg='white', variable=error_level, value='M').pack()
Radiobutton(ws, text="Q - 25%", bg='white', variable=error_level, value='Q').pack()
Radiobutton(ws, text="H - 30%", bg='white', variable=error_level, value='H').pack()
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
    output.config(text='')

def display_code():
    img_lbl.config(image=img)
    output.config(text="QR code of " + user_input.get())

def limit_url_len(*args):
    value = user_input.get()
    if len(value) > url_max_len:
        user_input.set(value[:url_max_len])
        messagebox.showwarning('warning', 'Max url length is ' + str(url_max_len))

lbl = Label(
    ws,
    text="Enter message or URL",
    bg='white'
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

img_lbl = Label(
    ws,
    bg='white'
)
img_lbl.pack()

output = Label(
    ws,
    text="",
    bg='white'
)
output.pack()

ws.mainloop()
