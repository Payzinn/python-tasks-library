from tkinter import *
import pytube as youtube
from tkinter import messagebox
import threading
from tkinter import ttk
import time
root = Tk()
root.geometry('940x480')
root.resizable(True, False)
root.title('Скачивание видео с YouTube')
root.config(bg='#7A97FB')

first_link = StringVar()

def download_thread():
    thread = threading.Thread(target=download)
    thread.start()

def info_thread():
    thread = threading.Thread(target=update_video_information)
    thread.start()

def reset():
    first_link.set('')
    form_label_duration.config(text='Длительность видео:')
    form_label_name.config(text='Название видео:')
    form_label_weight.config(text='Вес видео:')

def Exit():
    root.destroy()

def download():
    start_progressbar()
    try:
        ytlink = first_link.get()
        youtubelink = youtube.YouTube(ytlink)
        video = youtubelink.streams.get_highest_resolution()
        video.download()
        messagebox.showinfo("Готово", "Загрузка видео завершена")
    except Exception as e:
        messagebox.showerror('Ошибка', 'Ссылка нерабочая или возникла другая проблема:\n{}'.format(e))
    finally:
        stop_progressbar()

def audio_download():
    start_progressbar()
    try:
        ytlink = first_link.get()
        youtubelink = youtube.YouTube(ytlink)
        audio = youtubelink.streams.get_audio_only()
        audio.download()
        messagebox.showinfo("Готово", "Загрузка аудио завершена")
    except Exception as e:
        messagebox.showerror('Ошибка', 'Ссылка нерабочая или возникла другая проблема:\n{}'.format(e))
    finally:
        stop_progressbar()

def get_video_weight():
    form_label_weight.config(text="Загрузка.")
    time.sleep(0.5)
    form_label_weight.config(text="Загрузка..")
    time.sleep(0.5)
    form_label_weight.config(text="Загрузка...")
    try:
        ytlink = first_link.get()
        youtubelink = youtube.YouTube(ytlink)
        video_stream = youtubelink.streams.get_highest_resolution()
        video_weight = video_stream.filesize_mb
        form_label_weight.config(text="Вес видео: {:.2f} Мб".format(video_weight))
    except Exception as e:
        form_label_weight.config(text="Произошла ошибка в получении веса видео")
        print('Произошла ошибка: {}'.format(e))

def get_video_info():
    try:
        ytlink = first_link.get()
        youtubelink = youtube.YouTube(ytlink)
        length_in_seconds = youtubelink.length
        minutes = length_in_seconds // 60
        seconds = length_in_seconds % 60
        video_title = youtubelink.title
        form_label_duration.config(text='Длительность видео: {} минут {} секунд'.format(minutes, seconds))
        form_label_name.config(text="Название видео: {}".format(video_title))
    except Exception as e:
        form_label_duration.config(text="Ошибка в получении длительности видео")
        form_label_name.config(text="Ошибка в получении названия видео")
        print('Произошла ошибка: {}'.format(e))

def update_video_information(event=None):
    get_video_info()
    get_video_weight()

def paste_from_clipboard():
    first_entry.event_generate('<<Paste>>')
    root.update_idletasks()
    info_thread()

def start_progressbar():
    progress.start(10)

def stop_progressbar():
    progress.stop()

progressbar_container = Frame(root)
progressbar_container.place(x = 10, y = 420)
progress = ttk.Progressbar(root, orient='horizontal', length = 100, mode='indeterminate')
progress.pack()

form_label = Label(root, text='---Загрузка видео с YouTube---', font=('Jost', 20, 'bold'), bg='#7A97FB')
form_label.pack(pady=15)

form_label_first = Label(root, text='Ссылка на видео:', font=('Jost', 20, 'bold'), bg='#7A97FB')
form_label_first.place(x=10, y=100)

first_entry = Entry(root, textvariable=first_link, font=('Jost', 20))
first_entry.place(x=260, y=100)
first_entry.bind('<Return>', lambda event: info_thread())
first_entry.bind('<Control-v>', lambda event: info_thread())

form_label_duration = Label(root, text='Длительность видео:', font=('Jost', 20), bg='#7A97FB')
form_label_duration.place(x=10, y=250)

form_label_name = Label(root, text='Название видео:', font=('Jost', 20), bg='#7A97FB')
form_label_name.place(x=10, y=320)

form_label_weight = Label(root, text='Вес видео:', font=('Jost', 20), bg='#7A97FB')
form_label_weight.place(x=10, y=360)

paste_button = Button(root, text='Вставить из буфера обмена',font=('Jost',10), command=paste_from_clipboard)
paste_button.place(x=340, y=190)

full_download_button = Button(root, text='Скачать', font=('Jost', 10), bd=2, command=download_thread)
full_download_button.pack()
full_download_button.place(x=420, y=150)

audio_download_button = Button(root, text='Скачать только аудио', font=('Jost', 10), bd=2, command=audio_download)
audio_download_button.place(x=280, y=150)

clear_button = Button(root, text='Очистить', font=('Jost', 10), bd=5, command=reset)
clear_button.place(x=640, y=102)

#exit_button = Button(root, text='Выход', font=('Jost', 10, 'italic'), bd=2, command=Exit)
#exit_button.place(x=420, y=230)

root.mainloop()