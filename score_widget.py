import tkinter
import note_lookup
from variables import Variables


class ScoreWidget(tkinter.Text):
    def __init__(self, *args, **kwargs):
        tkinter.Text.__init__(self, *args, **kwargs)

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, command, *args):
        cmd = (self._orig, command) + args
        result = self.tk.call(cmd)

        # print(command, args, "=>", result)

        if command in ("insert", "delete", "replace"):
            self.event_generate("<<TextModified>>")

        if command == "insert" and len(args[1]) == 1:
            self.add_note(args[1], self.get(1.0, tkinter.END))

        return result

    def add_note(self, note, full_string):

        string = self.get(1.0, "end-2c")

        current_note = note.upper()

        if Variables.accidental == 0:
            current_note += "b"
        elif Variables.accidental == 2:
            current_note += "S"

        current_note += str(Variables.octave)

        self.delete("1.0", tkinter.END)
        self.insert(tkinter.END, string)

        if current_note in note_lookup.note_dictionary[str(Variables.note_length)]:
            note_addition = note_lookup.note_dictionary[str(Variables.note_length)][current_note]
            self.insert(tkinter.END, note_addition)

