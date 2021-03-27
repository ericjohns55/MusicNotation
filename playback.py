from note import Note
from note_lookup import LookupNote
from variables import Variables
import winsound

class Playback:
    def __init__(self, text):
        self.score = text
        self.notes = []

    def parse(self):
        array = self.score[7:]

        measures = array.split("!")

        for i in range(len(measures)):
            individual_notes = measures[i].split("=")

            for j in range(len(individual_notes)):
                if individual_notes[j] != "" and individual_notes[j] != "\n":
                    note = Note(individual_notes[j])
                    self.notes.append(note)
                    # print(note.get_information())

    def play_score(self):
        beat_time = 60000 / Variables.tempo

        for i in range(len(self.notes)):
            self.notes[i].play()

    @staticmethod
    def play_tone(note, octave, accidentals):
        if note.upper() == "R":
            return

        note_name = note.upper() + str(octave)

        if note in LookupNote.key_sig[Variables.key_sig] and Variables.accidental == 1:
            accidental_adjust = LookupNote.key_sig[Variables.key_sig][note]
        else:
            accidental_adjust = accidentals

        if accidental_adjust == 0:
            frequency = Note.flat_frequencies[note_name]
        elif accidental_adjust == 1 or accidental_adjust == 3:
            frequency = Note.natural_frequencies[note_name]
        else:
            frequency = Note.sharp_frequencies[note_name]

        winsound.Beep(frequency, 150)
