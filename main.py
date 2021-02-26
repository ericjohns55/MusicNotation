# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pydub import AudioSegment
from pydub.playback import play
from PIL import Image, ImageTk
import tkinter
import keyboard
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

    mixed_audio1 = c_note.overlay(e_note).overlay(g_note).overlay(as_note)[0.1:1000]
    mixed_audio2 = g_note.overlay(b_note).overlay(d_note).overlay(ghigh_note)[0.1:1000]

    play(mixed_audio1)
    play(mixed_audio2)


def key_press_event(event):
    char_list = list(event.name.lower())
    char = ord(char_list[0])

    if len(char_list) == 1 and 97 <= char <= 103:
        note = AudioSegment.from_mp3(os.getcwd() + "\\sound\\" + chr(char).upper() + "4.mp3")[:200]
        play(note)


def main_scene():
    print("EEE")



def score_scene():
    frame_title.pack_forget()
    icon.pack_forget()
    frame_config.pack_forget()
    frame_timesig_title.pack_forget()
    frame_timesig_buttons.pack_forget()
    frame_keysig_title.pack_forget()
    frame_keysig_buttons.pack_forget()
    frame_tempo.pack_forget()
    frame_create_button.pack_forget()
    frame_quit.pack_forget()

    # Icon -------------------------------------------------------------------------------------------------------------

    staff_image = Image.open(os.getcwd() + "\\images\\staff.png")
    resized = ImageTk.PhotoImage(staff_image.resize((1280, 576)))

    imageView = tkinter.Label(image=resized, bg=background_color)
    imageView.image = resized

    # Frame Frame ------------------------------------------------------------------------------------------------------

    frame_rows = tkinter.Frame(app)
    frame_rows.configure(bg=background_color)

    # Note Length Buttons Frame ----------------------------------------------------------------------------------------

    frame_note_length = tkinter.Frame(frame_rows)
    frame_note_length.configure(bg=background_color)

    note_lengths = ["1/16", "1/8", "1/4", "1/2", "1"]

    for i in range(len(note_lengths)):
        btn = tkinter.Button(frame_note_length, text=note_lengths[i], width=12, height=3)
        btn.grid(row=0, column=i, padx=5, pady=(10, 0))

    # Notes Button Frame -----------------------------------------------------------------------------------------------

    frame_notes = tkinter.Frame(frame_rows)
    frame_notes.configure(bg=background_color)

    note_lengths = ["C", "D", "E", "F", "G", "A", "B"]

    for i in range(len(note_lengths)):
        btn = tkinter.Button(frame_notes, text=note_lengths[i], width=12, height=3)
        btn.grid(row=0, column=i, padx=5, pady=(10, 0))

    # Octave Buttons Frame ---------------------------------------------------------------------------------------------

    frame_octave = tkinter.Frame(frame_rows)
    frame_octave.configure(bg=background_color)

    btn_octave_dec = tkinter.Button(frame_octave, text="-", width=12, height=3)
    btn_octave_dec.grid(row=0, column=0, padx=5,)

    lbl_octave = tkinter.Label(frame_octave, bg=background_color, text="Octave: 4", fg=foreground_color, width=12, height=3)
    lbl_octave.config(font=("Arial", 16))
    lbl_octave.grid(row=0, column=1, padx=(0, 20))

    btn_octave_inc = tkinter.Button(frame_octave, text="+", width=12, height=3)
    btn_octave_inc.grid(row=0, column=2, padx=5)

    # Return Buttons ---------------------------------------------------------------------------------------------------

    frame_returns = tkinter.Frame(frame_rows)
    frame_returns.configure(bg=background_color)

    btn_return = tkinter.Button(frame_returns, text="Return to Main Menu", width=30, height=3, command=play_sound)
    btn_return.grid(row=0, column=0, padx=5)

    btn_shutdown = tkinter.Button(frame_returns, text="Quit", width=30, height=3, command=quit)
    btn_shutdown.grid(row=0, column=1, padx=5)

    # Pack Frames ------------------------------------------------------------------------------------------------------

    imageView.pack()
    frame_notes.grid(row=0, column=0, padx=(14, 5))
    frame_note_length.grid(row=0, column=1, padx=(5, 14))
    frame_octave.grid(row=1, column=0, pady=(0, 0))
    frame_returns.grid(row=1, column=1, pady=(0, 0))
    frame_rows.pack()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    background_color = "gray"
    foreground_color = "white"

    app = tkinter.Tk()
    app.title("Music Notation")
    app.geometry("1280x720")
    app.configure(bg=background_color)
    app.resizable(False, False)

    keyboard.on_press(key_press_event)

    # Title Frame ------------------------------------------------------------------------------------------------------

    frame_title = tkinter.Frame(app)
    frame_title.configure(bg=background_color)

    title = tkinter.Label(frame_title, bg=background_color, text="Music Notation", fg=foreground_color)
    title.config(font=("Arial", 24, 'bold'))
    title.grid(row=0, column=0, pady=(25, 0))

    # Icon -------------------------------------------------------------------------------------------------------------

    image = Image.open(os.getcwd() + "\\images\\icon.png")
    photo = ImageTk.PhotoImage(image.resize((96, 96)))

    icon = tkinter.Label(image=photo, bg=background_color)
    icon.image = photo

    # Configuration Label ----------------------------------------------------------------------------------------------

    frame_config = tkinter.Frame(app)
    frame_config.configure(bg=background_color)
    lbl_config = tkinter.Label(frame_config, bg=background_color, text="Choose Score Configuration Below", fg=foreground_color)
    lbl_config.config(font=("Arial", 18, 'bold'))
    lbl_config.grid(row=0, column=0, pady=(25, 0))

    # Time Signature Text Frame ----------------------------------------------------------------------------------------

    frame_timesig_title = tkinter.Frame(app)
    frame_timesig_title.configure(bg=background_color)
    lbl_timesig = tkinter.Label(frame_timesig_title, bg=background_color, text="Time Signature:", fg=foreground_color)
    lbl_timesig.config(font=("Arial", 16))
    lbl_timesig.grid(row=0, column=0, pady=(20, 0))

    # Time Signature Buttons Frame -------------------------------------------------------------------------------------

    frame_timesig_buttons = tkinter.Frame(app)
    frame_timesig_buttons.configure(bg=background_color)

    timesig_buttons = ["4/4", "3/4", "2/4", "5/4", "12/8", "6/8"]

    for i in range(len(timesig_buttons)):
        btn = tkinter.Button(frame_timesig_buttons, text=timesig_buttons[i], width=12, height=3)
        btn.grid(row=0, column=i, padx=5, pady=(20, 0))

    # Key Signature Text Frame -----------------------------------------------------------------------------------------

    frame_keysig_title = tkinter.Frame(app)
    frame_keysig_title.configure(bg=background_color)
    lbl_keysig_title = tkinter.Label(frame_keysig_title, bg=background_color, text="Key Signature:", fg=foreground_color)
    lbl_keysig_title.config(font=("Arial", 16))
    lbl_keysig_title.grid(row=0, column=0, pady=(20, 0))

    # Key Signature Buttons Frame --------------------------------------------------------------------------------------

    frame_keysig_buttons = tkinter.Frame(app)
    frame_keysig_buttons.configure(bg=background_color)

    keysig_buttons = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

    for i in range(len(keysig_buttons)):
        btn = tkinter.Button(frame_keysig_buttons, text=keysig_buttons[i], width=12, height=3)
        btn.grid(row=0, column=i, padx=5, pady=(20, 0))

    # Tempo Frame ------------------------------------------------------------------------------------------------------

    frame_tempo = tkinter.Frame(app)
    frame_tempo.configure(bg=background_color)

    lbl_tempo = tkinter.Label(frame_tempo, bg=background_color, text="Tempo:", fg=foreground_color)
    lbl_tempo.config(font=("Arial", 16))
    lbl_tempo.grid(row=0, column=0, pady=(25, 0))

    entry_tempo = tkinter.Entry(frame_tempo, text="Tempo", validate='key', vcmd=(app.register(validate), '%S'))
    entry_tempo.config(font=("Arial", 16))
    entry_tempo.grid(row=0, column=1, pady=(25, 0))

    lbl_bpm = tkinter.Label(frame_tempo, bg=background_color, text="bpm", fg=foreground_color)
    lbl_bpm.config(font=("Arial", 16))
    lbl_bpm.grid(row=0, column=2, pady=(25, 0))

    # Create Score Button ----------------------------------------------------------------------------------------------

    frame_create_button = tkinter.Frame(app)
    frame_create_button.configure(bg=background_color)

    create_button = tkinter.Button(frame_create_button, text="Create Score with Configuration", width=25, height=2, command=score_scene)
    create_button.config(font=("Arial", 18))
    create_button.grid(row=2, column=0, pady=(25, 10))

    # Quit Button ------------------------------------------------------------------------------------------------------

    frame_quit = tkinter.Frame(app)
    frame_quit.configure(bg=background_color)

    btn_quit = tkinter.Button(frame_quit, text="Quit", width=20, height=3, command=quit)
    btn_quit.grid(row=0, column=0, pady=(10, 0))

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

