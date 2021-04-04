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
    # default constructor
    def __init__(self, *args, **kwargs):
        tkinter.Text.__init__(self, *args, **kwargs)

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)
        self.previous_text = ""

    # event listener
    def _proxy(self, command, *args):
        cmd = (self._orig, command) + args
        result = self.tk.call(cmd)

        # print(command, args, "=>", result)

        if command in ("insert", "delete", "replace"):
            self.event_generate("<<TextModified>>")

        # grab trace of insert and delete commands, pass in lengths
        if command == "insert" and len(args[1]) == 1:
            self.add_note(args[1], True)
        elif command == "delete" and len(args) == 1:
            self.remove_note()

        return result

    # lookup and concatenate the score setup information in lookup tables then return them to be placed in the score
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

        # find the difference between the old text and the current text
        for i, s in enumerate(difflib.ndiff(self.previous_text, self.get(1.0, tkinter.END))):
            if s[0] == "-":  # check for deletion
                # new string is the old string up to the remove index, plus the rest conversion, plus the remaining text
                new_string = new_text[:i] + LookupNote.convert_to_rest(s[-1]) + new_text[i:]
                break

        # replace string
        self.delete(1.0, tkinter.END)
        self.insert(1.0, new_string)

    def add_note(self, note, input_event):
        # find insertion index of the note
        insert_index = self.index(tkinter.INSERT)

        # if the inputted key is a `, then run the break apart event
        if note == "`":
            self.break_note(insert_index)
            return

        # check if at end of the score
        if int(insert_index.split(".")[1]) == len(self.get(1.0, "end-1c")):  # PROBLEM HERE
            # if it was a keyboard event, there was an attempt to add text to the text area, remove 2 characters
            # if not keyboard, remove one character from the end (just whitespace)
            if input_event:
                string = self.get(1.0, "end-2c")
            else:
                string = self.get(1.0, "end-1c")

            # convert to upper case for easy keyboard parsing
            current_note = note.upper()

            # nuke the current text to make sure nothing i dont want added is added
            self.delete("1.0", tkinter.END)
            self.insert(tkinter.END, string)

            # check validity of octave 2 (only high A is allowed)
            if Variables.octave == 2 and ord(current_note) > 65:
                return

            # check if current note fits in the measure
            if Variables.current_measure_length + (1.0 / float(Variables.note_length)) > Variables.get_measure_length():
                messagebox.showerror("Invalid Configuration", "ERROR: This note is too long to fit in this measure!")
                return

            # check if the note exists in the naturals table (cross-reference keyboard input to see if valid input)
            if current_note in note_lookup.naturals:
                # check if rest, then add the rest symbol from the lookup class if so
                if current_note == "R":
                    append = LookupNote.get_rest(Variables.note_length)

                # if not a rest, append the note from the symbol generation in the lookup class
                else:
                    append = LookupNote.get_note(current_note, Variables.octave, Variables.note_length,
                                                 Variables.accidental, Variables.key_sig)
                # insert note
                self.insert(tkinter.END, append)
            else:
                return

            # play tone so the user knows what they just added
            Playback.play_tone(current_note, Variables.octave, Variables.accidental)

            # update the current measure length
            Variables.current_measure_length += 1.0 / float(Variables.note_length)

            # compare to see if the measure length was just finished, if so add a measure line
            if math.isclose(Variables.get_measure_length(), Variables.current_measure_length):
                Variables.current_measure_length = 0.0
                self.insert(tkinter.END, "!=")

            # save the new text so it can be compared again if needed on next input event
            self.save_last_text()
        else:  # note is not at the end of the score
            # get the current character at the insertion index
            split = insert_index.split(".")
            next_index = split[0] + "." + str(int(split[1]) + 1)
            character = self.get(insert_index, next_index)

            # if the note is one that can be replaced
            if LookupNote.replaceable(character):
                # parse the insertion index
                first_half = self.get(1.0, split[0] + "." + str(int(split[1]) - 1))
                second_half = self.get(split[0] + "." + str(int(split[1]) + 2), "end-1c")

                # generate new note from the lookup note class using current settings
                new_note = LookupNote.get_note(note.upper(), Variables.octave, LookupNote.get_note_length(character),
                                               Variables.accidental, Variables.key_sig)

                # if there is an accidental symbol, remove it
                if 208 <= ord(first_half[-1]) <= 254:
                    first_half = first_half[0:len(first_half) - 1]

                # delete the old text, insert the new generated text with the new symbol in the insertion index
                self.delete(1.0, tkinter.END)
                self.insert(tkinter.END, first_half + new_note + second_half)

                # play the tone so they know what they inputted
                Playback.play_tone(note.upper(), Variables.octave, Variables.accidental)

                # save the text for future comparisons
                self.save_last_text()
            else:  # cancel the event if replacement is impossible
                self.cancel_event()

    # here we are going to break up rests or old notes into new notes
    def break_note(self, insert_index):
        split = insert_index.split(".")
        next_index = split[0] + "." + str(int(split[1]) + 1)

        # check if the insertion character is 1 long (will glitch out with extra whitespace at end without check)
        if len(self.get(insert_index, next_index)) == 1:
            character = self.get(insert_index, next_index)

            # check if note is breakable
            if LookupNote.breakable(character):
                # if a rest, break into two smaller rests
                if character == ":":
                    replace = "9=9="
                elif character == ";":
                    replace = ":=:="
                elif character == "<":
                    replace = ";=;="
                else:  # if not a rest, break into a note then a rest of the same length
                    note = chr(ord(character) - 16)  # grab note from ascii table 1 length down
                    rest = LookupNote.get_rest(LookupNote.get_note_length(note))    # grab rest
                    replace = note + "=" + rest

                # grab the string around the insertion index
                first_half = self.get(1.0, split[0] + "." + str(int(split[1]) - 1))
                second_half = self.get(split[0] + "." + str(int(split[1]) + 2), "end-1c")

                # delete old text and insert with the insertion
                self.delete(1.0, tkinter.END)
                self.insert(tkinter.END, first_half + replace + second_half)

                # save for future comparisons
                self.save_last_text()
            else:
                self.cancel_event()
        else:
            self.cancel_event()

    # remove the current text, input the last text
    # in case someone adds something that is not supported this ensures the application does not crash and burn
    def cancel_event(self):
        self.delete(1.0, tkinter.END)
        self.insert(1.0, self.previous_text)

    # save the last text
    def save_last_text(self):
        self.previous_text = self.get(1.0, "end-1c")

        # if the text does not end with a whitespace character, add one
        if not self.previous_text.endswith("="):
            self.previous_text += "="
