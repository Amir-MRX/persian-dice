import customtkinter as ctk
from random import randint



#handel window window
root = ctk.CTk()
root.geometry("439x481")
root.config(bg='#0B2042')
root.resizable(0,0)
root.wm_title("Dice")

setmode = ctk.set_default_color_theme("dark-blue")

#handel gui
frame = ctk.CTkFrame(
    master=root,
    width=220.76,
    height=33.96,
    fg_color='#0000cc', # #E34F4F
    corner_radius=5)

frame.place(relx=.25, y=25)

info = ctk.CTkLabel(
    master=frame,
    text="برنامه ی ریختن تاس",
    # text_color="black",
    font=('Vazirmatn-Light.ttf', 16))

info.place(relx=0.20, rely=0.01)

nbd = ctk.CTkLabel(
    master=root,
    text="ﺪﯿﻨﻛ  ﺩﺭﺍﻭ ﺍﺭ ﺱﺎﺗ ﺩﺍﺪﻌﺗ ",
    text_color="white",
    font=('Vazirmatn-Light.ttf', 15),
    # fg_color='#0B2042'
    bg_color="#001a4d",
    )

nbd.place(relx=0.1, rely=0.3)

nbe = ctk.CTkEntry(
    master=root,
    text_color='black',
    # fg_color='#8B8B8B',
    corner_radius=5,
    width=361,
    height=44,
    placeholder_text="کنید وارد تعداد را تاس ",
    placeholder_text_color="#BABABA")

nbe.place(relx=0.1, rely=0.38)

nbs = ctk.CTkLabel(
    master=root,
    text="",
    text_color="white",
    font=('Vazirmatn-Light.ttf', 36),
    # fg_color='#0B2042'
    bg_color="#0b2042"
    )

nbs.place(relx=0.48, rely=0.55)

#handel opration
def handler():
    global random_number
    random_number = randint(1, 6)
    value = nbe.get()

    if value == '1' or value == '2':
        if value == '1':
            nbs.configure(text=str(random_number), text_color='white', font=('Vazirmatn-Light.ttf', 36))
            nbs.place(relx=0.48, rely=0.6)
        
        elif value == '2':
            random_number2 = randint(1, 6)
            nbs.configure(
                text=str(random_number) + ',' + str(random_number2),
                text_color='white',
                font=('Vazirmatn-Light.ttf', 36),
                )
            
            nbs.place(relx=0.45, rely=0.6)
    
    elif value == "":
        nbs.configure(text="")
    
    else:
        nbs.configure(
            text="حداکثر 2 تاس",
            text_color='red',
            font=('Vazirmatn-Bold.ttf', 18))
        
        nbs.place(relx=0.38, rely=0.65)

gbn = ctk.CTkButton(
    master=root,
    text="ﻦﺘﺨﯾﺭ ﺱﺎﺗ ",
    width=186.45,
    height=41,
    text_color='black',
    # fg_color='#50C370',
    font=('Vazirmatn-Bold.ttf', 18),
    # hover_color='#96FFB3',
    command=handler)

gbn.place(relx=0.3, rely=0.75)

root.bind('q', quit)


root.mainloop()
