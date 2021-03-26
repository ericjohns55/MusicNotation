# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pydub import AudioSegment
from pydub.playback import play
from PIL import Image, ImageTk
from tkinter import Widget
from tkinter import messagebox
import playback
import tkinter
import winsound
import pyglet
import os

from variables import Variables
import score_widget


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


def validate_form():
    if not Variables.key_sig == "N" and not Variables.time_sig == "N" and Variables.tempo > 0:
        generate_scene(False)
    else:
        error = ""

        if Variables.key_sig == "N":
            error += "Please select a valid key signature.\n"
        if Variables.time_sig == "N":
            error += "Please select a valid time signature.\n"
        if not Variables.tempo > 0:
            error += "Please enter a valid tempo (greater than 0)"

        messagebox.showerror("Invalid Configuration", error)


def generate_scene(scene):
    # App Icon
    image = Image.open(os.getcwd() + "\\images\\icon.png")
    photo = ImageTk.PhotoImage(image.resize((96, 96)))

    icon = tkinter.Label(image=photo, bg=background_color)
    icon.image = photo

    # Staff
    staff_image = Image.open(os.getcwd() + "\\images\\staff.png")
    resized = ImageTk.PhotoImage(staff_image.resize((1280, 576)))

    imageView = tkinter.Label(image=resized, bg=background_color)
    imageView.image = resized

    # Main Scene Frame Declaration

    frame_title = tkinter.Frame(app)
    frame_config = tkinter.Frame(app)
    frame_timesig_title = tkinter.Frame(app)
    frame_timesig_buttons = tkinter.Frame(app, name="time_sig")
    frame_keysig_title = tkinter.Frame(app)
    frame_keysig_buttons = tkinter.Frame(app, name="key_sig")
    frame_tempo = tkinter.Frame(app)
    frame_create_button = tkinter.Frame(app)
    frame_quit = tkinter.Frame(app)

    # Score Scene Frame Declaration

    frame_row1 = tkinter.Frame(app)
    frame_row2 = tkinter.Frame(app)
    frame_note_length = tkinter.Frame(frame_row1, name="note_length")
    frame_notes = tkinter.Frame(frame_row1)
    frame_accidentals = tkinter.Frame(frame_row2)
    frame_octave = tkinter.Frame(frame_row2)
    frame_play = tkinter.Frame(frame_row2)
    frame_returns = tkinter.Frame(frame_row2)

    # Main Scene
    if scene:
        remove_children()
        text_entry.delete(1.0, tkinter.END)

        # Title Frame --------------------------------------------------------------------------------------------------

        frame_title.configure(bg=background_color)

        title = tkinter.Label(frame_title, bg=background_color, text="Music Notation", fg=foreground_color)
        title.config(font=("Arial", 24, 'bold'))
        title.grid(row=0, column=0, pady=(25, 0))

        # Configuration Label ------------------------------------------------------------------------------------------

        frame_config.configure(bg=background_color)
        lbl_config = tkinter.Label(frame_config, bg=background_color, text="Choose Score Configuration Below",
                                   fg=foreground_color)
        lbl_config.config(font=("Arial", 18, 'bold'))
        lbl_config.grid(row=0, column=0, pady=(25, 0))

        # Time Signature Text Frame ------------------------------------------------------------------------------------

        frame_timesig_title.configure(bg=background_color)
        lbl_timesig = tkinter.Label(frame_timesig_title, bg=background_color, text="Time Signature:",
                                    fg=foreground_color)
        lbl_timesig.config(font=("Arial", 16))
        lbl_timesig.grid(row=0, column=0, pady=(20, 0))

        # Time Signature Buttons Frame ---------------------------------------------------------------------------------

        frame_timesig_buttons.configure(bg=background_color)

        timesig_buttons = ["4/4", "3/4", "2/4", "6/8", "Cut"]

        for i in range(len(timesig_buttons)):
            btn_timesig = tkinter.Button(frame_timesig_buttons, text=timesig_buttons[i], width=12, height=3)
            btn_timesig.config(command=lambda btn_timesig=btn_timesig: select_option(btn_timesig))
            btn_timesig.grid(row=0, column=i, padx=5, pady=(20, 0))

        # Key Signature Text Frame -------------------------------------------------------------------------------------

        frame_keysig_title.configure(bg=background_color)
        lbl_keysig_title = tkinter.Label(frame_keysig_title, bg=background_color, text="Key Signature:",
                                         fg=foreground_color)
        lbl_keysig_title.config(font=("Arial", 16))
        lbl_keysig_title.grid(row=0, column=0, pady=(20, 0))

        # Key Signature Buttons Frame ----------------------------------------------------------------------------------

        frame_keysig_buttons.configure(bg=background_color)

        keysig_buttons = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

        for i in range(len(keysig_buttons)):
            btn_keysig = tkinter.Button(frame_keysig_buttons, text=keysig_buttons[i], width=12, height=3)
            btn_keysig.config(command=lambda btn_keysig=btn_keysig: select_option(btn_keysig))
            btn_keysig.grid(row=0, column=i, padx=5, pady=(20, 0))

        # Tempo Frame --------------------------------------------------------------------------------------------------

        frame_tempo.configure(bg=background_color)

        lbl_tempo = tkinter.Label(frame_tempo, bg=background_color, text="Tempo:", fg=foreground_color)
        lbl_tempo.config(font=("Arial", 16))
        lbl_tempo.grid(row=0, column=0, pady=(25, 0))

        string_var = tkinter.StringVar()
        string_var.trace("w", lambda name, index, mode, string_var=string_var: tempo_change())

        def tempo_change():
            Variables.tempo = int(string_var.get())
            return True

        entry_tempo = tkinter.Entry(frame_tempo, text="Tempo", validate='key', vcmd=(app.register(validate), '%S'),
                                    textvariable=string_var)
        entry_tempo.config(font=("Arial", 16))
        entry_tempo.grid(row=0, column=1, pady=(25, 0))

        lbl_bpm = tkinter.Label(frame_tempo, bg=background_color, text="bpm", fg=foreground_color)
        lbl_bpm.config(font=("Arial", 16))
        lbl_bpm.grid(row=0, column=2, pady=(25, 0))

        # Create Score Button ------------------------------------------------------------------------------------------

        frame_create_button.configure(bg=background_color)

        create_button = tkinter.Button(frame_create_button, text="Create Score with Configuration", width=25, height=2,
                                       command=lambda: validate_form())
        create_button.config(font=("Arial", 18))
        create_button.grid(row=0, column=0, padx=5, pady=(25, 10))

        load_button = tkinter.Button(frame_create_button, text="Load Score from File", width=25, height=2)
        load_button.config(font=("Arial", 18))
        load_button.grid(row=0, column=1, padx=5, pady=(25, 10))

        # Quit Button --------------------------------------------------------------------------------------------------

        frame_quit.configure(bg=background_color)

        btn_quit = tkinter.Button(frame_quit, text="Quit", width=20, height=3, command=quit)
        btn_quit.grid(row=0, column=0, pady=(10, 0))

        # Assembly -----------------------------------------------------------------------------------------------------

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
    else:
        remove_children()

        # Row Frames ---------------------------------------------------------------------------------------------------

        frame_row1.configure(bg=background_color)

        frame_row2.configure(bg=background_color)

        # Score Frame --------------------------------------------------------------------------------------------------

        # score = setup_score.ScoreSetup(Variables.time_sig, Variables.key_sig, Variables.tempo)

        text_entry.config(font=("Musiqwik", 42))
        text_entry.setup_score()
        # text_entry.bind("<<TextModified>>", score_modify)

        text_entry.pack()


        # Note Length Buttons Frame ------------------------------------------------------------------------------------

        frame_note_length.configure(bg=background_color)

        note_lengths = ["1/8", "1/4", "1/2", "1"]

        for i in range(len(note_lengths)):
            btn_note_length = tkinter.Button(frame_note_length, text=note_lengths[i], width=12, height=3)
            btn_note_length.config(command=lambda btn_note_length=btn_note_length: select_option(btn_note_length))
            btn_note_length.grid(row=0, column=i, padx=5, pady=(10, 0))

            if btn_note_length.cget("text") == "1/4":
                btn_note_length.config(bg=selected_color)


        # Notes Button Frame -------------------------------------------------------------------------------------------

        frame_notes.configure(bg=background_color)

        note_lengths = ["A", "B", "C", "D", "E", "F", "G", "Rest"]

        for i in range(len(note_lengths)):
            btn_note_name = tkinter.Button(frame_notes, text=note_lengths[i], width=12, height=3)
            btn_note_name.config(command=lambda btn_note_name=btn_note_name: note_button(btn_note_name))
            btn_note_name.grid(row=0, column=i, padx=5, pady=(10, 0))

        # Accidentals Button Frame -------------------------------------------------------------------------------------

        frame_accidentals.configure(bg=background_color)

        btn_flat = tkinter.Button(frame_accidentals, text="b", width=12, height=3, command=lambda: accidentals(btn_flat))
        btn_flat.grid(row=0, column=0, padx=5)

        btn_sharp = tkinter.Button(frame_accidentals, text="#", width=12, height=3, command=lambda: accidentals(btn_sharp))
        btn_sharp.grid(row=0, column=1, padx=5)

        # Octave Buttons Frame -----------------------------------------------------------------------------------------

        frame_octave.configure(bg=background_color)

        lbl_octave = tkinter.Label(frame_octave, bg=background_color, text="Octave: +0", fg=foreground_color,
                                   width=12, height=3)

        btn_octave_dec = tkinter.Button(frame_octave, text="-", width=12, height=3,
                                        command=lambda: update_octave(False, lbl_octave))
        btn_octave_dec.grid(row=0, column=0, padx=5)

        lbl_octave.config(font=("Arial", 16))
        lbl_octave.grid(row=0, column=1, padx=(0, 20))

        btn_octave_inc = tkinter.Button(frame_octave, text="+", width=12, height=3,
                                        command=lambda: update_octave(True, lbl_octave))
        btn_octave_inc.grid(row=0, column=2, padx=5)

        # Play/Pause Button Frame --------------------------------------------------------------------------------------

        frame_play.configure(bg=background_color)

        btn_play = tkinter.Button(frame_play, text="Play", width=18, height=3, command=lambda: play_score(btn_play))
        btn_play.grid(row=0, column=0)

        # Return Buttons -----------------------------------------------------------------------------------------------

        frame_returns.configure(bg=background_color)

        btn_return = tkinter.Button(frame_returns, text="Return to Main Menu", width=17, height=3,
                                    command=lambda: generate_scene(True))
        btn_return.grid(row=0, column=0, padx=(15, 5))

        btn_save = tkinter.Button(frame_returns, text="Save", width=17, height=3)
        btn_save.grid(row=0, column=1, padx=5)

        btn_shutdown = tkinter.Button(frame_returns, text="Quit", width=17, height=3, command=quit)
        btn_shutdown.grid(row=0, column=2, padx=5)

        # Pack Frames --------------------------------------------------------------------------------------------------

        frame_score.pack()
        frame_notes.grid(row=0, column=0, padx=(14, 5))
        frame_note_length.grid(row=0, column=1, padx=(5, 14))
        frame_play.grid(row=0, column=0, padx=(18, 5), pady=(0, 0))
        frame_accidentals.grid(row=0, column=1, padx=(50, 32), pady=(0, 0))
        frame_octave.grid(row=0, column=2, padx=(19, 0), pady=(0, 0))
        frame_returns.grid(row=0, column=3, padx=(0, 25), pady=(0, 0))
        frame_row1.pack()
        frame_row2.pack()


