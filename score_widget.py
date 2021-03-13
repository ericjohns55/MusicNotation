import tkinter
from note_lookup import LookupNote
import font_dictionary
from variables import Variables
import note_lookup
import difflib
import math


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
            self.add_note(args[1], True)    # self.get(1.0, tkinter.END)
        elif command == "delete" and len(args) == 1:
            # print("DELETE: " + self.get(1.0, tkinter.END))
            self.remove_note()

        return result

    def setup_score(self):
        score = "&=" + font_dictionary.key_sig_lookup[Variables.key_sig] + "=" +\
               font_dictionary.time_sig_lookup[Variables.time_sig] + "=="
        self.insert(1.0, score)
        self.previous_text = score

    def remove_note(self):
        # print("Original: " + self.previous_text)
        # print("New: " + self.get(1.0, tkinter.END))

        new_text = self.get(1.0, "end-1c")

        new_string = " "

        for i, s in enumerate(difflib.ndiff(self.previous_text, self.get(1.0, tkinter.END))):
            if s[0] == "-":
                print("Deleted " + s[-1] + " from index " + str(i))
                new_string = new_text[:i] + LookupNote.convert_to_rest(s[-1]) + new_text[i:]
                print(new_text)
                break

        self.delete(1.0, tkinter.END)
        self.insert(1.0, new_string)

    def add_note(self, note, input_event):
        if input_event:
            string = self.get(1.0, "end-2c")
        else:
            string = self.get(1.0, "end-1c")

        current_note = note.upper()

        self.delete("1.0", tkinter.END)
        self.insert(tkinter.END, string)

        if Variables.octave == 2 and ord(current_note) > 65:
            return

        if current_note in note_lookup.naturals:
            if current_note == "R":
                append = LookupNote.get_rest(Variables.note_length)
            else:
                append = LookupNote.get_note(current_note, Variables.octave, Variables.note_length,
                                                     Variables.accidental)
            self.insert(tkinter.END, append)
        else:
            return

        Variables.current_measure_length += 1.0 / float(Variables.note_length)

        if Variables.current_measure_length > Variables.get_measure_length():
            Variables.current_measure_length = 0.0          # Fix issues in case something gets off

        if math.isclose(Variables.get_measure_length(), Variables.current_measure_length):
            Variables.current_measure_length = 0.0
            self.insert(tkinter.END, "!=")

        self.previous_text = self.get(1.0, tkinter.END)



