# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pydub import AudioSegment
from pydub.playback import play
import tkinter
import os


def play_sound():
    c_note = AudioSegment.from_mp3(os.getcwd() + "\\sound\\C4.mp3")
    e_note = AudioSegment.from_mp3(os.getcwd() + "\\sound\\E4.mp3")
    g_note = AudioSegment.from_mp3(os.getcwd() + "\\sound\\G4.mp3")
    as_note = AudioSegment.from_mp3(os.getcwd() + "\\sound\\As5.mp3")
    b_note = AudioSegment.from_mp3(os.getcwd() + "\\sound\\B5.mp3")
    d_note = AudioSegment.from_mp3(os.getcwd() + "\\sound\\D5.mp3")
    ghigh_note = AudioSegment.from_mp3(os.getcwd() + "\\sound\\G5.mp3")

    mixed_audio1 = c_note.overlay(e_note).overlay(g_note).overlay(as_note)
    play(mixed_audio1)

    mixed_audio2 = g_note.overlay(b_note).overlay(d_note).overlay(ghigh_note)
    play(mixed_audio2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = tkinter.Tk()
    app.geometry("500x200")

    button = tkinter.Button(app, height=3, width=12, text="Play", command=play_sound)
    button.pack()

    button2 = tkinter.Button(app, height=3, width=12, text="Exit", command=quit)
    button2.pack()

    app.mainloop()

