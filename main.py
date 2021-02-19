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
    app.title("Music Notation")
    app.geometry("1280x720")
    app.resizable(False, False)

    app.rowconfigure(0, minsize=50, weight=1)
    app.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=50, weight=1)

    # Time Signatures --------------------------------------------------------------------------------------------------

    timesig_buttons = ["4/4", "3/4", "5/4", "2/4", "12/8", "6/8"]

    app.rowconfigure(1, minsize=50, weight=1)
    app.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=50, weight=1)

    lbl_timesig = tkinter.Label(master=app, text="Time Signatures:", width=80, height=4)
    lbl_timesig.config(font=("Arial", 24))
    lbl_timesig.grid(row=1, column=0, padx=5)

    for i in range(len(timesig_buttons)):
        btn = tkinter.Button(master=app, text=timesig_buttons[i], width=200, height=4)
        btn.grid(row=1, column=i+1, padx=5)

    # Note Lengths -----------------------------------------------------------------------------------------------------

    note_length_buttons = ["1/16", "1/8", "1/4", "1/2", "1"]

    app.rowconfigure(2, minsize=50, weight=2)
    app.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)

    lbl_note = tkinter.Label(master=app, text="Note Lengths:", width=80, height=4)
    lbl_note.config(font=("Arial", 24))
    lbl_note.grid(row=2, column=0, padx=5)

    for i in range(len(note_length_buttons)):
        btn = tkinter.Button(master=app, text=note_length_buttons[i], width=200, height=4)
        btn.grid(row=2, column=i+1, padx=5)

    # Key Signatures ---------------------------------------------------------------------------------------------------

    keysig_buttons = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

    app.rowconfigure(3, minsize=50, weight=3)
    app.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], minsize=50, weight=1)

    lbl_note = tkinter.Label(master=app, text="Key Signatures:", width=80, height=4)
    lbl_note.config(font=("Arial", 20))
    lbl_note.grid(row=3, column=0, padx=5)

    for i in range(len(keysig_buttons)):
        btn = tkinter.Button(master=app, text=keysig_buttons[i], width=200, height=4)
        btn.grid(row=3, column=i+1, padx=5)

    # -----------------------------------------------------------------------------------------------------------------

    app.mainloop()