def remove_children():
    widgets = app.winfo_children()

    for item in widgets:
        item.pack_forget()


def update_octave(increment, lbl):
    Variables.octave = int(lbl.cget("text")[-1])
    Variables.octave += (1 if increment else -1)

    if 0 <= Variables.octave <= 2:
        lbl.config(text=("Octave: +" + str(Variables.octave)))


def accidentals(button):
    def clear_other():
        children = Widget.nametowidget(app, button.winfo_parent()).winfo_children()

        for child in children:
            if not child == button:
                child.config(bg=button_background)

    if button.cget("bg") == selected_color:
        button.config(bg=button_background)
        clear_other()
        Variables.accidental = 1
    else:
        button.config(bg=selected_color)
        clear_other()

        if button.cget("text") == "b":
            Variables.accidental = 0
        else:
            Variables.accidental = 2


def select_option(button):
    parent_frame = Widget.nametowidget(app, button.winfo_parent())
    children = parent_frame.winfo_children()

    for child in children:
        child.config(bg=button_background)

    button.config(bg=selected_color)

    frame_name = parent_frame.winfo_name()

    if frame_name == "time_sig":
        Variables.time_sig = button.cget("text")
    elif frame_name == "key_sig":
        Variables.key_sig = button.cget("text")
    elif frame_name == "note_length":
        Variables.note_length = int(button.cget("text").replace("1/", ""))


def note_button(button):
    note_name = button.cget("text")

    if note_name.lower() == "rest":
        note_name = "R"

    text_entry.add_note(note_name, False)


def play_score(button):
    Variables.playing = not Variables.playing

    score_playback = playback.Playback(text_entry.get(1.0, tkinter.END))

    if Variables.playing:
        button.configure(text="Stop")

        winsound.Beep(440, 100)
        winsound.Beep(540, 100)

        score_playback.parse()

        Variables.playing = False
        button.configure(text="Play")
    else:
        button.configure(text="Play")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    background_color = "white"
    foreground_color = "black"
    button_background = "SystemButtonFace"
    selected_color = "lightgray"

    app = tkinter.Tk()
    app.title("Music Notation")
    app.geometry("1280x720")
    app.configure(bg=background_color)
    app.resizable(False, False)

    pyglet.font.add_file(os.getcwd() + "\\Musiqwik.ttf")

    frame_score = tkinter.Frame(app)
    text_entry = score_widget.ScoreWidget(frame_score, width=1200, height=5)

    generate_scene(True)

    app.mainloop()
