'''
▀█████████▄   ▄██████▄   ▄█           ███      ▄███████▄  
  ███    ███ ███    ███ ███       ▀█████████▄ ██▀     ▄██ 
  ███    ███ ███    ███ ███          ▀███▀▀██       ▄███▀ 
 ▄███▄▄▄██▀  ███    ███ ███           ███   ▀  ▀█▀▄███▀▄▄ 
▀▀███▀▀▀██▄  ███    ███ ███           ███       ▄███▀   ▀ 
  ███    ██▄ ███    ███ ███           ███     ▄███▀       
  ███    ███ ███    ███ ███▌    ▄     ███     ███▄     ▄█ 
▄█████████▀   ▀██████▀  █████▄▄██    ▄████▀    ▀████████▀   v0.1
                        ▀                                 
boltz was possible only due to spotify_dl,
https://github.com/SathyaBhat/spotify-dl,
'''
import tkinter as tk
from tkinter import messagebox
from src.boltz import *
import sys
import threading
def main():
  
  window = tk.Tk(className="boltz")
  title = tk.Label(window, text = "Your spotify pl: ", font=('Arial',30))
  url_entry = tk.Entry(window, width=300, font=('Arial',18))
  button = tk.Button(window, text = "convert", command=lambda: threading.Thread(target=bolt.download, args=(url_entry.get(),window,)).start())
  title.pack()
  url_entry.pack()
  url_entry.insert(0,"https://open.spotify.com/playlist/..")
  button.pack()
  bolt = boltz()
  window.geometry("840x470")
  window.mainloop()

    

if __name__ == '__main__':
  main()
  
    