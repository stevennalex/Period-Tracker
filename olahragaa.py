import webbrowser
import tkinter as tk

def open_youtube_link():
    youtube_link = "https://www.youtube.com/"
    webbrowser.open(youtube_link)

# Fungsi yang dijalankan saat tombol diklik
def on_button_click():
    open_youtube_link()
