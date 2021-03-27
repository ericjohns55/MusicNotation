import tkinter
from note_lookup import LookupNote
import font_dictionary
from variables import Variables
import note_lookup
import difflib
import math
from playback import Playback
from tkinter import messagebox


class ScoreWidget(tkinter.Text):
    def __init__(self, *args, **kwargs):
        tkinter.Text.__init__(self, *args, **kwargs)

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)
        self.previous_text = ""

    def _proxy(self, command, *args):
        cmd = (self._orig, command) + args
        result = self.tk.call(cmd)

        # print(command, args, "=>", result)

        if command in ("insert", "delete", "replace"):
            self.event_generate("<<TextModified>>")

        if command == "insert" and len(args[1]) == 1:
            self.add_note(args[1], True)
        elif command == "delete" and len(args) == 1:
            self.remove_note()

        return result

    def setup_score(self):
        if Variables.file_setup:
            score = Variables.file_score
        else:
            score = "&=" + font_dictionary.key_sig_lookup[Variables.key_sig] + "=" + \
                    font_dictionary.time_sig_lookup[Variables.time_sig] + "=="

        self.insert(1.0, score)
        self.previous_text = score

    def remove_note(self):
        new_text = self.get(1.0, "end-1c")

        new_string = " "

        for i, s in enumerate(difflib.ndiff(self.previous_text, self.get(1.0, tkinter.END))):
            if s[0] == "-":
                new_string = new_text[:i] + LookupNote.convert_to_rest(s[-1]) + new_text[i:]
                break

        self.delete(1.0, tkinter.END)
        self.insert(1.0, new_string)

    def add_note(self, note, input_event):
        insert_index = self.index(tkinter.INSERT)

        if note == "`":
            self.break_rest(insert_index)
            return

        if int(insert_index.split(".")[1]) == len(self.get(1.0, "end-1c")):  # PROBLEM HERE
            if input_event:
                string = self.get(1.0, "end-2c")
            else:
                string = self.get(1.0, "end-1c")

            current_note = note.upper()

            self.delete("1.0", tkinter.END)
            self.insert(tkinter.END, string)

            if Variables.octave == 2 and ord(current_note) > 65:
                return

            if Variables.current_measure_length + (1.0 / float(Variables.note_length)) > Variables.get_measure_length():
                messagebox.showerror("Invalid Configuration", "ERROR: This note is too long to fit in this measure!")
                return

            if current_note in note_lookup.naturals:
                if current_note == "R":
                    append = LookupNote.get_rest(Variables.note_length)
                else:
                    append = LookupNote.get_note(current_note, Variables.octave, Variables.note_length,
                                                 Variables.accidental, Variables.key_sig)

                self.insert(tkinter.END, append)
            else:
                return

            Playback.play_tone(current_note, Variables.octave, Variables.accidental)

            Variables.current_measure_length += 1.0 / float(Variables.note_length)

            if math.isclose(Variables.get_measure_length(), Variables.current_measure_length):
                Variables.current_measure_length = 0.0
                self.insert(tkinter.END, "!=")

            self.save_last_text()
        else:
            split = insert_index.split(".")
            next_index = split[0] + "." + str(int(split[1]) + 1)
            character = self.get(insert_index, next_index)

            if LookupNote.replaceable(character):
                rest_char = self.get(insert_index, next_index)
                first_half = self.get(1.0, split[0] + "." + str(int(split[1]) - 1))
                second_half = self.get(split[0] + "." + str(int(split[1]) + 2), "end-1c")

                new_note = LookupNote.get_note(note.upper(), Variables.octave, LookupNote.get_note_length(rest_char),
                                               Variables.accidental, Variables.key_sig)

                self.delete(1.0, tkinter.END)
                self.insert(tkinter.END, first_half + new_note + second_half)

                Playback.play_tone(note.upper(), Variables.octave, Variables.accidental)

                self.save_last_text()
            else:
                self.delete(1.0, tkinter.END)
                self.insert(1.0, self.previous_text)

    def break_rest(self, insert_index):
        split = insert_index.split(".")
        next_index = split[0] + "." + str(int(split[1]) + 1)

        if len(self.get(insert_index, next_index)) == 1:
            character = self.get(insert_index, next_index)

            if len(character) != 0 and LookupNote.breakable(character):
                if character == ":":
                    replace = "9=9="
                elif character == ";":
                    replace = ":=:="
                elif character == "<":
                    replace = ";=;="
                else:
                    note = chr(ord(character) - 16)
                    rest = LookupNote.get_rest(LookupNote.get_note_length(note))
                    replace = note + "=" + rest

                first_half = self.get(1.0, split[0] + "." + str(int(split[1]) - 1))
                second_half = self.get(split[0] + "." + str(int(split[1]) + 2), "end-1c")

                self.delete(1.0, tkinter.END)
                self.insert(tkinter.END, first_half + replace + second_half)

                self.save_last_text()
            else:
                self.cancel_event()
        else:
            self.cancel_event()

    def cancel_event(self):
        self.delete(1.0, tkinter.END)
        self.insert(1.0, self.previous_text)

    def save_last_text(self):
        self.previous_text = self.get(1.0, "end-1c")

        if not self.previous_text.endswith("="):
            self.previous_text += "="
