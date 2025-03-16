import tkinter # type: ignore
import customtkinter # type: ignore
import pygame # type: ignore
from PIL import Image, ImageTk # type: ignore
from threading import Thread # type: ignore
import time # type: ignore
import math # type: ignore

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title('Music Player')
root.geometry('400x480')
pygame.mixer.init()

list_of_songs = ['music/Jonas Kolberg - Bright Horizon.mp3', 'music/sza-kill-bill.mp3']
list_of_covers = ['img/Jonas Kolberg - Bright Horizon.png', 'img/sza-kill-bill.png']
n = 0
is_playing = False  # Play/Stop ауыстыру үшін


def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2 = image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.19, rely=.06)

    stripped_string = song_name.split('/')[-1][:-4]  # Файл атауын дұрыс алу
    song_name_label = tkinter.Label(text=stripped_string, bg='#222222', fg='white', font=("Arial", 12))
    song_name_label.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)  # Орнын реттеу


def progress():
    a = pygame.mixer.Sound(list_of_songs[n])
    song_len = a.get_length() * 3
    for i in range(0, math.ceil(song_len)):
        time.sleep(.3)
        progressbar.set(pygame.mixer.music.get_pos() / 1000000)


def threading():
    t1 = Thread(target=progress)
    t1.start()


def play_music():
    global n, is_playing
    if is_playing:
        pygame.mixer.music.stop()
        play_button.configure(text="Play")
        is_playing = False
    else:
        threading()
        song_name = list_of_songs[n]
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(slider.get())
        get_album_cover(song_name, n)
        play_button.configure(text="Stop")
        is_playing = True


def skip_forward():
    global n, is_playing
    n = (n + 1) % len(list_of_songs)  # Цикл бойынша ауыстыру
    play_music()


def skip_back():
    global n, is_playing
    n = (n - 1) % len(list_of_songs)
    play_music()


def volume(value):
    pygame.mixer.music.set_volume(float(value))


# Buttons
play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=2)
skip_f.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_back, width=2)
skip_b.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

# Volume control
vol_icon = tkinter.Label(root, text="🔊", font=("Arial", 14))  # Суреттің орнына эмодзи
vol_icon.place(relx=0.2, rely=0.78, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=210)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#32a85a', width=250)
progressbar.place(relx=.5, rely=.85, anchor=tkinter.CENTER)

root.mainloop()
