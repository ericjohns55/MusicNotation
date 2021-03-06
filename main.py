# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image, ImageTk
from tkinter import Widget
from tkinter import messagebox
from tkinter import filedialog
from os.path import expanduser
import playback
import tkinter
import pyglet
import os

from variables import Variables
import score_widget


# make sure only digits can be inputted into the tempo field
def validate(char):
    if char.isdigit():
        return True
    else:
        return False


# make sure all settings are selected before creating the score
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
        Variables.tempo = 0
        Variables.current_measure_length = 0.0
        Variables.time_sig = "N"
        Variables.key_sig = "N"

        if Variables.file_setup:
            Variables.file_setup = False
            Variables.file_score = ""

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

        def tempo_change(): # grab tempo in tempo box
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

        load_button = tkinter.Button(frame_create_button, text="Load Score from File", width=25, height=2, command=load_file)
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
    else:   # generate score screen
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

        accidentals_text = ["b", "N", "#"]

        for i in range(len(accidentals_text)):
            btn_accidental = tkinter.Button(frame_accidentals, text=accidentals_text[i], width=8, height=3)
            btn_accidental.config(command=lambda btn_accidental=btn_accidental: accidentals(btn_accidental))
            btn_accidental.grid(row=0, column=i, padx=5, pady=(0, 0))

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

        btn_play = tkinter.Button(frame_play, text="Play", width=18, height=3, command=lambda: play_score())
        btn_play.grid(row=0, column=0)

        # Return Buttons -----------------------------------------------------------------------------------------------

        frame_returns.configure(bg=background_color)

        btn_return = tkinter.Button(frame_returns, text="Return to Main Menu", width=17, height=3,
                                    command=lambda: generate_scene(True))
        btn_return.grid(row=0, column=0, padx=(15, 5))

        btn_save = tkinter.Button(frame_returns, text="Save", width=17, height=3, command=save_file)
        btn_save.grid(row=0, column=1, padx=5)

        btn_shutdown = tkinter.Button(frame_returns, text="Quit", width=17, height=3, command=quit)
        btn_shutdown.grid(row=0, column=2, padx=5)

        # Pack Frames --------------------------------------------------------------------------------------------------

        frame_score.pack()
        frame_notes.grid(row=0, column=0, padx=(14, 5))
        frame_note_length.grid(row=0, column=1, padx=(5, 14))
        frame_play.grid(row=0, column=0, padx=(18, 5), pady=(0, 0))
        frame_accidentals.grid(row=0, column=1, padx=(40, 22), pady=(0, 0))
        frame_octave.grid(row=0, column=2, padx=(19, 0), pady=(0, 0))
        frame_returns.grid(row=0, column=3, padx=(0, 25), pady=(0, 0))
        frame_row1.pack()
        frame_row2.pack()


# remove all widgets from view
def remove_children():
    widgets = app.winfo_children()

    for item in widgets:
        item.pack_forget()


# update the current input octave
def update_octave(increment, lbl):
    Variables.octave = int(lbl.cget("text")[-1])
    Variables.octave += (1 if increment else -1)

    if 0 <= Variables.octave <= 2:
        lbl.config(text=("Octave: +" + str(Variables.octave)))


# accidentals listener
def accidentals(button):
    # clear other selected accidentals
    def clear_other():
        children = Widget.nametowidget(app, button.winfo_parent()).winfo_children()

        for child in children:
            if not child == button:
                child.config(bg=button_background)

    # deselect if already selected
    if button.cget("bg") == selected_color:
        button.config(bg=button_background)
        clear_other()
        Variables.accidental = 1
    else:
        button.config(bg=selected_color)
        clear_other()

        # load accidentals
        if button.cget("text") == "b":
            Variables.accidental = 0
        elif button.cget("text") == "#":
            Variables.accidental = 2
        else:
            Variables.accidental = 3


# listener for buttons where you can only select one in a row
# deselects other buttons when you grab one so there is no confusion
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


# button input for score window
def note_button(button):
    note_name = button.cget("text")

    if note_name.lower() == "rest":
        note_name = "R"

    text_entry.add_note(note_name, False)


# playback button listener
def play_score():
    Variables.playing = True
    score_playback = playback.Playback(text_entry.get(1.0, tkinter.END))
    score_playback.parse()
    score_playback.play_score()



def load_file():
    # grab file from box
    filename = filedialog.askopenfilename(initialdir=expanduser("~\\Desktop"), title="Select a Score File",
                                          filetypes=[("Score Files", "*.mn")])
    file = open(filename, "r")

    config = file.readline()

    # parse settings line
    settings = config.replace("||", "").replace("\n", "").split(";")
    key_sig = "N"
    time_sig = "N"
    tempo = 0
    current_length = -1.0

    # parse and load settings
    for i in range(len(settings)):
        read_setting = settings[i].split(":")

        if read_setting[0] == "key_sig":
            key_sig = read_setting[1]
        elif read_setting[0] == "tempo":
            tempo = int(read_setting[1])
        elif read_setting[0] == "time_sig":
            time_sig = read_setting[1]
        elif read_setting[0] == "current_length":
            current_length = float(read_setting[1])

    # check file validity
    if key_sig == "N" or time_sig == "N" or tempo == 0 or current_length == -1.0:
        messagebox.showerror("Invalid File", "Could not load score settings from file")
    else:
        # load settings if acceptable
        Variables.tempo = tempo
        Variables.key_sig = key_sig
        Variables.time_sig = time_sig
        Variables.current_measure_length = current_length

        Variables.file_setup = True
        Variables.file_score = file.readline().replace("Â", "")   # for reasons i dont understand it adds this character
        generate_scene(False)   # load score page

    file.close()


def save_file():
    # create file save dialog
    file = filedialog.asksaveasfile(initialdir=expanduser("~\\Desktop"), mode='w', defaultextension=".mn",
                                    filetypes=[("Score Files", "*.mn")])

    # if file doesnt exist, give up
    if file is None:
        messagebox.showerror("Invalid File", "Invalid filename specified")
        return

    # save settings and load score to file
    config = "||key_sig:" + Variables.key_sig + ";tempo:" + str(Variables.tempo) + ";time_sig:" + Variables.time_sig \
             + ";current_length: " + str(Variables.current_measure_length) + "||\n"
    file.write(config + text_entry.get(1.0, "end-1c"))
    file.close()


if __name__ == '__main__':
    # themes
    background_color = "white"
    foreground_color = "black"
    button_background = "SystemButtonFace"
    selected_color = "lightgray"

    # generate window
    app = tkinter.Tk()
    app.title("Music Notation")
    app.geometry("1280x720")
    app.configure(bg=background_color)
    app.resizable(False, False)

    # load music font
    pyglet.font.add_file(os.getcwd() + "\\Musiqwik.ttf")

    # generate score widget
    frame_score = tkinter.Frame(app)
    text_entry = score_widget.ScoreWidget(frame_score, width=1200, height=5)

    # load widgets (default first)
    generate_scene(True)

    app.mainloop()
