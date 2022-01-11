from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyqrcode
import validators
import time
import traceback
from pathlib import Path

###############################################
# Constants
# Limit url length
URL_MAX_LEN = 250
# Window frame H,W
GEOMETRY_VAL = '800x800'
# Color to use
COLOR_BG = 'white'
# Color to use
SAVE_TO_FOLDER = '/qrcode-files/'

GENERATE_QR_TXT = 'Generate QR'
SAVE_TO_FILE_TXT = 'Save To File'
CLEAR_TXT = 'Clear It'
###############################################

def generate_QR():
    url = user_input.get()
    if len(url) == 0:
        messagebox.showwarning('warning', 'All Fields are Required!')
    elif validators.domain(url) or validators.url(url):
        try:
            global qr, img
            qr = pyqrcode.create(user_input.get(), error=error_level.get())
            img = BitmapImage(data=qr.xbm(scale=8))
            save_button_change_state(NORMAL)
            display_code()
        except:
            pass
    else:
        messagebox.showwarning('warning', 'Not Valid URL!')

def save_button_change_state(st):
    button_save_to_file["state"] = st

def clear_QR():
    img_lbl.config(image='')
    user_input.set('')
    output.config(text='')
    save_button_change_state(DISABLED)

def display_code():
    img_lbl.config(image=img)
    output.config(text="QR code of " + user_input.get())

def limit_url_len(*args):
    value = user_input.get()
    if len(value) > URL_MAX_LEN:
        user_input.set(value[:URL_MAX_LEN])
        messagebox.showwarning('warning', 'Max url length is ' + str(URL_MAX_LEN))

def savefile():
    try:
        Path(SAVE_TO_FOLDER).mkdir(parents=True, exist_ok=True)
        filename = SAVE_TO_FOLDER + 'qr_code_' + str(time.time()) + '.svg'
        qr.svg(filename)
        messagebox.showinfo('info', 'QR code saved to file ' + str(filename))
    except Exception:
        traceback.print_exc()


# Create new tkinter object
ws = Tk()
ws.title("Create QR-code Naya-DS-Course")
ws.geometry(GEOMETRY_VAL)
ws.config(bg=COLOR_BG)

# Define error level
error_level = StringVar()
Label(ws, text="Choose error correction level", bg=COLOR_BG).pack()
Radiobutton(ws, text="L - 7%", bg=COLOR_BG, variable=error_level, value='L', state=NORMAL).pack()
Radiobutton(ws, text="M - 15%", bg=COLOR_BG, variable=error_level, value='M').pack()
Radiobutton(ws, text="Q - 25%", bg=COLOR_BG, variable=error_level, value='Q').pack()
Radiobutton(ws, text="H - 30%", bg=COLOR_BG, variable=error_level, value='H').pack()
error_level.set('L')

lbl = Label(
    ws,
    text="Enter message or URL",
    bg=COLOR_BG
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
    text=GENERATE_QR_TXT,
    width=15,
    command=generate_QR
)
button.pack(pady=5)

button = Button(
    ws,
    text=CLEAR_TXT,
    width=15,
    command=clear_QR
)
button.pack(pady=10)

button_save_to_file = Button(ws, text=SAVE_TO_FILE_TXT, command=savefile)
button_save_to_file.pack(pady=10)
save_button_change_state(DISABLED)

img_lbl = Label(
    ws,
    bg=COLOR_BG
)
img_lbl.pack()

output = Label(
    ws,
    text="",
    bg=COLOR_BG
)
output.pack()

ws.mainloop()