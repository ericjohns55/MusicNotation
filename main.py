# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pydub import AudioSegment
from pydub.playback import play
from PIL import Image, ImageTk
import tkinter
import os


def validate(char):
    if char.isdigit():
        return True
    else:
        return False


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
    app.configure(bg='white')
    app.resizable(False, False)

    # Title Frame ------------------------------------------------------------------------------------------------------

    frame_title = tkinter.Frame(app)
    frame_title.configure(bg='white')

    title = tkinter.Label(frame_title, bg="white", text="Music Notation")
    title.config(font=("Arial", 24, 'bold'))
    title.grid(row=0, column=0, pady=(25, 0))

    # Icon -------------------------------------------------------------------------------------------------------------

    image = Image.open(os.getcwd() + "\\images\\icon.png")
    photo = ImageTk.PhotoImage(image.resize((96, 96)))

    icon = tkinter.Label(image=photo, bg="white")
    icon.image = photo

    # Configuration Label ----------------------------------------------------------------------------------------------

    frame_config = tkinter.Frame(app)
    frame_config.configure(bg='white')
    lbl_config = tkinter.Label(frame_config, bg="white", text="Choose Score Configuration Below")
    lbl_config.config(font=("Arial", 18, 'bold'))
    lbl_config.grid(row=0, column=0, pady=(25, 0))

    # Time Signature Text Frame ----------------------------------------------------------------------------------------

    frame_timesig_title = tkinter.Frame(app)
    frame_timesig_title.configure(bg='white')
    lbl_timesig = tkinter.Label(frame_timesig_title, bg="white", text="Time Signature:")
    lbl_timesig.config(font=("Arial", 16))
    lbl_timesig.grid(row=0, column=0, pady=(20, 0))

    # Time Signature Buttons Frame -------------------------------------------------------------------------------------

    frame_timesig_buttons = tkinter.Frame(app)
    frame_timesig_buttons.configure(bg='white')

    timesig_buttons = ["4/4", "3/4", "2/4", "5/4", "12/8", "6/8"]

    for i in range(len(timesig_buttons)):
        btn = tkinter.Button(frame_timesig_buttons, text=timesig_buttons[i], width=12, height=3)
        btn.grid(row=0, column=i, padx=5, pady=(20, 0))

    # Key Signature Text Frame -----------------------------------------------------------------------------------------

    frame_keysig_title = tkinter.Frame(app)
    frame_keysig_title.configure(bg='white')
    lbl_keysig_title = tkinter.Label(frame_keysig_title, bg="white", text="Key Signature:")
    lbl_keysig_title.config(font=("Arial", 16))
    lbl_keysig_title.grid(row=0, column=0, pady=(20, 0))

    # Key Signature Buttons Frame --------------------------------------------------------------------------------------

    frame_keysig_buttons = tkinter.Frame(app)
    frame_keysig_buttons.configure(bg='white')

    keysig_buttons = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

    for i in range(len(keysig_buttons)):
        btn = tkinter.Button(frame_keysig_buttons, text=keysig_buttons[i], width=12, height=3)
        btn.grid(row=0, column=i, padx=5, pady=(20, 0))

    # Tempo Frame ------------------------------------------------------------------------------------------------------

    frame_tempo = tkinter.Frame(app)
    frame_tempo.configure(bg='white')

    lbl_tempo = tkinter.Label(frame_tempo, bg="white", text="Tempo:")
    lbl_tempo.config(font=("Arial", 16))
    lbl_tempo.grid(row=0, column=0, pady=(25, 0))

    entry_tempo = tkinter.Entry(frame_tempo, text="Tempo", validate='key', vcmd=(app.register(validate), '%S'))
    entry_tempo.config(font=("Arial", 16))
    entry_tempo.grid(row=0, column=1, pady=(25, 0))

    lbl_bpm = tkinter.Label(frame_tempo, bg="white", text="bpm")
    lbl_bpm.config(font=("Arial", 16))
    lbl_bpm.grid(row=0, column=2, pady=(25, 0))

    # Create Score Button ----------------------------------------------------------------------------------------------

    frame_create_button = tkinter.Frame(app)
    frame_create_button.configure(bg='white')

    create_button = tkinter.Button(frame_create_button, text="Create Score with Configuration", width=25, height=2)
    create_button.config(font=("Arial", 18))
    create_button.grid(row=2, column=0, pady=(25, 0))

    # Quit Button ------------------------------------------------------------------------------------------------------

    frame_quit = tkinter.Frame(app)
    frame_quit.configure(bg='white')

    btn_quit = tkinter.Button(frame_quit, text="Quit", width=20, height=3)
    btn_quit.grid(row=0, column=0, pady=(20, 0))

    # Assembly ---------------------------------------------------------------------------------------------------------

    frame_title.pack()
    icon.pack()
    frame_config.pack()
    frame_timesig_title.pack()
    frame_timesig_buttons.pack()
    frame_keysig_title.pack()
    frame_keysig_buttons.pack()
    frame_tempo.pack()
    frame_create_button.pack()
    frame_quit.pack()
    app.mainloop()

