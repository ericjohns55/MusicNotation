from note import Note
from note_lookup import LookupNote
from variables import Variables
import winsound


class Playback:
    def __init__(self, text):
        self.score = text
        self.notes = []

    def parse(self):
        # remove beginning part of score that provides playing information
        array = self.score[7:]

        # split at measure lines - ! symbols in the font
        measures = array.split("!")

        # loop over each measure
        for i in range(len(measures)):
            # split the measure into notes
            individual_notes = measures[i].split("=")

            # loop through all notes
            for j in range(len(individual_notes)):
                # make sure no whitespace escaped the filter
                if individual_notes[j] != "" and individual_notes[j] != "\n":
                    # send the excerpt into the note class to parse input
                    note = Note(individual_notes[j])
                    # append note to list for playback
                    self.notes.append(note)
                    # print(note.get_information())

    def play_score(self):
        # play all notes in the score

        for i in range(len(self.notes)):
            self.notes[i].play()

    # this method exists so when you insert a note into the score you know what it sounds like
    # plays to a default of 150ms
    @staticmethod
    def play_tone(note, octave, accidentals):
        if note.upper() == "R":
            return

        note_name = note.upper() + str(octave)

        # check if note is in key sig table and has no accidental
        if note in LookupNote.key_sig[Variables.key_sig] and Variables.accidental == 1:
            accidental_adjust = LookupNote.key_sig[Variables.key_sig][note]
        else:
            accidental_adjust = accidentals

        # grab frequency from the lookup tables in the note class
        if accidental_adjust == 0:
            frequency = Note.flat_frequencies[note_name]
        elif accidental_adjust == 1 or accidental_adjust == 3:
            frequency = Note.natural_frequencies[note_name]
        else:
            frequency = Note.sharp_frequencies[note_name]

        winsound.Beep(frequency, 150)

